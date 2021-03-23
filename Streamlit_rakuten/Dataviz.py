# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:17:29 2021

@author: Lenovo
"""

import requests
import io
import pandas as pd


def get_dataset_cleaned():
  url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/Datasets/dataset_cleaned.csv"# Make sure the url is the raw version of the file on GitHub
  download = requests.get(url).content
  dataset_cleaned = pd.read_csv(io.StringIO(download.decode('utf-8')))
  # Remplacer les labels de 0 à 26
  return dataset_cleaned