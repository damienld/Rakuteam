# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 01:45:38 2021

@author: slam_
"""

import streamlit as st

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
#import plotly.graph_objects as go

from modelisation import *

def displayclassif_and_cross(model_index):
    st.text(get_classifreport(model_index))   
    cross=get_crosstab(model_index)
    fig=plt.figure(figsize=(70,50))
    sns.heatmap(cross, annot=True, cmap="YlGnBu");
    plt.xticks(rotation=90);
    st.pyplot(fig)   
    
Models = ["Modèle RF", 
         "Modèle NN Text", 
         "Modèle NN Image", 
         "Voting Classifier (3modèles)"]
   
# app2.py
def app():
    st.title('MODELISATION')

    alg = ['1-RF', '2-CNN image', '3-DNN texte', 'weighted voting']
    classifier = st.selectbox('Selection du modèle', alg)
    if classifier=='1-RF':
        model_index = "1"
        displayclassif_and_cross(model_index)
    elif classifier == '2-CNN image':
        model_index = "2"
        displayclassif_and_cross(model_index)
    elif classifier == '3-DNN texte':
        model_index = "3"
        displayclassif_and_cross(model_index)
    elif classifier == 'weighted voting':
        model_index = "4"
        displayclassif_and_cross(model_index)
