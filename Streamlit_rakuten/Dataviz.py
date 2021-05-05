# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:17:29 2021

@author: Lenovo
"""
import streamlit as st
import requests
import io
import pandas as pd
from modelisation import *
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
from bokeh.io import output_notebook
from bokeh.transform import factor_cmap
from bokeh.palettes import Category20b,  viridis, Turbo256, d3,cividis
from bokeh.models.tools import HoverTool

from bokeh.transform import linear_cmap

@st.cache
def get_dataset_cleaned_old():
  url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/Features/data_features_final.csv"# Make sure the url is the raw version of the file on GitHub
  download = requests.get(url).content
  dataset_cleaned = pd.read_csv(io.StringIO(download.decode('utf-8')))
  # Remplacer les labels de 0 à 26
  return dataset_cleaned

@st.cache
def get_dataset_cleaned():
  dataset_cleaned = pd.read_csv("data_features_final.csv")
  # Remplacer les labels de 0 à 26
  return dataset_cleaned

@st.cache
def get_regex_value_counts(val_regex):
    df_code = load_df_code_designation(1)
    df = get_dataset_cleaned()
    df = df[df['designation'].notnull()]
    df_1 = df[df['designation'].str.contains(val_regex)]
    class_nb = pd.DataFrame(df_1['prdtypecode_x'].value_counts())
    class_nb.columns = ["Nombre d'articles"]
    test = class_nb.join(df_code)
    return test

@st.cache
def get_pixel_value_counts(x_2):
  df_code = load_df_code_designation(1)
  df = get_dataset_cleaned()
  class_pix_mean = pd.DataFrame(df.groupby(by='prdtypecode_x')[x_2].mean().round(2))
  class_pix_mean.columns = ["Pourcentage moyen de pixels"]

  test = class_pix_mean.join(df_code).sort_values('Pourcentage moyen de pixels', ascending=False)
  return test


@st.cache
def get_regex_sample(val_regex):
    df_code = load_df_code_designation(1)
    df = get_dataset_cleaned()
    df = df[df['designation'].notnull()]
    df_1 = df[df['designation'].str.contains(val_regex)]
    # class_nb = pd.DataFrame(df_1['prdtypecode_x'].value_counts())
    # class_nb.columns = ["Nombre d'articles"]
    # test = class_nb.join(df_code)
    return df_1.head(10).reset_index()    

def get_proba_bar(df_ypred_proba):  
  from bokeh.io import output_file, show
  from bokeh.models import ColumnDataSource, FactorRange
  from bokeh.plotting import figure
  from bokeh.io import output_notebook
  from bokeh.transform import factor_cmap
  from bokeh.palettes import Set1, Set3, mpl, all_palettes
  from bokeh.models.tools import HoverTool

  output_notebook()


  #selectionner les 3 premières classes en termes de proba
  top_proba = df_ypred_proba.head(3)


  prd_codes = top_proba['libellé'] 
  models = ['Modèle global', 'Random Forest','CNN Image', 'DNN Texte']

  #création d'un dict 
  data = {'Catégorie produit' : prd_codes,
          'Modèle global'   : top_proba['Proba'],
          'Random Forest'   : top_proba['RF'],
          'CNN Image'   : top_proba['CNN img'],
          'DNN Texte'   : top_proba['DNN txt']}



  x = [ (code, model) for code in prd_codes for model in models ]
  counts = sum(zip(data['Modèle global'], data['Random Forest'], 
                  data['CNN Image'],data['DNN Texte']), ()) 

  source = ColumnDataSource(data=dict(x=x, counts=counts))

  #initialisation du hover tool
  hover = HoverTool(
                  tooltips=[
                      ("Probabilité", "@counts")
                    ])

  p = figure(x_range=FactorRange(*x), plot_height=500, plot_width=1000, 
            #title="Probabilités des différents modèle pour les 3 premières classes",
            toolbar_location=None, tools="")

  pal = ('#d98880', '#a569bd', '#82e0aa','#3498db'  ) 
        
  p.add_tools(hover)

  p.vbar(x='x', top='counts', width=0.9, source=source, line_color="white",

  # use the palette to colormap based on the the x[1:2] values
  fill_color=factor_cmap('x', palette=pal, factors=models, start=1, end=2))

  p.y_range.start = 0
  p.x_range.range_padding = 0.1
  p.xaxis.major_label_orientation = 1
  p.xgrid.grid_line_color = None

  return p

def get_keywords_bar(df_keywords):


  output_notebook()

  df_keywords = df_keywords.sort_values('tfidf', ascending= True)

  desi = df_keywords.iloc[:,0]

  counts = df_keywords.iloc[:,1]

  hover1 = HoverTool(
          tooltips=[
              ("Score TF-IDF", "@right")
            ])

  # Instanciation de la figure

  p1 = figure(y_range = desi,                         # l'axe des ordonnées devient un axe catégoriel
            plot_width = 900, plot_height = 400,      # dimensions de la figure
            x_axis_label="Score TF-IDF", y_axis_label="Top 15 des mots clés") 

  couleurs = viridis(15) #Reverse(viridis(15))

  # Instanciation d'un diagramme à barres horizontales
  p1.add_tools(hover1)

  p1.hbar(y = desi,                    # ordonnées
        right = counts,  # abscisses
        height = 0.7,
        color=couleurs,
        line_color='black')     

  return p1

def get_colors_bar(df):
  import pandas as pd

  df_color = df[['R','G','B']]
  desi = list(df_color.columns)
  counts = df_color.iloc[0,:]

  hover1 = HoverTool(
          tooltips=[
              ("Nombre de pixels", "@right")
            ])

  # Instanciation de la figure

  p1 = figure(y_range = desi,                         # l'axe des ordonnées devient un axe catégoriel
            plot_width = 900, plot_height = 400,      # dimensions de la figure
            x_axis_label="Nombre de pixels activés", y_axis_label="Canaux R G B") 

  # Instanciation d'un diagramme à barres horizontales
  p1.add_tools(hover1)

  couleurs = ['red', 'green','cyan' ]

  p1.hbar(y = desi,                    # ordonnées
        right = counts,  # abscisses
        height = 0.7,
        fill_color=couleurs,
        line_color='black')     

  return p1

def get_text_features_bar(df):
  df_text = df.drop(columns=['R','G','B','blanc','noir','designation', 'description','productid', 'prdtypecode','desi_nb_phrases','desc_nb_phrases' ,'best_idf'])

  df_text = df_text.T

  df_text = df_text[df_text[0]>0]

  df_text = df_text.filter(like = 'des', axis=0)
  desi = list(df_text.index)

  counts = df_text.iloc[:,0]

  hover1 = HoverTool(
          tooltips=[
              ("", "@right")
            ])

  # Instanciation de la figure

  p1 = figure(y_range = desi,                         # l'axe des ordonnées devient un axe catégoriel
            plot_width = 900, plot_height = 400,      # dimensions de la figure
            x_axis_label="Nombre", y_axis_label="Features texte") 

  couleurs = viridis(len(desi))
  # Instanciation d'un diagramme à barres horizontales
  p1.add_tools(hover1)

  p1.hbar(y = desi,                    # ordonnées
        right = counts,  # abscisses
        height = 0.7,
        fill_color=couleurs,
        line_color='black')     

  return p1


