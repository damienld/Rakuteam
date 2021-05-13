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
from bokeh.models.widgets import Panel, Tabs
import bokeh.models
import time

df = get_dataset_cleaned()
df_desig_class = load_df_code_designation(1)

from sample import *

     
# app3.py
# @st.cache
def app():
    st.title('Analyse exploratoire des données')
    st.write("""Comme dans tout projet de data science, la première étape que nous avons réalisée est une analyse rapide des données.""")
    st.write("""Ainsi nous avons pu nous approprier le jeu de données mis à notre disposition, et identifier d'eventuels schémas récurents pouvant être utilisés 
    dans le cadre du machine learning""")   
    st.write("""Pour cela, nous avons effectué une visualisation des données en utilisant les bibliothèques Matplotib, 
    Seaborn et WordCloud, ce qui nous a permis de mieux comprendre et caractériser la cohérence des articles au sein d’une même classe.""")


    alg = ['Texte','Expressions régulières','Image']

    st.info('Merci de sélectionner ci-dessous le type de données que vous souhaitez explorer.')
    
    classifier = st.selectbox('', alg, )



    if classifier=='Texte':
        # placeholder=st.image("./présentation/gif_HUD.gif", width=600)
        # time.sleep(4)
        # placeholder.empty()
        st.subheader("**Exploration du texte**")
        
        st.info("Vous pouvez saisir ci-dessous le mot que vous souhaitez chercher dans la désignation des articles.")
        saisie_manuelle = st.text_input('', )
    
        PAGES = {
        "Saisie manuelle": saisie_manuelle,
        }
        mot = saisie_manuelle
        saisie_manuelle  = '[ ,.]'+saisie_manuelle+'[ ,.]'
        regex = get_regex_value_counts(saisie_manuelle)
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
        

        text_display = "Nombre d'occurence par classe du mot"
              
        Affichage_titre(text_display,mot)

        st.bokeh_chart(p1)
        
        df_regex = get_regex_sample(saisie_manuelle)
        
        df_regex = df_regex['designation']
        import re
        s = ""
        if mot != "": 
            # st.write('Voici quelques exemples de désignations contenant le mot '+mot) 

            text_display = "Exemples de désignations contenant le mot"
        # mot_display = " "+mot+" "

            Affichage_titre(text_display,mot)
        
            exemple_nb = 1
            for sentence in df_regex:
                x = re.split("\s",sentence)
                for word in x:
                    v = word
                    
                    if word == mot:
                        
                        v = """<span style="
                                    background:yellow;
                                    color: black;
                                    background:#42f566;
                                    padding: 0px 5px;
                                    border-radius: 5px;">"""+word +'</span>'
                        
                    myTuple = (s, v)
    
                    s = " ".join(myTuple)
                    
                s = str(exemple_nb) + ". " + s
                st.markdown(s, unsafe_allow_html=True)
                exemple_nb += 1
                s=""
                # st.text(s.replace(mot1, '\033[44;33m{}\033[m'.format(mot)))
        
        
        
    elif classifier=='Expressions régulières':
        st.subheader("**Recherche d'expressions régulières**")
    
        PAGES = {
        "Pas de motif particulier (afficher tous les articles)": '.',
        "n°, N° ou numéro": '(numéro )',
        "Unités de longueur (m, cm, mm)": '([\d.]+)\s?(cm|mm|m|M)[\s.]',
        "Unités de poids (kg, g, mg)": '([\d.]+)\s?(kg|g|mg|Kg)[\s.]',
        "Unités de volume (l, cl, ml)": '([\\d.]+)\\s?(mL|L|ml|l|cl)[\\s.]',
        
        }

        DESIGNATION = {
        '(numéro )' : "n°, N ° ou numéro",
        '([\d.]+)\s?(cm|mm|m|M)[\s.]' : "m, cm ou mm",
        '([\d.]+)\s?(kg|g|mg|Kg)[\s.]': "kg, g ou mg",
        '([\\d.]+)\\s?(mL|L|ml|l|cl)[\\s.]': "l, cl ou ml",

        }
        
        st.markdown("Sélectionner le motif à rechercher")
        selection = st.radio("", list(PAGES.keys()))
        x = PAGES[selection]
        
        df_regex = get_regex_sample(x)
        
        df_regex = df_regex['designation']
     
        
        regex = get_regex_value_counts(x)
        regex = regex.sort_values("Nombre d'articles",ascending = True)
    
        desi = regex["désignation"]
        
        counts = regex["Nombre d'articles"]


            
        hover2 = HoverTool(
                tooltips=[
                    ("Nombre d'articles", "@right")
                   ])
    
        # Instanciation de la figure
        
        p2 = figure(y_range = desi,                         # l'axe des ordonnées devient un axe catégoriel
                   plot_width = 900, plot_height = 400,      # dimensions de la figure
                   x_axis_label="Nombre d'articles", y_axis_label="Désignation des classe") 
        
        # Instanciation d'un diagramme à barres horizontales
        p2.add_tools(hover2)
        
        p2.hbar(y = desi,                    # ordonnées
               right = counts,  # abscisses
               height = 0.7,
               fill_color="#9b59b6",
               line_color='black')                   # épaisseur
        
        # Affichage de la figure

        if x == ".": 
            st.write("Nombre total d'articles par classe:")
        
            st.bokeh_chart(p2)

        else: 
            # st.write("Nombre d'articles par classe contenant" +DESIGNATION[x] )
            text_display= "Nombre d'articles par classe contenant"
            mot = DESIGNATION[x]
            Affichage_titre(text_display,mot)
            st.bokeh_chart(p2)
            # st.write('Exemples de désignations contenant '+DESIGNATION[x])
            text_display= "Exemples de désignations contenant"
            mot = DESIGNATION[x]
            Affichage_titre(text_display,mot)



            for sentence in df_regex:
                st.text(sentence)

    else:
        st.subheader("**Exploration des données Images**")
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
        
        st.markdown("Sélectionner le paramètre à afficher")
        selection_2 = st.radio("", list(PAGES_2.keys()))
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
                   x_axis_label=x_name, y_axis_label="Désignation des classe")
        
        p2.add_tools(hover2)
        
        p2.hbar(y = desi,                    # ordonnées
               right = round(counts),  # abscisses
               height = 0.7,
               fill_color=couleur[x_2],
               line_color='black')
        
        st.bokeh_chart(p2)
    
def Affichage_titre(texte,var_select):
     st.markdown("""<span style="
                                font-weight:bold;
                                color: white;
                                text-decoration: underline;
                                font-size: 20px;
                                ">"""+texte +"""</span><span>:  </span><span style="
                                font-weight:bold;
                                color: black;
                                background:#42f566;
                                font-size: 22px;
                                padding: 5px 10px;
                                border-radius: 5px;
                                ">"""+var_select+"""</span>""" , unsafe_allow_html=True)
   