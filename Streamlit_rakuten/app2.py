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
    st.markdown("**Classification Report: **")
    st.text(get_classifreport(model_index))   
    path="./Demo/heatmap" + model_index +".png"
    st.image(path)#, width=600)
    #cross=get_crosstab(model_index)
    #fig=plt.figure(figsize=(28,20))
    #sns.heatmap(cross, annot=True, cmap="YlGnBu");
    #plt.xticks(rotation=90);
    #st.markdown("**Confusion Matrix Heatmap: **")
    #st.pyplot(fig)   
    

# app2.py
def app():
    st.title('MODELISATION')

    alg = ['1-RF', '2-CNN image', '3-DNN texte', '4-Voting Classifier']
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
    elif classifier == '4-Voting Classifier':
        model_index = "4"
        displayclassif_and_cross(model_index)
