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