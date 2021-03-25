# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:24:15 2021

@author: Dam
"""
import requests
import io
import random
import pandas as pd
def get_random_article(classe=-1, nbrows=1):
    url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/Datasets/dataset_streamlit.csv"
    download = requests.get(url).content
    df=pd.read_csv(io.StringIO(download.decode('utf-8')), index_col=0)
    if (classe >= 0):
        df=df[df["prdtypecode"]==classe]
    listchoix=random.sample(range(len(df)), nbrows)
    #print(listchoix)
    df=df.iloc[listchoix]
    #print("longueur ", len(df))
    for i in range(len(df)):
        print(i)
        path="/images/"
        img = df.iloc[i,5]
        df.iloc[i,5]=path+img
    return df


def get_sample_img_classe(classe=-1, nbrows=1):
    url = "https://raw.githubusercontent.com/JulienJ-44/rakuteam/main/Datasets/echantillons_streamlit.csv"
    download = requests.get(url).content
    df2=pd.read_csv(io.StringIO(download.decode('utf-8')), index_col=0)
    for i in range(len(df2)):
        print(i)
        path="/echantillons/"
        img = df2.iloc[i,1]
        df2.iloc[i,1]=path+img
    return df2


get_sample_img_classe()




#df=get_random_article(2583, 3)
#print(df.head())
"""
print(df.head(1))
import shutil
for i in range(len(df)):
   
  path="D:/DataScientest/images/images/image_train/"
  img = df.iloc[i,5]
  
  img=path+img
  filePath = shutil.copy(img,'C:/Users/Dam/Documents/GitHub/rakuteam/Streamlit_rakuten/image"s')
"""
