# -*- coding: utf-8 -*-
"""1_Cleaning_prep.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FdV82GHUgLRmlQ9o0FpkjNV60cRV_mjW
"""

#CONNEXION à google drive
import re  
import io
from nltk.tokenize import PunktSentenceTokenizer
import nltk as nltk
import PIL
from PIL import Image
import numpy as np
from utils import image_url_to_numpy_array_skimage

#DEBUT PREPROCESSING
isManualData=True
isRegenerateKeywords=False
#CHARGEMENT des 15 keyword par classe
import pickle

def load_keywords_fromfile():
  # reading the dictionnary des 15 keyword
  with open('./streamlit_rakuten/dico_keywords_tfidf_15.pkl', 'rb') as handle: 
    data = handle.read() 
  # reconstructing the data as dictionary 
  lst_keywords_byclass = pickle.loads(data) 
  return lst_keywords_byclass

lst_keywords_byclass = load_keywords_fromfile()

#la liste des keywords stockés par classe a été limitée à 10, faut il aller plus loin, performances?
"""
Fontion de scoring qui renvoie un score selon le nombre d'occurences des mots et leur score idf
texte: texte à lire mot à mot pour scorer les mots
dict_keywords_idf:dictionnaire des keywords/idf d'une des classes produits
"""
def scoring(texte, dict_keywords_idf):
#texte = texte de la désignaton/description de l'article
#dict_keywords_idf = [mot1 mot2 mot3 ...]
  #print(texte)
  #print(dict_keywords_idf)
  score = 0.0
  for keyword_key,keyword_idf in dict_keywords_idf.items():
    nb_occur = len(re.findall(keyword_key, texte, flags=re.IGNORECASE))
    score += nb_occur*keyword_idf
  #print(score)
  return score

def add_bestidf(df):
  col_start=7
  df["best_idf"]=df.iloc[:,col_start:].idxmax(axis=1)
  #df["best_idf"]= [2583 if (s.sum()==0) else df.iloc[:,col_start:].idxmax(axis=1) for s in df.iloc[:,1col_start1:]]
  #gestion des cas où toutes les colonnes valent 0
  #on affecte la classe 2583 (majoritaire)
  for i in range(len(df)):
    sum = df.iloc[i,col_start:].sum()
    if (sum == 0):
      df["best_idf"][i]="2583"
  return df

#Tokenisation (Séparation du texte en phrases et mots) du champ "designation"
def add_nb_phrases(df):
  #en phrases
  tokenizer = PunktSentenceTokenizer()
  df['desi_nb_phrases']= df['designation'].apply(lambda x: len(tokenizer.tokenize(str(x))))
  df['desc_nb_phrases']= df['description'].apply(lambda x: len(tokenizer.tokenize(str(x))))
  #en mots
  #df['desi_nb_mots+']= df['designation'].apply(lambda x: len(x.split(" "))
  #df['desc_nb_mots+']= df['description'].apply(lambda x: len(x.split(" "))
  return df

#Expressions régulières pour identifier les différentes unités
#TODO transformer en numérique pas en liste
def add_regex1(df):
  #nombre de nombres à 2 chiffres ou +
  r = re.compile("[0-9]{2,}") 
  df['desi_nb2chiffres+']= df['designation'].apply(lambda x: min(1,len(r.findall(x))))
  df['desc_nb2chiffres+']= df['description'].apply(lambda x: min(1,len(r.findall(x))))
  #XGo ou XMo ou XTo
  #r = re.compile("([\d.]+)\s?(go|mo|to|Go|Mo|To|giga|gigas)") 
  #df['desi_Go']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
  #df['desc_Go']=df['description'].apply(lambda x: min(1,len(r.findall(x))))
  #N°X
  r = re.compile("(numéro )") 
  df['desi_num']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
  df['desi_num']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
  #r = re.compile("[Nn][°]\s?[\d]+") 
  #df['desi_num']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
  #df['desc_num']=df['description'].apply(lambda x: min(1,len(r.findall(x))))
  #Poids kg Kg mg g
  r = re.compile("[0-9\.]+[kKm]?[g]") #([\d.]+)\s+(lbs?|oz|g|kg) 
  r = re.compile("([\d.]+)\s?(KG|Kg|g|kg|mg)[\s.]") #(nombres ou .)+ / (espace)+ / (kg mg ..)
  df['desi_poids']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
  df['desc_poids']=df['description'].apply(lambda x: min(1,len(r.findall(x))))
  #Taille cm mm m
  r = re.compile("([\d.]+)\s?(cm|mm|m|M)[\s.]") 
  df['desi_long']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
  df['desc_long']=df['description'].apply(lambda x: min(1,len(r.findall(x))))
  #Volume mL cL dL
  r = re.compile("([\d.]+)\s?(mL|L|ml|l|cl)[\s.]") 
  df['desi_vol']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
  df['desc_vol']=df['description'].apply(lambda x: min(1,len(r.findall(x))))
  #Age
  r = re.compile("([\d.]+)\s?(an|ans|An|Ans|mois|Mois)[\s.]") 
  df['desi_ans_mois']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
  df['desc_ans_mois']=df['description'].apply(lambda x: min(1,len(r.findall(x))))
  #Pièces
  r = re.compile("([\d.]+)\s?(pc|pcs|pièces|pièce)[\s.]") 
  df['desi_pieces']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
  df['desc_pieces']=df['description'].apply(lambda x: min(1,len(r.findall(x))))
  #%
  #r = re.compile("([\d.]+)\s?%") 
  #df['desi_pourcent']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
  #df['desc_pourcent']=df['description'].apply(lambda x: min(1,len(r.findall(x))))
  return df

def add_regex2(df) :
    df['desi_word_count'] = df['designation'].apply(lambda x : len(str(x).split()))
    df['desi_char_count (w/o space)'] = df['designation'].apply(lambda x : len(x.replace(" ","")))
    #df['desi_word_density'] = df['desi_word_count'] / (df['desi_char_count'] + 1)
    df['desi_total_length'] = df['designation'].apply(len)
    #df['desi_capitals'] = df['designation'].apply(lambda comment: sum(1 for c in comment if c.isupper()))
    # df['desi_caps_vs_length'] = df.apply(lambda row: float(row['desi_capitals'])/float(row['desi_total_length']),axis=1)
    df['desi_num_exclamation_marks'] =df['designation'].apply(lambda x: x.count('!'))
    df['desi_num_question_marks'] = df['designation'].apply(lambda x: x.count('?'))
    #df['desi_num_punctuation'] = df['designation'].apply(lambda x: sum(x.count(w) for w in '.,;:'))
    #df['desi_num_symbols'] = df['designation'].apply(lambda x: sum(str(x).count(w) for w in '*&$%+-/'))
    df['desi_num_unique_words'] = df['designation'].apply(lambda x: len(set(w for w in x.split())))
    df['desi_words_vs_unique'] = df['desi_num_unique_words'] / df['desi_word_count']
    df["desi_word_unique_percent"] =  df["desi_num_unique_words"]*100/df['desi_word_count']
    
    df['descri_word_count'] = df['description'].apply(lambda x : len(str(x).split()))
    df['descri_char_count (w/o space)'] = df['description'].apply(lambda x : len(str(x).replace(" ","")))
    #df['descri_word_density'] = df['descri_word_count'] / (df['descri_char_count'] + 1)
    df['descri_total_length'] = df['description'].apply(lambda x :len(str(x)))
   # df['descri_capitals'] = df['description'].apply(lambda comment: sum(1 for c in str(comment) if c.isupper()))
    # df['descri_caps_vs_length'] = df.apply(lambda row: float(row['descri_capitals'])/float(row['descri_total_length']),axis=1)
    df['descri_num_exclamation_marks'] =df['description'].apply(lambda x: str(x).count('!'))
    df['descri_num_question_marks'] = df['description'].apply(lambda x: str(x).count('?'))
    #df['descri_num_punctuation'] = df['description'].apply(lambda x: sum(str(x).count(w) for w in '.,;:'))
   # df['descri_num_symbols'] = df['description'].apply(lambda x: sum(str(x).count(w) for w in '*&$%'))
    df['descri_num_unique_words'] = df['description'].apply(lambda x: len(set(w for w in str(x).split())))
    df['descri_words_vs_unique'] = df['descri_num_unique_words'] / df['descri_word_count']
    df["descri_word_unique_percent"] =  df["descri_num_unique_words"]*100/df['descri_word_count']
    return df

def create_features_loadedd(df):
  df=add_nb_phrases(df)
  df["best_idf"]=0
  #lst_keywords_byclass contient: {1180:[mot1 mot2 mot3 ...], 2520:[mot1 mot2 mot3 ...] ...}
  #lst_keywords_byclass = sorted(lst_keywords_byclass)
  for (key_kw, value_kw) in sorted(lst_keywords_byclass.items()):
    #key_kw=1180
    #value_kw=[mot1 mot2 mot3 ...]
    df['class_'+str(key_kw)]=df['designation'].apply(lambda x: scoring(x, value_kw))
  df=add_bestidf(df)
  df=add_regex1(df)
  df=add_regex2(df)
  return df
'''  
#TEST   create_features_loadeddf
isManualData=False
if (not isManualData):
  url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/Datasets/dataset_challenge_cleaned.csv"
  download = requests.get(url).content
  df = pd.read_csv(io.StringIO(download.decode('utf-8')), index_col=0)
  df=df.drop("Unnamed: 0.1", axis=1)
  df['designation']=df['designation'].fillna("")
  #valeurs MANQUANTES
  df['description']=df['description'].fillna("")
  create_features_loadedd(df)
'''

def add_imgfeatures(df, imgpath):
    if (not (imgpath == "")):
        if (imgpath.startswith("http")):
            image=image_url_to_numpy_array_skimage(imgpath)
        else:
            image = np.array(Image.open(imgpath))
        n_white_pix = np.sum(image == [255, 255, 255])/750000
        n_black_pix = np.sum(image == [0,0,0])/750000
        image_mean = np.mean(image, axis=(0, 1))  
        df['blanc']=n_white_pix
        df['noir']=n_black_pix
        #print("image_mean:",image_mean)
        df['R']= image_mean[0]
        df['G']= image_mean[1]
        df['B']= image_mean[2]
    else:
        df['blanc']=0
        df['noir']=0
        df['R']= 0
        df['G']= 0
        df['B']= 0
    return df
    
def add_features_to_manualdf(df, imgpath):
  df=add_nb_phrases(df)
  df["best_idf"]=0
  #lst_keywords_byclass contient: {1180:[mot1 mot2 mot3 ...], 2520:[mot1 mot2 mot3 ...] ...}
  #lst_keywords_byclass = sorted(lst_keywords_byclass)
  for (key_kw, value_kw) in sorted(lst_keywords_byclass.items()):
    #key_kw=1180
    #value_kw=[mot1 mot2 mot3 ...]
    df['class_'+str(key_kw)]=df['designation'].apply(lambda x: scoring(x, value_kw))
  df=add_bestidf(df)
  df=add_regex1(df)
  df=add_regex2(df)
  df=add_imgfeatures(df, imgpath)
  return df
'''
#TEST  add_features_to_manualdf
isManualData=True
if (isManualData):
  madescription=""
  madesignation="guerre tuques"
  df=clean_manualdata(madesignation, madescription)
  add_features_to_manualdf(df)

df.head()

df.to_csv(f'{pathSaveCsv}/features_texte.csv')
'''