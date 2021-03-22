# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:27:06 2021

@author: slam_
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np

from sklearn import preprocessing
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
import requests
import io

model_index = 1#input("Select a model: 1-RF, 2-CNN image, 3-DNN texte, default-weighted voting")
print(model_index)

def load_df_code_designation():
  url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/Demo/df_classes_avec_code_libelle_code026.csv"
  download = requests.get(url).content
  df = pd.read_csv(io.StringIO(download.decode('utf-8')), index_col=0)
  return df

df_code_designation = load_df_code_designation()



def get_ytest():
  url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/y_pred_proba/y_test.csv"# Make sure the url is the raw version of the file on GitHub
  download = requests.get(url).content
  y_test = pd.read_csv(io.StringIO(download.decode('utf-8')))
  # Remplacer les labels de 0 à 26
  y_test = y_test.replace({'prdtypecode': {10: 1, 2280:2,   50:3, 1280:4, 2705:5, 2522:6, 2582:7, 1560:8, 1281:9, 1920:10, 2403:11,
        1140:12, 2583:13, 1180:14, 1300:15, 2462:16, 1160:17, 2060:18,   40:19,   60:20, 1320:21, 1302:22,
        2220:23, 2905:24, 2585:25, 1940:26, 1301:0}})
  try:
    y_test = y_test.drop('Unnamed: 0', axis =1)
  except:
    print("(2)no columns Unnamed: 0")
  return y_test

def get_ytrain():
  url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/y_pred_proba/y_train.csv"# Make sure the url is the raw version of the file on GitHub
  download = requests.get(url).content
  y_train = pd.read_csv(io.StringIO(download.decode('utf-8')))
  # Remplacer les labels de 0 à 26
  return y_train

def set_model_name(model_index):
  if (model_index == "1"):
    model_selected="Random Forest"
    
  elif (model_index == "2"):
    model_selected="CNN images"
    
  elif (model_index == "3"):
    model_selected="DNN texte"
    
  else:
    model_selected="weighted voting"
  return model_selected

def calc_y_pred(model_index):
  if (model_index == "1"):
    url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/y_pred_proba/ypred_proba_RandomForest_Global_score0_74.csv"
    download = requests.get(url).content
    y_pred_proba= pd.read_csv(io.StringIO(download.decode('utf-8')))
  elif (model_index == "2"):
    url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/y_pred_proba/ypred_proba_Image_score_0_55_correct.csv"
    download = requests.get(url).content
    y_pred_proba= pd.read_csv(io.StringIO(download.decode('utf-8')))
  elif (model_index == "3"):
    url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/y_pred_proba/ypred_proba_DnnText_score0_82.csv"
    download = requests.get(url).content
    y_pred_proba= pd.read_csv(io.StringIO(download.decode('utf-8')))
  else:
    url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/y_pred_proba/ypred_proba_RandomForest_Global_score0_74.csv" # Make sure the url is the raw version of the file on GitHub
    download = requests.get(url).content
    y_pred_proba_rf = pd.read_csv(io.StringIO(download.decode('utf-8')))
    url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/y_pred_proba/ypred_proba_DnnText_score0_82.csv" # Make sure the url is the raw version of the file on GitHub
    download = requests.get(url).content
    y_pred_proba_dnntext = pd.read_csv(io.StringIO(download.decode('utf-8')))
    url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/y_pred_proba/ypred_proba_Image_score_0_55_correct.csv"# Make sure the url is the raw version of the file on GitHub
    download = requests.get(url).content
    y_pred_proba_img = pd.read_csv(io.StringIO(download.decode('utf-8')))
    score1_rf = 0.74
    score2_dnntext = 0.82
    score3_img = 0.58
    y_pred_proba = (score1_rf * y_pred_proba_rf + score2_dnntext * y_pred_proba_dnntext + score3_img * y_pred_proba_img) / (score1_rf + score2_dnntext + score3_img)
  # Drop les colonnes inutiles
  try:
      y_pred_proba = y_pred_proba.drop('Unnamed: 0', axis =1)
  except:
    print("(1)no columns Unnamed: 0")
  return y_pred_proba

from sklearn.metrics import accuracy_score
from sklearn import metrics

def get_classif_report(index_model):
  model_index=index_model
  y_test=get_ytest()
  y_train=get_ytrain()
  model_selected=set_model_name(index_model)
  y_pred_proba=calc_y_pred(index_model)
  #preparation des données pour le crosstab
  # Convertir Dataframe en array
  y_pred_proba_arr = y_pred_proba.to_numpy()
  y_test = y_test.to_numpy()
  # on prend l'index de la proba la + élevée
  # pour récupérer les classes
  y_pred = y_pred_proba_arr.argmax(axis=1)
  y_pred
  # Pour ajouter une dimension en plus
  y_pred = np.reshape(y_pred, (-1, 1))
  return(metrics.classification_report(y_test, y_pred))
print("Evaluation détaillée de la Classification :\n \n" , get_classif_report("3"))

# y_test = y_test.replace({'prdtypecode': {10: 1, 2280:2,   50:3, 1280:4, 2705:5, 2522:6, 2582:7, 1560:8, 1281:9, 1920:10, 2403:11,
#        1140:12, 2583:13, 1180:14, 1300:15, 2462:16, 1160:17, 2060:18,   40:19,   60:20, 1320:21, 1302:22,
#        2220:23, 2905:24, 2585:25, 1940:26, 1301:0}})

# Crosstab avec ravel pr enlever dimension et eviter message d'erreur (Error: If using all scalar values, you must pass an index)
dfcross = pd.crosstab(y_test.ravel(), y_pred.ravel(), rownames=['Classe réelle'], colnames=['Classe prédite'],normalize = 0) #TODO remettre ,normalize = 0
dfcross = dfcross.sort_index(axis=0)
dfcross = dfcross.sort_index(axis=1)
dfcross.columns = df_code_designation['désignation']
dfcross.index = df_code_designation['désignation']

import seaborn as sns
# Matrice de confusion
plt.figure(figsize=(25,25))
g = sns.heatmap(dfcross,  annot=True, cmap="YlGnBu");
plt.xticks(rotation=90);
