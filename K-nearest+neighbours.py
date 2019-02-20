
# coding: utf-8


import pandas as pd
import os
from matplotlib import pyplot as plt
from sklearn import datasets
import numpy as npy
import urllib.request
import csv
import io
import seaborn as sns
# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier


# using the cogress data to fit a k-Nearest Neighbors classifier to the voting dataset
url = "https://assets.datacamp.com/production/course_6078/datasets/house-votes-84.csv"
webpage = urllib.request.urlopen(url)
datareader = csv.reader(webpage.read().decode('utf-8').splitlines())


# printing it
data = []
for row in datareader:
    data.append(row)

for row in data:
    print(row)
    
# converting the list to pandas dataframe
data = pd.DataFrame(data)


type(data)
# renaming column indexes 
data.columns = ['party', 'infants', 'water', 'budget', 'physician', 'salvador',
       'religious', 'satellite', 'aid', 'missile', 'immigration', 'synfuels',
       'education', 'superfund', 'crime', 'duty_free_exports', 'eaa_rsa']


data.shape

data = data.applymap(lambda x: 1 if x == "y" else x)
data = data.applymap(lambda x: 0 if x == "n" else x)
data = data.applymap(lambda x: 0 if x == "?" else x)

data.info()


# Scikit-learn API requires that the features need to be in an array where each column is a feature 
# and each row a different observation or data point - in this case, a Congressman's voting record. 
# The target needs to be a single column with the same number of observations as the feature data. 
# HEre we name the feature array X and response variable y: This is in accordance with the common scikit-learn practice.
# Creating arrays for the features and the response variable:
y = data['party'].values
X = data.drop('party', axis=1).values
# Use of the .values attribute to ensure X and y are NumPy arrays 
# Without using .values, X and y are a DataFrame and Series respectively


# Creating a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors=6)

# Fitting the classifier to the data
knn.fit(X, y)


# Predicting the labels for the training data X: y_pred
# this is already seen data obv
y_pred = knn.predict(X)
print("Prediction: {}".format(y_pred)) 


X_new = [0.460824, 0.04546, 0.133819, 0.783906, 0.46796, 0.779067, 0.848285, 0.473114,  0.949498, 0.721726,  
         0.301748, 0.619569,  0.076781, 0.427347, 0.637339,  0.595389]


df_new = pd.DataFrame([X_new])


new_prediction = knn.predict(df_new)
print("Prediction: {}".format(new_prediction)) 




