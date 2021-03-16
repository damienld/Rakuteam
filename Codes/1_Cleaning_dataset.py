# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:21:09 2021

@author: Rakuteam
"""

#CONNEXION à google drive TODO: adapter à environnement GIThub Streamlit
import pandas as pd
from google.colab import drive

drive.mount('/Drive')

#CHARGEMENT des fichiers
X = pd.read_csv("/Drive/My Drive/Colab/X_train_update.csv", index_col=0) 
#X_train_update.info()
y = pd.read_csv("/Drive/My Drive/Colab/Y_train_CVw08PX.csv", index_col=0) 

#Création d'un liste contenant tous les codes de classe
classes_codes = (y['prdtypecode'].value_counts().index.tolist())


#Suppression colone 'imageid'
df1 = X.drop(['imageid'], axis = 1)

#on joint X et y TODO: à garder? Utile uniquement pour la Dataviz
df = pd.merge(df1, y, left_index=True, right_index=True)

#Traitement des valeurs manquantes (remplacées par " ")
df['designation']=df['designation'].fillna("")
df['description']=df['description'].fillna("")

#Passer tous le texte en minuscule
df['description'] = df['description'].str.lower()
df['designation'] = df['designation'].str.lower()

#Recodage des caractères HTML
df.replace(["&eacute;","&egrave;","&euml;","&ecirc;","&ocirc;","&ugrave;","&ccedil;","&agrave;","&nbsp;","&amp;","&#39;"]
           , ["é","è","ë","ê","ô","ù","ç","à"," ","&","'"], inplace=True, regex=True)


"""
Return the text in lower case after removing html tags
"""   
import re 
 
def pre_process(text):
    # lowercase
    #text=text.lower()
    #remove tags
    text=re.sub('<.*?>'," ",text) #COMMENTAIRE: retrait des caracère trop tôt (nécéssaire pour création de features)
    return text

df['description'] = df['description'].apply(lambda x:pre_process(x))
df['designation'] = df['designation'].apply(lambda x:pre_process(x))


#FONCTION pour supprimer les mots inutiles
# Download the stopwords
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk as nltk
nltk.download('punkt') #télécharge les paquets language (dont FR)
nltk.download('stopwords')

#Ajoute des stopwords à la liste française prédéfinie
stop_words = set(stopwords.words('french'))
stop_words.update(stopwords.words('english'))
stop_words.update(stopwords.words('german'))
stop_words.update(['-','de','en','pour','la','(',')','the','/li','/strong','strong','and','non','eacute','comme','cette','of'])





def filtrer_mots_inutiles(texte):
  """
  Fonction pour transformer un texte en une suite de mots séparés par des espaces
  et en excluant les stopwords et les mots de moins de 2 caractères
  """
  mots = word_tokenize(texte, language='french')
  tokens = []
  for mot in mots:
    if (mot not in stop_words and len(mot)>1):
      tokens.append(mot.lower())
  return tokens

df['designation']= df['designation'].apply(lambda x: filtrer_mots_inutiles(x))
df['description']= df['description'].apply(lambda x: filtrer_mots_inutiles(x))

#Création d'un fichier CSV sur Google Drive
path = '/Drive/My Drive/Projet Rakuten'
df.to_csv(f'{path}/dataset_cleaned.csv')

