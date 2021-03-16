# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:30:57 2021

@author: Rakuteam
"""

#CONNEXION à google drive
import pandas as pd
from google.colab import drive

drive.mount('/Drive')

#Chargement fichier CSV enregistré à la fin de la phase de cleaning (1_Cleaning_data_set)
path = '/Drive/My Drive/Projet Rakuten'
df=pd.read_csv(f'{path}/dataset_cleaned.csv')
df['designation']=df['designation'].fillna("")
#valeurs MANQUANTES
df['description']=df['description'].fillna("")


###TODO lemmatisation


#Tokenisation (Séparation du texte en phrases et mots) des champs "designation" & "description"
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import word_tokenize
import nltk as nltk
nltk.download('punkt') #télécharge les paquets language (dont FR)

#Décompte du nombre de phrases
tokenizer = PunktSentenceTokenizer()
df['desi_nb_phrases']= df['designation'].apply(lambda x: len(tokenizer.tokenize(str(x))))
df['desc_nb_phrases']= df['description'].apply(lambda x: len(tokenizer.tokenize(str(x))))
#en mots
#df['desi_nb_mots+']= df['designation'].apply(lambda x: len(x.split(" "))
#df['desc_nb_mots+']= df['description'].apply(lambda x: len(x.split(" "))


#IDF ("inverse de fréquence de document")
#formule: log(nbr d articles / nb d articles dans lequels le terme apparaît)
from sklearn.feature_extraction.text import TfidfVectorizer
#transformation de la colonne en type liste
words_desi=df['designation'].tolist()
#words_desc=df['description'].tolist()

# create object 
vect  = TfidfVectorizer()  
# get tf-df values 
result = vect.fit_transform(words_desi) 
# get idf values 
#sorted_vocabulary = dict(sorted(vect.vocabulary_.items(), key=lambda item: item[0], reverse=True))
print(vect.vocabulary_)
print(vect.get_feature_names())
print(vect.idf_)

#fonctions de manipulation des TFIDF
def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

def extract_topn_from_vector(feature_names, sorted_items, topn=10):
    """Obtenir le score tf-idf des n premiers élements extraits de features (feature_names)"""
    
    #use only topn items from vector
    sorted_items = sorted_items[:topn]

    score_vals = []
    feature_vals = []
    
    # word index and corresponding tf-idf score
    for idx, score in sorted_items:
        
        #keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    #create a tuples of feature,score
    #results = zip(feature_vals,score_vals)
    results= {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]]=score_vals[idx]
    
    return results

#TF fréquence du terme dans l ensbl de la categorie d articles
feature_names=vect.get_feature_names()
#on étudie le champ designation ( à remplacer par "description" si besoin)
colonneClass = "designation" 
class_text_cols = []
#on parcourt la liste des codes de classes
lst_keywords_byclass={}
classes_codes = (df['prdtypecode'].value_counts().index.tolist())
#classes_codes=[2583, 1220, 22240, ...]
for class_code in classes_codes:
  #on copie dans un df les lignes correspondant au code de classe actuel
  df_class = df[df["prdtypecode"]==class_code]
  #on joint tous les élements de la colonne dans une chaîne
  class_text = ' '.join(df_class[colonneClass])
  #affichage des infos de la classe
  print("Classe:", class_code, "\n", len(df_class.index), " éléments")
  #tfidf
  class_text_encode = vect.transform([class_text])

  
  #sort the tf-idf vectors by descending order of scores
  sorted_items=sort_coo(class_text_encode.tocoo())
  #extract only the top n; n here is 10
  keywords=extract_topn_from_vector(feature_names,sorted_items,15)
  # now print the results
  print("===Keywords===")
  for k in keywords:
      print(k,keywords[k])
  lst_keywords_byclass[class_code]=keywords
  print("\n")

#lst_keywords_byclass contient: {1180:[mot1 mot2 mot3 ...], 2520:[mot1 mot2 mot3 ...] ...}

#TEMP df_sample!!!
#df_sample=df.head(1000) #TEMP!!!!
#la liste des keywords stockés par classe a été limitée à 10, faut il aller plus loin, performances?
"""
Fontion de scoring qui renvoie un score selon le nombre d'occurences des mots et leur score idf
texte: texte à lire mot à mot pour scorer les mots
dict_keywords_idf:dictionnaire des keywords/idf d'une des classes produits
"""
import re
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

df["best_idf"]=0
#lst_keywords_byclass contient: {1180:[mot1 mot2 mot3 ...], 2520:[mot1 mot2 mot3 ...] ...}
#lst_keywords_byclass = sorted(lst_keywords_byclass)
for (key_kw, value_kw) in sorted(lst_keywords_byclass.items()):
  #key_kw=1180
  #value_kw=[mot1 mot2 mot3 ...]
  df['class_'+str(key_kw)]=df['designation'].apply(lambda x: scoring(x, value_kw))


col_start=8
df["best_idf"]=df.iloc[:,col_start:].idxmax(axis=1)
#df["best_idf"]= [2583 if (s.sum()==0) else df.iloc[:,col_start:].idxmax(axis=1) for s in df.iloc[:,1col_start1:]]
#gestion des cas où toutes les colonnes valent 0
#on affecte la classe 2583 (majoritaire)
for i in range(len(df)):
  sum = df.iloc[i,col_start:].sum()
  if (sum == 0):
    df["best_idf"][i]="2583"

# print("#Articles:", len(df))
# print(df["best_idf"].value_counts())
#path = '/Drive/My Drive/Projet Rakuten'
#df.to_csv(f'{path}/damien.csv')

#Expressions régulières pour identifier les différentes unités
#TODO transformer en numérique pas en liste
import re

#nombre de nombres à 2 chiffres ou +
r = re.compile("[0-9]{2,}") 
#df['desi_nb2chiffres+']= df['designation'].apply(lambda x: min(1,len(r.findall(x))))
df['desc_nb2chiffres+']= df['description'].apply(lambda x: min(1,len(r.findall(x))))
#XGo ou XMo ou XTo
#r = re.compile("([\d.]+)\s?(go|mo|to|Go|Mo|To|giga|gigas)") 
#df['desi_Go']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
#df['desc_Go']=df['description'].apply(lambda x: min(1,len(r.findall(x))))
#N°X
r = re.compile("[Nn][°]\s?[\d]+") 
#df['desi_num']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
df['desi_num']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
r = re.compile("[Nn][°]\s?[\d]+") 
#df['desi_num']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
df['desc_num']=df['description'].apply(lambda x: min(1,len(r.findall(x))))
#Poids kg Kg mg g
#r = re.compile("[0-9\.]+[kKm]?[g]") #([\d.]+)\s+(lbs?|oz|g|kg) 
r = re.compile("([\d.]+)\s?(KG|Kg|g|kg|mg)[\s.]") #(nombres ou .)+ / (espace)+ / (kg mg ..)
#df['desi_poids']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
df['desc_poids']=df['description'].apply(lambda x: min(1,len(r.findall(x))))
#Taille cm mm m
r = re.compile("([\d.]+)\s?(cm|mm|m|M)[\s.]") 
#df['desi_long']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
df['desc_long']=df['description'].apply(lambda x: min(1,len(r.findall(x))))
#Volume mL cL dL
r = re.compile("([\d.]+)\s?(mL|L|ml|l|cl)[\s.]") 
#df['desi_vol']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
df['desc_vol']=df['description'].apply(lambda x: min(1,len(r.findall(x))))
#Age
r = re.compile("([\d.]+)\s?(an|ans|An|Ans|mois|Mois)[\s.]") 
#df['desi_ans_mois']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
df['desc_ans_mois']=df['description'].apply(lambda x: min(1,len(r.findall(x))))
#Pièces
r = re.compile("([\d.]+)\s?(pc|pcs|pièces|pièce)[\s.]") 
#df['desi_pieces']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
df['desc_pieces']=df['description'].apply(lambda x: min(1,len(r.findall(x))))
#%
r = re.compile("([\d.]+)\s?%[\s.]") 
#df['desi_pourcent']=df['designation'].apply(lambda x: min(1,len(r.findall(x))))
df['desc_pourcent']=df['description'].apply(lambda x: min(1,len(r.findall(x))))

#TODO merger création features ci-dessus à la fonction  feature?
def feature(df) :
    df['desi_word_count'] = df['designation'].apply(lambda x : len(str(x).split()))
    df['desi_char_count (w/o space)'] = df['designation'].apply(lambda x : len(x.replace(" ","")))
    df['desi_word_density'] = df['desi_word_count'] / (df['desi_char_count'] + 1)
    df['desi_total_length'] = df['designation'].apply(len)
    df['desi_capitals'] = df['designation'].apply(lambda comment: sum(1 for c in comment if c.isupper()))
    # df['desi_caps_vs_length'] = df.apply(lambda row: float(row['desi_capitals'])/float(row['desi_total_length']),axis=1)
    df['desi_num_exclamation_marks'] =df['designation'].apply(lambda x: x.count('!'))
    df['desi_num_question_marks'] = df['designation'].apply(lambda x: x.count('?'))
    df['desi_num_punctuation'] = df['designation'].apply(lambda x: sum(x.count(w) for w in '.,;:'))
    df['desi_num_symbols'] = df['designation'].apply(lambda x: sum(x.count(w) for w in '*&$%+-/'))
    df['desi_num_unique_words'] = df['designation'].apply(lambda x: len(set(w for w in x.split())))
    df['desi_words_vs_unique'] = df['desi_num_unique_words'] / df['desi_word_count']
    df["desi_word_unique_percent"] =  df["desi_num_unique_words"]*100/df['desi_word_count']
    
    df['descri_word_count'] = df['description'].apply(lambda x : len(str(x).split()))
    df['descri_char_count (w/o space)'] = df['description'].apply(lambda x : len(str(x).replace(" ","")))
    df['descri_word_density'] = df['descri_word_count'] / (df['descri_char_count'] + 1)
    df['descri_total_length'] = df['description'].apply(lambda x :len(str(x)))
    df['descri_capitals'] = df['description'].apply(lambda comment: sum(1 for c in str(comment) if c.isupper()))
    # df['descri_caps_vs_length'] = df.apply(lambda row: float(row['descri_capitals'])/float(row['descri_total_length']),axis=1)
    df['descri_num_exclamation_marks'] =df['description'].apply(lambda x: str(x).count('!'))
    df['descri_num_question_marks'] = df['description'].apply(lambda x: str(x).count('?'))
    df['descri_num_punctuation'] = df['description'].apply(lambda x: sum(str(x).count(w) for w in '.,;:'))
    df['descri_num_symbols'] = df['description'].apply(lambda x: sum(str(x).count(w) for w in '*&$%'))
    df['descri_num_unique_words'] = df['description'].apply(lambda x: len(set(w for w in str(x).split())))
    df['descri_words_vs_unique'] = df['descri_num_unique_words'] / df['descri_word_count']
    df["descri_word_unique_percent"] =  df["descri_num_unique_words"]*100/df['descri_word_count']
    return df


feature(df)

df = df.drop(columns='Unnamed: 0' )






