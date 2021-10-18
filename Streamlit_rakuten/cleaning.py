# -*- coding: utf-8 -*-
"""1_Cleaning_prep.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FdV82GHUgLRmlQ9o0FpkjNV60cRV_mjW
"""

import pandas as pd
import streamlit as st

import re  
import requests
import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk as nltk

def creerDataframePourArticleManuel(madescription, madesignation):
  dic={"designation":[madesignation],"description":[madescription],"productid":0,"imageid":None,"prdtypecode":None}
  X=pd.DataFrame(dic)
  return X

#CHARGEMENT des fichiers
def load_X(isManualDataFrame,madescription, madesignation):
  if (not isManualDataFrame):
    url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/Datasets/Dataset_challenge.csv"
    download = requests.get(url).content
    X=pd.read_csv(io.StringIO(download.decode('utf-8')), index_col=0)
  else:
    #OU création d'un dataframe
    X=creerDataframePourArticleManuel(madescription, madesignation)
  return X

def cleaningX_to_df(X):
  #PREPARATION: FUSION de X et y et remplacement des VALEURS MANQUANTES par ""
  df = X.drop(['imageid'], axis = 1)#
  #on joint X et y
  #df = pd.merge(df1, y, left_index=True, right_index=True)

  #valeurs MANQUANTES
  df['description']=df['description'].fillna("")
  df['designation']=df['designation'].fillna("")
  #turn all text to LOWER case
  df['description'] = df['description'].str.lower()
  df['designation'] = df['designation'].str.lower()

  #recodage des caractères HTML
  df.replace(["&eacute;","&egrave;","&euml;","&ecirc;","&ocirc;","&ugrave;","&ccedil;","&agrave;","&nbsp;","&amp;","&#39;","'",'n°']
            , ["é","è","ë","ê","ô","ù","ç","à"," ","&"," "," ",'numéro '], inplace=True, regex=True)

  """
  Return the text in lower case after removing html tags
  """    
  def pre_process(text):
      # lowercase
      #text=text.lower()
      #remove tags
      text=re.sub('<.*?>'," ",text) 
      return text

  df['description'] = df['description'].apply(lambda x:pre_process(x))
  df['designation'] = df['designation'].apply(lambda x:pre_process(x))
  return df

# Download the stopwords
@st.cache
def get_stopwords():
  #utiliser @st.cache !!! pour STREAMLIT
  nltk.download('punkt') #télécharge les paquets language (dont FR)
  nltk.download('stopwords')
  #Ajoute des stopwords à la liste française prédéfinie
  stop_words = set(stopwords.words('french'))
  stop_words.update(stopwords.words('english'))
  stop_words.update(stopwords.words('german'))
  stop_words.update(['-','de','en','pour','la','(',')','the','/li','/strong','strong','and','non','eacute','comme','cette','of'])
  return stop_words

#FONCTION pour supprimer les mots inutiles
def filtrer_mots_inutiles(texte,lststopwords):
  """
  Fonction pour transformer un texte en une suite de mots séparés par des espaces
  et en excluant les stopwords et les mots de moins de 2 caractères
  """
  mots = word_tokenize(texte, language='french')
  tokens = []
  for mot in mots:
    if (mot not in lststopwords and len(mot)>1):
      tokens.append(mot.lower())
  mastring=" ".join(tokens)
  return mastring

#3 ways to clean data

def clean_manualdata(madesignation, madescription):
  """
  input: madescription & madesignation are used
  """
  X=load_X(True, madescription, madesignation)
  df=cleaningX_to_df(X)
  stopwords=get_stopwords()
  df['designation']= df['designation'].apply(lambda x: filtrer_mots_inutiles(x, stopwords))
  df['description']= df['description'].apply(lambda x: filtrer_mots_inutiles(x, stopwords))
  return df

def clean_data():
  """
  load data from file and clean it
  """
  X=load_X(False, "", "")
  df=cleaningX_to_df(X)
  stopwords=get_stopwords()
  df['designation']= df['designation'].apply(lambda x: filtrer_mots_inutiles(x, stopwords))
  df['description']= df['description'].apply(lambda x: filtrer_mots_inutiles(x, stopwords))
  return df

def load_data_cleaned():
  """
  load dataset_challenge_cleaned.csv
  """
  df= pd.read_csv(f'{pathSaveCsv}/dataset_challenge_cleaned.csv')
  df['designation']=df['designation'].fillna("")
  #valeurs MANQUANTES
  df['description']=df['description'].fillna("")
  return df

#TEST function clean_manualdata()
#madescription="voici ma description d'article"
#madesignation="voici ma désignation d'article"
#df=clean_manualdata(madesignation,madescription)
#df

#TEST2 function clean_data()
#df=clean_data() #same can be done by df=pd.read_csv(f'{pathSaveCsv}/dataset_challenge_cleaned.csv')
#df
#if (isSaveData):
#  df.to_csv(f'{pathSaveCsv}/dataset_challenge_cleaned.csv')
