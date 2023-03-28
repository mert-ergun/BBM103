import numpy as np
import pandas as pd
import random as rd
import time 


def distance(p1, p2):
    """
    Calculates the euclidean distance between two points
    """
    return np.sqrt(np.sum(np.square(p1 - p2)))


def knn(X, Y, query_point, k, weights=None):
    """
    Finds the k nearest neighbours of a query point
    """
    dot_product = np.dot(query_point, X.T)
    
    nearest = np.argsort(dot_product)[-k:]
    nearest_labels = [Y[i] for i in nearest]
    
    if weights is None:
        return max(set(nearest_labels), key=nearest_labels.count)
    else:
        weighted_labels = [nearest_labels[i] * weights[i] for i in range(k)]
        return max(set(weighted_labels), key=weighted_labels.count)
         

def standardize(X):
    """
    Standardizes the data by subtracting the mean and dividing by the standard deviation 
    """
    x_min = np.min(X, axis=0)
    x_max = np.max(X, axis=0)
    
    x_normalized = (X - x_min) / (x_max - x_min)
    
    return x_normalized


df = pd.read_csv('data.csv', encoding='utf-8', encoding_errors='ignore')  # Read the data file which is in csv format and store it in a dataframe


df.drop(['Response Id'], axis=1, inplace=True)  # Drop the Response Id column as it is not required
df.dropna(axis=1, inplace=True)  # Drop the columns with null values if any

personality_labels = {'ESTJ':0, 'ENTJ':1, 'ESFJ':2, 'ENFJ':3, 'ISTJ':4, 'ISFJ':5, 'INTJ':6, 'INFJ':7, 'ESTP':8,
                      'ESFP':9, 'ENTP':10, 'ENFP':11, 'ISTP':12, 'ISFP':13, 'INTP':14, 'INFP':15}  # Dictionary to map the personality types to integers

df.Personality = [personality_labels[item] for item in df.Personality]  # Map the personality types to integers

numpy_array = df.to_numpy()  # Convert the dataframe to a numpy array


folds = np.array_split(numpy_array, 5)

time_start = time.time()
print("Start Time: ", time_start)
for k in (1,3,5,7,9):
	total_accuracies = []
	total_precisions = []
	total_recalls = []

	for m in range(5):
		accuracies = []
		precisions = []
		recalls = []

		test_set = folds[m]
		train_set = np.concatenate(folds[:m] + folds[m+1:])
		print(test_set)
		X_train = train_set[:, :-1]
		Y_train = train_set[:, -1]
		X_test = test_set[:, :-1]
		Y_test = test_set[:, -1]

		confusion_matrix = [[0] * 16 for _ in range(16)]
		for example in test_set:
			true_class = example[-1]
			predicted_class = knn(X_train, Y_train, example[:-1], k)
			if predicted_class == true_class:
				confusion_matrix[true_class][predicted_class] += 1
			else:
				confusion_matrix[true_class][predicted_class] += 1

		for i in range(16):
			true_positives = confusion_matrix[i][i]
			false_positives = sum(confusion_matrix[i][j] for j in range(16) if j != i)
			false_negatives = sum(confusion_matrix[j][i] for j in range(16) if j != i)
			true_negatives = sum(confusion_matrix[j][k] for j in range(16) for k in range(16) if j != i and k != i)
			accuracy = (true_positives + true_negatives) / (true_positives + false_positives + false_negatives + true_negatives)
			precision = true_positives / (true_positives + false_positives)
			recall = true_positives / (true_positives + false_negatives)
			accuracies.append(accuracy)
			precisions.append(precision)
			recalls.append(recall)

		accuracy = sum(accuracies) / len(accuracies)
		precision = sum(precisions) / len(precisions)
		recall = sum(recalls) / len(recalls)

		print('Accuracy For Set ', m+1, ": ", accuracy, "K = {}".format(k))
		print('Precision For Set ', m+1, ": ", precision, "K = {}".format(k))
		print('Recall For Set ', m+1, ": ", recall, "K = {}".format(k))
		set_time = time.time()
		print("Time Taken: ", set_time - time_start)

		total_accuracies.append(accuracy)
		total_precisions.append(precision)
		total_recalls.append(recall)

	accuracy_for_k = sum(total_accuracies) / len(total_accuracies)
	precision_for_k = sum(total_precisions) / len(total_precisions)
	recall_for_k = sum(total_recalls) / len(total_recalls)

	print('Accuracy for K = {}:'.format(k), accuracy_for_k)
	print('Precision for K = {}:'.format(k), precision_for_k)
	print('Recall for K = {}:'.format(k), recall_for_k)




# test_set_size = 0.002 # Size of the test set (0.2% of the total data)
# test_set_indices = rd.sample(range(0, len(df)), int(len(df) * test_set_size))  # Randomly select the indices of the test set

# test_set = df.iloc[test_set_indices]  # Create the test set
# train_set = df.drop(test_set_indices)  # Create the train set

# test_set = test_set.to_numpy()  # Convert the test set to a numpy array
# train_set = train_set.to_numpy()  # Convert the train set to a numpy array

# X = train_set[:, :-1]  # Independent variables (Features)
# Y = train_set[:, -1]  # Dependent variable (Personality (0-15))
# test_set_independent = test_set[:, :-1]  # Independent variables of the test set
# test_set_dependent = test_set[:, -1]  # Dependent variable of the test set


# # Create a confusion matrix with 16 rows and 16 columns
# confusion_matrix = [[0] * 16 for _ in range(16)]

# # Iterate over the test examples
# for example in test_set:
# 	true_class = example[-1]
# 	predicted_class = knn(X, Y, example[:-1], 5)
# 	if predicted_class == true_class:
# 		confusion_matrix[true_class][predicted_class] += 1
# 	else:
# 		confusion_matrix[true_class][predicted_class] += 1

# # Calculate the accuracy, precision, and recall for each class
# for i in range(16):
# 	true_positives = confusion_matrix[i][i]
# 	false_positives = sum(confusion_matrix[i][j] for j in range(16) if j != i)
# 	false_negatives = sum(confusion_matrix[j][i] for j in range(16) if j != i)
# 	total = sum(confusion_matrix[i])
# 	accuracy = true_positives / total
# 	precision = true_positives / (true_positives + false_positives)
# 	recall = true_positives / (true_positives + false_negatives)

# 	# Print the values for accuracy, precision, and recall
# 	print("Class", i)
# 	print("Accuracy:", accuracy)
# 	print("Precision:", precision)
# 	print("Recall:", recall)	

# total_true_positives = sum(confusion_matrix[i][i] for i in range(16))
# total_true_negatives = sum(confusion_matrix[i][j] for i in range(16) for j in range(16) if i != j and j != i)
# total_false_positives = sum(confusion_matrix[i][j] for i in range(16) for j in range(16) if i != j)
# total_false_negatives = sum(confusion_matrix[i][j] for i in range(16) for j in range(16) if i != j)

# total_accuracy = (total_true_positives + total_true_negatives) / (total_true_positives + total_true_negatives + total_false_positives + total_false_negatives)
# total_precision = total_true_positives / (total_true_positives + total_false_positives)
# total_recall = total_true_positives / (total_true_positives + total_false_negatives)

# print("Total Accuracy:", total_accuracy)
# print("Total Precision:", total_precision)
# print("Total Recall:", total_recall)


# normalized_X = standardize(X)  # Normalize the independent variables
# normalized_test_set = standardize(test_set_independent)  # Normalize the independent variables of the test set

# confusion_matrix_normalized = [[0] * 16 for _ in range(16)]

# counter = 0
# for example in normalized_test_set:
# 	true_class = test_set_dependent[counter]
# 	predicted_class = knn(normalized_X, Y, example, 5)
# 	if predicted_class == true_class:
# 		confusion_matrix_normalized[true_class][predicted_class] += 1
# 	else:
# 		confusion_matrix_normalized[true_class][predicted_class] += 1
# 	counter += 1

# for i in range(16):
# 	true_positives = confusion_matrix_normalized[i][i]
# 	false_positives = sum(confusion_matrix_normalized[i][j] for j in range(16) if j != i)
# 	false_negatives = sum(confusion_matrix_normalized[j][i] for j in range(16) if j != i)
# 	total = sum(confusion_matrix_normalized[i])
# 	accuracy = true_positives / total
# 	precision = true_positives / (true_positives + false_positives)
# 	recall = true_positives / (true_positives + false_negatives)

# 	print("Class", i)
# 	print("Accuracy:", accuracy)
# 	print("Precision:", precision)
# 	print("Recall:", recall)

# total_true_positives = sum(confusion_matrix_normalized[i][i] for i in range(16))
# total_true_negatives = sum(confusion_matrix_normalized[i][j] for i in range(16) for j in range(16) if i != j and j != i)
# total_false_positives = sum(confusion_matrix_normalized[i][j] for i in range(16) for j in range(16) if i != j)
# total_false_negatives = sum(confusion_matrix_normalized[i][j] for i in range(16) for j in range(16) if i != j)

# total_normalized_accuracy = (total_true_positives + total_true_negatives) / (total_true_positives + total_true_negatives + total_false_positives + total_false_negatives)
# total_normalized_precision = total_true_positives / (total_true_positives + total_false_positives)
# total_normalized_recall = total_true_positives / (total_true_positives + total_false_negatives)

# print("Total Accuracy:", total_normalized_accuracy)
# print("Total Precision:", total_normalized_precision)
# print("Total Recall:", total_normalized_recall)
