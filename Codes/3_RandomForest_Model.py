# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:19:44 2021

@author: Lenovo
"""

import pandas as pd
from google.colab import drive
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import requests
import io
from sklearn.ensemble import VotingClassifier, StackingClassifier
from sklearn.model_selection import train_test_split, cross_validate, KFold
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler

drive.mount('/Drive')


# Downloading the csv file from your GitHub account

url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/Features/data_features_final.csv" # Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe

df = pd.read_csv(io.StringIO(download.decode('utf-8')))

#Drop useless columns
df = df.drop(["Unnamed: 0.1","Unnamed: 0","imageid", "prdtypecode.1","productid","designation","description", "best_idf"], axis=1)

#Create "class" columns with the copy of 'prdtypecode'
df['class'] = df['prdtypecode']
#Drop column related to product type codification
df = df.drop('prdtypecode', axis=1)

# ​Replace Rakuten product type codification with corresponding class between 0 to 26.
df = df.replace({'class': {10: 1, 2280:2,   50:3, 1280:4, 2705:5, 2522:6, 2582:7, 1560:8, 1281:9, 1920:10, 2403:11,
       1140:12, 2583:13, 1180:14, 1300:15, 2462:16, 1160:17, 2060:18,   40:19,   60:20, 1320:21, 1302:22,
       2220:23, 2905:24, 2585:25, 1940:26, 1301:0}})
#Create target df
target = df['class']
#Create features df
features = df.drop(['class'], axis=1)

#Prepare training and test data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size = 0.2, random_state = 123)


#Standard Scaler creation based on X_train
scaler = StandardScaler().fit(X_train)

#X_train and X_test scaling
X_train  = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#Random Forest Classifier creation
clf1 = RandomForestClassifier(max_features ='sqrt', n_jobs = -1,n_estimators = 500)
clf1.fit(X_train, y_train)

y_pred = clf1.predict(X_test)
dfcross=pd.crosstab(y_test.ravel(), y_pred, rownames=['Realité'], colnames=['Prédiction'], normalize=1)


classif = classification_report(y_test, y_pred)














































