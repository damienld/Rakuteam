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
from bokeh.plotting import figure, output_notebook, show 
from bokeh.models.tools import HoverTool
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6

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
    
  
    regex = get_regex_value_counts(x)
    regex = regex.sort_values("Nombre d'articles",ascending = True)

    desi = regex["désignation"]
    
    counts = regex["Nombre d'articles"]
        
    hover1 = HoverTool(
            tooltips=[
                ("Nombre d'articles", "@right")
               ])

    # Instanciation de la figure
    
    p1 = figure(y_range = desi,                         # l'axe des ordonnées devient un axe catégoriel
               plot_width = 900, plot_height = 400,      # dimensions de la figure
               x_axis_label="Nombre d'articles", y_axis_label="Désignation de la classe") 
    
    # Instanciation d'un diagramme à barres horizontales
    p1.add_tools(hover1)
    
    p1.hbar(y = desi,                    # ordonnées
           right = counts,  # abscisses
           height = 0.7,
           fill_color="#9b59b6",
           line_color='black')                   # épaisseur
    
    # Affichage de la figure
    
    st.bokeh_chart(p1)
    
    PAGES_2 = {
    "Moyenne de nombre de pixel 'Red'": 'R',
    "Moyenne de nombre de pixel 'Green'": 'G',
    "Moyenne de nombre de pixel 'Blue'": 'B',
    #"Pourcentage moyen de pixel 'Black'": 'noir',
    "Pourcentage moyen de pixel 'White'": 'blanc',
    }
    
    couleur = {
    'R': '#e74c3c',
    'G': '#2ecc71',
    'B': '#5499c7',
    'noir': '#1b2631',
    'blanc': '#ecf0f1',
    }
    
    selection_2 = st.radio("Sélectionner le motif à rechercher", list(PAGES_2.keys()))
    x_2 = PAGES_2[selection_2]
    
    print(x_2)
    
    pixel = get_pixel_value_counts(x_2)
    
    pixel = pixel.sort_values("Pourcentage moyen de pixels",ascending = True)
    
    if x_2 == 'blanc' or x_2 == 'noir':
      x_name = 'Pourcentage moyen de pixels '+ x_2
      counts = pixel["Pourcentage moyen de pixels"]*100
    else:
      x_name = 'Nombre moyen de pixels '+ x_2
      counts = pixel["Pourcentage moyen de pixels"]
    
    desi = pixel["désignation"]
    
    hover2 = HoverTool(
            tooltips=[
                (x_name, "@right")
               ])

    # Instanciation de la figure
    
    p2 = figure(y_range = desi,                   # l'axe des ordonnées devient un axe catégoriel
               plot_width = 900, plot_height = 400,      # dimensions de la figure
               x_axis_label=x_name, y_axis_label="Désignation de la classe")
    
    p2.add_tools(hover2)
    
    p2.hbar(y = desi,                    # ordonnées
           right = round(counts),  # abscisses
           height = 0.7,
           fill_color=couleur[x_2],
           line_color='black')
    
    st.bokeh_chart(p2)
    
    
    
    

    
    
    
    # df_code = load_df_code_designation(1)
    
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
