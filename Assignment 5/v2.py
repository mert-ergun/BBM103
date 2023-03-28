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
    dot_product = np.sum(X**2, axis=1) + np.sum(query_point**2) - 2 * np.dot(query_point, X.T)
    
    nearest = np.argsort(dot_product)[:k]
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