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

@st.cache
def get_dataset_cleaned():
  url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/Features/data_features_final.csv"# Make sure the url is the raw version of the file on GitHub
  download = requests.get(url).content
  dataset_cleaned = pd.read_csv(io.StringIO(download.decode('utf-8')))
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

@st.cache()
def class_proba_multibar(df_ypred_proba, top=5,):
      from bokeh.io import output_file, show
      from bokeh.models import ColumnDataSource, FactorRange
      from bokeh.plotting import figure

      output_file("bars.html")

      top_proba = df_ypred_proba.head(top)

      prdct_codes = top_proba['libellé']
      voting = top_proba['Voting']
      rf = top_proba['RF']
      dnn = top_proba['DNN txt']
      cnn = top_proba['CNN img']

      models = ['Voting', 'Random Forest', 'DNN Texte', 'CNN Image']

      data = {'Classes' : prdct_codes,
              'Voting'   : voting,
              'Random Forest'   : rf,
              'DNN Texte'   : dnn,
              'CNN Image': cnn}

      # this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
      x = [ (classes, models) for code in prdct_codes for model in models ]
      counts = sum(zip(data['Voting'], data['Random Forest'], data['DNN Texte'], data['CNN Image']), ()) # like an hstack

      source = ColumnDataSource(data=dict(x=x, counts=counts))

      p = figure(x_range=FactorRange(*x), plot_height=250, title="Fruit counts by year",
                toolbar_location=None, tools="")

      p.vbar(x='x', top='counts', width=0.9, source=source)

      p.y_range.start = 0
      p.x_range.range_padding = 0.1
      p.xaxis.major_label_orientation = 1
      p.xgrid.grid_line_color = None

      return p

      