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

     
# app3.py
def app():
    st.title('Dataviz reporting')
    st.write('Exploration de donnée')
    
 
    
    # for a scatter plot we will create random data 
    #x1 = np.random.uniform(size=100) 
    #y1 = np.random.uniform(size=100) 
    #x2 = np.random.uniform(size=100) 
    #y2 = np.random.uniform(size=100) 
    #fig = plt.figure() 
    #plt.scatter(x1, y1, color='b', s=5, label='random data 1') 
    #plt.scatter(x2, y2, color='r', s=5, label='random data 2') 
    #plt.xlabel('X') 
    #plt.ylabel('Y') 
    #plt.legend() 
    #st.pyplot(fig)
    
    
    
    
    #créer la table de répartition des classe et 
    # class_nb = pd.DataFrame(df['prdtypecode_x'].value_counts())
    # class_nb.columns = ["Nombre d'articles"]
    # test = class_nb.join(df_desig_class)
    
    
    saisie_manuelle = st.text_input("Entrer le mot à chercher")
    
    PAGES = {
    "Pas de motif particulier (tous les articles)": '.',
    "n°,N° ou numéro": '(numéro )',
    "Unités de longueur (m, cm, mm)": '([\d.]+)\s?(cm|mm|m|M)[\s.]',
    "Unités de poids (kg, g, mg)": '([\d.]+)\s?(cm|mm|m|M)[\s.]',
    "Unités de volume (l, cl, ml)": '([\d.]+)\s?(cm|mm|m|M)[\s.]',
    "Saisie manuelle": saisie_manuelle
    }

    
    
    selection = st.radio("Sélectionner le motif à rechercher", list(PAGES.keys()))
    x = PAGES[selection]
    
    
    # x = '(numéro )'

    test = get_regex_value_counts(x)
    
    fig = plt.figure(figsize=(50,18))
    # plt.subplot(1,2,1)
    
    # g = sns.barplot(data=test, x="Classe - Désignation", y="Nombre d'article")
    # g.set_xticklabels(g.get_xticklabels(),rotation=90);
    # # print(test)
    sns.set(font_scale=3) 
    # plt.subplot(1,2,2)
    sns.barplot(data=test, y="désignation", x="Nombre d'articles", orient='h');
    # h.set_xticklabels(g.get_xticklabels(),rotation=90);
    st.pyplot(fig)
    
    PAGES_2 = {
    "Moyenne de nombre de pixel 'Red'": 'R',
    "Moyenne de nombre de pixel 'Green'": 'G',
    "Moyenne de nombre de pixel 'Blue'": 'B',
    "Moyenne de nombre de pixel 'Black'": 'noir',
    "Moyenne de nombre de pixel 'White'": 'blanc',
    }

    
    
    selection_2 = st.radio("Sélectionner le motif à rechercher", list(PAGES_2.keys()))
    x_2 = PAGES_2[selection_2]
     

    test_2 = get_pixel_value_counts(x_2)
    
    st.dataframe(test_2)
    
    fig_2 = plt.figure(figsize=(50,18))
    # plt.subplot(1,2,1)
    
    # g = sns.barplot(data=test, x="Classe - Désignation", y="Nombre d'article")
    # g.set_xticklabels(g.get_xticklabels(),rotation=90);
    # # print(test)
    sns.set(font_scale=3) 
    # plt.subplot(1,2,2)
    # sns.barplot(data=test_2, y="désignation", x="Pourcentage moyen de pixels", orient='h');
    # h.set_xticklabels(g.get_xticklabels(),rotation=90);
    st.pyplot(fig_2)
