# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 09:24:08 2021

@author: slam_
"""

import streamlit as st
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
from Dataviz import *
from modelisation import *
import seaborn as sns

df = get_dataset_cleaned()
df_desig_class = load_df_code_designation(1)

from sample import *

     
# app3.py
# @st.cache
def app():
    st.title('Dataviz reporting')
    st.write('Exploration de donnée')   
    
    saisie_manuelle = st.text_input("Entrer le mot à chercher")
    
    PAGES = {
    "Saisie manuelle": saisie_manuelle,
    "Pas de motif particulier (tous les articles)": '.',
    "n°,N° ou numéro": '(numéro )',
    "Unités de longueur (m, cm, mm)": '([\d.]+)\s?(cm|mm|m|M)[\s.]',
    "Unités de poids (kg, g, mg)": '([\d.]+)\s?(cm|mm|m|M)[\s.]',
    "Unités de volume (l, cl, ml)": '([\d.]+)\s?(cm|mm|m|M)[\s.]',
    
    }
    
    selection = st.radio("Sélectionner le motif à rechercher", list(PAGES.keys()))
    x = PAGES[selection]
    
  
    test = get_regex_value_counts(x)
    
    fig = plt.figure(figsize=(50,18))
 
    sns.set(font_scale=3) 
    
    sns.barplot(data=test, y="désignation", x="Nombre d'articles", orient='h');
    
    plt.ylabel("Désignation de la classe d'articles");
    
    plt.xlabel("Nombre d'atricles avec au moins une occurence du motif recherché");
    
    st.pyplot(fig)
    
    PAGES_2 = {
    "Moyenne de nombre de pixel 'Red'": 'R',
    "Moyenne de nombre de pixel 'Green'": 'G',
    "Moyenne de nombre de pixel 'Blue'": 'B',
    "Pourcentage moyen de pixel 'Black'": 'noir',
    "Pourcentage moyen de pixel 'White'": 'blanc',
    }

    
    
    selection_2 = st.radio("Sélectionner le motif à rechercher", list(PAGES_2.keys()))
    x_2 = PAGES_2[selection_2]
    test_2 = get_pixel_value_counts(x_2)
    # st.dataframe(test_2)
    fig_2 = plt.figure(figsize=(50,18))
    sns.set(font_scale=3) 
    if x_2 == 'blanc' or x_2 == 'noir':
      x_name = 'Pourcentage moyen de pixels '+ x_2
    else:
      x_name = 'Nombre moyen de pixels '+ x_2
      
    sns.barplot(data=test_2, y="désignation", x='Pourcentage moyen de pixels', orient='h');
    
    plt.ylabel("Désignation de la classe d'articles");
    
    plt.xlabel(x_name);
    
    st.pyplot(fig_2)
    
    
    
    df_code = load_df_code_designation(1)
    
    # print(df_code.head())
    
    # print(df_code)
    
    # alg = list(df_code['désignation'])
    # desi_classe = st.selectbox('Selection de la classe', alg)
    
    # alg_1 = list(range(1,11,1))
    # nb_article = st.selectbox("Nombre d'articles à afficher", alg_1) 
    
    
    # # if st.button("Chercher"):
    # code_classe_1 = df_code[df_code['désignation']==desi_classe]
    # code_classe = code_classe_1.index #['prdtypecode']
        
    # st.text(print('désignation classe: ', desi_classe))
    # st.text(print('code classe: ',code_classe))
    # st.text(print('nb article: ', nb_article))
       
     
    
    
    
    # export = get_random_article(code_classe, nb_article)
    
    # st.dataframe(export)
