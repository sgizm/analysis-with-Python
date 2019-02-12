
# coding: utf-8

# In[4]:

import pandas as pd
import os


# In[8]:

os.chdir("/Users/Desktop/Python")
pwd()


# Reading the file, checking the data
df = pd.read_csv("clus_data.csv")
df.info()
df.head()
df.tail()

print(df.info())


jobtime = df.JOBTIME
print(jobtime)
jobother = df["JOBFUNCOTHER"]
print(jobother)

# Operations on job functions and job times

df[jobtime < 1000]
df[COMPANY=='E*']

df.COMPANY

# selecting rows
df[df.COMPANY=='R*']
df[df.JOBFUNCOTHER != "data science"]
df[df["COMPANY"] != "R*"]



