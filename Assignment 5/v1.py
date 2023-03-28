import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rd


def distance(p1, p2):
    """
    Calculates the euclidean distance between two points
    """
    return np.sqrt(np.sum(np.square(p1 - p2)))


def knn(X, Y, query_point, k):
    """
    Finds the k nearest neighbours of a query point
    """
    vals = []
    m = X.shape[0]
    for i in range(m):
        d = distance(query_point, X[i])
        vals.append((d, Y[i]))
    vals = sorted(vals)
    vals = vals[:k]
    vals = np.array(vals)
    new_vals = np.unique(vals[:, 1], return_counts=True)
    index = new_vals[1].argmax()
    pred = new_vals[0][index]
    return int(pred)
        


df = pd.read_csv('data.csv', encoding='utf-8', encoding_errors='ignore')  # Read the data file which is in csv format and store it in a dataframe


df.drop(['Response Id'], axis=1, inplace=True)  # Drop the Response Id column as it is not required
df.dropna(axis=1, inplace=True)  # Drop the columns with null values if any

personality_labels = {'ESTJ':0, 'ENTJ':1, 'ESFJ':2, 'ENFJ':3, 'ISTJ':4, 'ISFJ':5, 'INTJ':6, 'INFJ':7, 'ESTP':8,
                      'ESFP':9, 'ENTP':10, 'ENFP':11, 'ISTP':12, 'ISFP':13, 'INTP':14, 'INFP':15}  # Dictionary to map the personality types to integers

df.Personality = [personality_labels[item] for item in df.Personality]  # Map the personality types to integers

numpy_array = df.to_numpy()  # Convert the dataframe to a numpy array


test_set_size = 0.002 # Size of the test set (0.2% of the total data)
test_set_indices = rd.sample(range(0, len(df)), int(len(df) * test_set_size))  # Randomly select the indices of the test set

test_set = df.iloc[test_set_indices]  # Create the test set
train_set = df.drop(test_set_indices)  # Create the train set

test_set = test_set.to_numpy()  # Convert the test set to a numpy array
train_set = train_set.to_numpy()  # Convert the train set to a numpy array

X = train_set[:, :-1]  # Independent variables (Features)
Y = train_set[:, -1]  # Dependent variable (Personality (0-15))

predictions = []  # List to store the predictions of the model

# Predict the personality of the test set using the KNN model
for i in range(len(test_set)):
    pred = knn(X, Y, test_set[i, :-1], 5)
    predictions.append(pred)

true_labels = test_set[:, -1]  # True labels of the test set

accuracy = np.sum(predictions == true_labels) / len(true_labels)  # Calculate the accuracy of the model

print("Accuracy of the model: ", accuracy)