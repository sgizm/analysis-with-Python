
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

plt.style.use('ggplot')


# first let's practise with the iris data
iris = datasets.load_iris()
type(iris)


# we see that bunch is like a dictionary, involving key of pairs 
print(iris.keys())

type(iris.data)


# remember, samples are rows, features are columns
iris.data.shape

iris.target_names


# another dataset, getting online
url = "https://assets.datacamp.com/production/course_6078/datasets/house-votes-84.csv"
webpage = urllib.request.urlopen(url)
datareader = csv.reader(webpage.read().decode('utf-8').splitlines())


# printing it
data = []
for row in datareader:
    data.append(row)

for row in data:
    print(row)


type(data)

# converting the list to pandas dataframe
data = pd.DataFrame(data)


type(data)

# renaming column indexes 
data.columns = ['party', 'infants', 'water', 'budget', 'physician', 'salvador',
       'religious', 'satellite', 'aid', 'missile', 'immigration', 'synfuels',
       'education', 'superfund', 'crime', 'duty_free_exports', 'eaa_rsa']


data.head()


# replacing yes/no's with 1/O's and also replacing NA's with 0's
data = data.applymap(lambda x: 1 if x == "y" else x)
data = data.applymap(lambda x: 0 if x == "n" else x)
data = data.applymap(lambda x: 0 if x == "?" else x)


#data = data.eq(1).astype(int)
data.info()


# let's explore the data with some plots 
# for the education bill
plt.figure()
sns.countplot(x='education', hue='party', data=data, palette='RdBu')
plt.xticks([0,1], ['No', 'Yes'])
plt.show()


# for the satellite bill
plt.figure()
sns.countplot(x='satellite', hue='party', data=data, palette='RdBu')
plt.xticks([0,1], ['No', 'Yes'])
plt.show()


# for the missile bill
plt.figure()
sns.countplot(x='missile', hue='party', data=data, palette='RdBu')
plt.xticks([0,1], ['No', 'Yes'])
plt.show()




