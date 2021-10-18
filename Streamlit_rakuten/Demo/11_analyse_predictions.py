# -*- coding: utf-8 -*-
"""11_Analyse_predictions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NxL1MeiSuDQjd2evwxilYrSCJtYCEOVC

<a href="https://colab.research.google.com/github/JulienJ-44/rakuteam/blob/main/11_bis_Vote_3_mod%C3%A8les_ypred_proba_text_0_82_img_0_55.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
"""

# Connection au google drive 
from google.colab import drive
drive.mount('/Drive')
pathSaveCsv = '/Drive/My Drive'

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

def display_keywords(name_classe_reelle, name_classe_predite):
  dataf_code_designation=load_df_code_designation
  classe_predite_code026=dataf_code_designation[dataf_code_designation["désignation"]==name_classe_reelle].code_0a26
  classe_reelle_code026=(dataf_code_designation[dataf_code_designation["désignation"]==name_classe_predite]).code_0a26
  classe_predite_code=dataf_code_designation[dataf_code_designation["désignation"]==name_classe_reelle].prdtypecode
  classe_reelle_code=(dataf_code_designation[dataf_code_designation["désignation"]==name_classe_predite]).prdtypecode

  import pickle
  import constants
  
  # reading the dictionnary des 15 keyword
  with open(constants.path+f'{pathSaveCsv}/dico_keywords_tfidf_15.pkl', 'rb') as handle: 
    data = handle.read() 
  # reconstructing the data as dictionary 
  lst_keywords_byclass = pickle.loads(data) 

  print("Classe:",classe_reelle_code, " ", classe_reelle_code026)
  print(lst_keywords_byclass[int(classe_reelle_code)])
  print("Classe:",classe_predite_code, " ", classe_predite_code026)
  print(lst_keywords_byclass[int(classe_predite_code)])
  #df_comparekeywords[classe_reelle_code]=lst_keywords_byclass[int(classe_reelle_code)]
  df_comparekeywords=pd.DataFrame(index=np.arange(15))
  df_comparekeywords[classe_reelle_code]=[key for key in lst_keywords_byclass[int(classe_reelle_code)]]
  df_comparekeywords[classe_reelle_code+"_"]=[lst_keywords_byclass[key] for key in lst_keywords_byclass[int(classe_reelle_code)]]
  df_comparekeywords[classe_predite_code]=[key for key in lst_keywords_byclass[int(classe_predite_code)]]
  df_comparekeywords[classe_predite_code+"_"]=[lst_keywords_byclass[key] for key in lst_keywords_byclass[int(classe_predite_code)]]
  print(df_comparekeywords.head(15))

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

def get_classifreport_crosstab(index_model):
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

print("Evaluation détaillée de la Classification :\n \n" , get_classif_report("4"))

def get_crosstab(index_model):
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
  # Crosstab avec ravel pr enlever dimension et eviter message d'erreur (Error: If using all scalar values, you must pass an index)
  dfcross = pd.crosstab(y_test.ravel(), y_pred.ravel(), rownames=['Classe réelle'], colnames=['Classe prédite'],normalize = 0) #TODO remettre ,normalize = 0  
  dfcross = dfcross.sort_index(axis=0)
  dfcross = dfcross.sort_index(axis=1)
  dfcross.columns = df_code_designation['désignation']
  dfcross.index = df_code_designation['désignation']
  return dfcross

import seaborn as sns
cross=get_crosstab("3")
print("Heatmap:")
plt.figure(figsize=(25,25))
g = sns.heatmap(cross,  annot=True, cmap="YlGnBu");
plt.xticks(rotation=90);

#chargement de ytest et des features pour récuérer l'échantillon d articles tests utilisé pour les modèles
url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/y_pred_proba/y_test.csv"# Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content
y_test_analyse = pd.read_csv(io.StringIO(download.decode('utf-8')), index_col=0)

url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/Features/data_features_final.csv"# Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content
data_features = pd.read_csv(io.StringIO(download.decode('utf-8')))
#on garde que les données avec label (on exclut la partie X_test challenge)
data_features = data_features.dropna(subset=['prdtypecode_x'])

# Drop le Unnamed
try:
    data_features = data_features.drop('Unnamed: 0', axis =1)
except:
  print("(1)no columns Unnamed: 0")
try:
    data_features = data_features.drop('prdtypecode_y', axis =1)
except:
  print("(1)no columns prdtypecode_y")

# on regénère les mêmes échantillons que pour les modèles
X_train, X_test, y_train, y_test = train_test_split(data_features, data_features['prdtypecode_x'], test_size = 0.2, random_state = 123)
y_test_analyse['prédiction'] = y_pred
X_test=X_test.sort_index(axis=0)
#y_test_analyse=y_test_analyse.sort_index(axis=0)
#y_pred=y_pred.sort(axis=0)
y_test_analyse = y_test_analyse.replace({'prdtypecode': {10: 1, 2280:2,   50:3, 1280:4, 2705:5, 2522:6, 2582:7, 1560:8, 1281:9, 1920:10, 2403:11,
       1140:12, 2583:13, 1180:14, 1300:15, 2462:16, 1160:17, 2060:18,   40:19,   60:20, 1320:21, 1302:22,
       2220:23, 2905:24, 2585:25, 1940:26, 1301:0}})

Global_df_analysis = pd.concat([X_test.drop("prdtypecode_x", axis=1),y_test_analyse], axis = 1)
ligne_erreur = Global_df_analysis[Global_df_analysis['prdtypecode']!=Global_df_analysis['prédiction']]
ligne_erreur.info()
#Quasiment 50% des erreurs de classfication correspondent à des articles à description vide! => amléiorer features RF sur designations

#dfcross_notnorm = pd.crosstab(y_test.ravel(), y_pred.ravel(), rownames=['Classe réelle'], colnames=['Classe prédite']) #TODO remettre ,normalize = 0
dfcross_notnorm = pd.crosstab(y_test_analyse.prdtypecode, y_test_analyse.prédiction, rownames=['Classe réelle'], colnames=['Classe prédite']) #TODO remettre ,normalize = 0
dfcross_notnorm = dfcross_notnorm.sort_index(axis=0)
dfcross_notnorm = dfcross_notnorm.sort_index(axis=1)
dfcross_notnorm.columns = df_code_designation['désignation']
dfcross_notnorm.index = df_code_designation['désignation']
dfcross_notnorm

cm = dfcross_notnorm
df = pd.DataFrame()

i=0
j=0
ClassVrai = []
ClassPredite = []
Erreurs = []
for i in range(len(cm)):
    for j in range(len(cm.columns)):
        if i != j:
            #if cm.iloc[i,j] > 0.05:
                ClassVrai.append(cm.index[i])
                ClassPredite.append(cm.columns[j])
                Erreurs.append(cm.iloc[i,j])
        
df = pd.DataFrame({'Classe réelle' : ClassVrai,
                    'Classe prédite' : ClassPredite,
                    '#Erreurs' : Erreurs
                    })

df=df.sort_values(by='#Erreurs',ascending=False)
df.head(10)
#df_sorted[df_sorted['Classe réelle']=='FIGURINES MANGAS']

#df_code_designation
print("\nErreur %:", df.iloc[indexrow,2])
display_prediction_errors(df.iloc[indexrow,0], df.iloc[indexrow,1])
print("\nExemples d'articles avec cette erreur de classification:")
ligne_erreur_1 = ligne_erreur[((ligne_erreur.prdtypecode==int(classe_reelle_code026)) & (ligne_erreur.prédiction==int(classe_predite_code026)))]
ligne_erreur_1.head(10)

df.groupby('Classe réelle').sum().sort_values(by='#Erreurs',ascending=False)

df.groupby('Classe prédite').sum().sort_values(by='#Erreurs',ascending=False)

dfcross_norm = pd.crosstab(y_test_analyse.prdtypecode, y_test_analyse.prédiction, rownames=['Classe réelle'], colnames=['Classe prédite'],normalize = 0) #TODO remettre ,normalize = 0
dfcross_norm = dfcross_norm.sort_index(axis=0)
dfcross_norm = dfcross_norm.sort_index(axis=1)
dfcross_norm.columns = df_code_designation['désignation']
dfcross_norm.index = df_code_designation['désignation']
dfcross_norm

cm = dfcross_norm
df = pd.DataFrame()

i=0
j=0
ClassVrai = []
ClassPredite = []
Erreurs = []
for i in range(len(cm)):
    for j in range(len(cm.columns)):
        if i != j:
            #if cm.iloc[i,j] > 0.05:
                ClassVrai.append(cm.index[i])
                ClassPredite.append(cm.columns[j])
                Erreurs.append(cm.iloc[i,j]*100)
        
df = pd.DataFrame({'Classe réelle' : ClassVrai,
                    'Classe prédite' : ClassPredite,
                    '#Erreurs %' : Erreurs
                    })         
df=df.sort_values(by='#Erreurs %',ascending=False)
df.head(10)
#df_sorted[df_sorted['Classe réelle']=='FIGURINES MANGAS']

indexrow=0 #select which row of dataframe above you want to investigate
classe_reelle_code=df_code_designation[df_code_designation["désignation"]==df.iloc[indexrow,0]]["prdtypecode"]
classe_predite_code=df_code_designation[df_code_designation["désignation"]==df.iloc[indexrow,1]]["prdtypecode"]



df.groupby('Classe prédite').sum().sort_values(by='#Erreurs %',ascending=False)

df.groupby('Classe réelle').sum().sort_values(by='#Erreurs %',ascending=False)

