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
from load_functions import *

Models = ["Modèle RF", 
         "Modèle NN Text", 
         "Modèle NN Image", 
         "Voting Classifier (3modèles)"]
   
# app2.py
def app():
    st.title('MODELISATION')
    st.radio("Selection du modèle",(Models))
    

 
alg = ['1-RF', '2-CNN image', '3-DNN texte', 'weighted voting']
classifier = st.selectbox('Selection du modèle', alg)
if classifier=='1-RF':

    model_index = 1
    
    def get_classif_report(index_model):
        model_index=index_model
        y_test=get_ytest()
        y_train=get_ytrain()
        model_selected=set_model_name(index_model)
        y_pred_proba=calc_y_pred(index_model)
        #preparation des données pour le crosstab
        # Convertir Dataframe en array
        y_pred_proba_arr = y_pred_proba.to_numpy()
        y_test = y_test.to_numpy()
        # on prend l'index de la proba la + élevée
        # pour récupérer les classes
        y_pred = y_pred_proba_arr.argmax(axis=1)
        y_pred
        # Pour ajouter une dimension en plus
        y_pred = np.reshape(y_pred, (-1, 1))
        return(metrics.classification_report(y_test, y_pred))
    
        print("Evaluation détaillée de la Classification :\n \n" , get_classif_report("1"))
     
elif classifier == '2-CNN image':

    model_index = 2
    
    def get_classif_report(index_model):
        model_index=index_model
        y_test=get_ytest()
        y_train=get_ytrain()
        model_selected=set_model_name(index_model)
        y_pred_proba=calc_y_pred(index_model)
        #preparation des données pour le crosstab
        # Convertir Dataframe en array
        y_pred_proba_arr = y_pred_proba.to_numpy()
        y_test = y_test.to_numpy()
        # on prend l'index de la proba la + élevée
        # pour récupérer les classes
        y_pred = y_pred_proba_arr.argmax(axis=1)
        y_pred
        # Pour ajouter une dimension en plus
        y_pred = np.reshape(y_pred, (-1, 1))
        return(metrics.classification_report(y_test, y_pred))
    
        print("Evaluation détaillée de la Classification :\n \n" , get_classif_report("1"))
    
elif classifier == 'DNN texte':
    model_index = 3
    
    def get_classif_report(index_model):
        model_index=index_model
        y_test=get_ytest()
        y_train=get_ytrain()
        model_selected=set_model_name(index_model)
        y_pred_proba=calc_y_pred(index_model)
        #preparation des données pour le crosstab
        # Convertir Dataframe en array
        y_pred_proba_arr = y_pred_proba.to_numpy()
        y_test = y_test.to_numpy()
        # on prend l'index de la proba la + élevée
        # pour récupérer les classes
        y_pred = y_pred_proba_arr.argmax(axis=1)
        y_pred
        # Pour ajouter une dimension en plus
        y_pred = np.reshape(y_pred, (-1, 1))
        return(metrics.classification_report(y_test, y_pred))
    
        print("Evaluation détaillée de la Classification :\n \n" , get_classif_report("1"))
    
elif classifier == 'weighted voting':
    model_index = 4
    
    def get_classif_report(index_model):
        model_index=index_model
        y_test=get_ytest()
        y_train=get_ytrain()
        model_selected=set_model_name(index_model)
        y_pred_proba=calc_y_pred(index_model)
        #preparation des données pour le crosstab
        # Convertir Dataframe en array
        y_pred_proba_arr = y_pred_proba.to_numpy()
        y_test = y_test.to_numpy()
        # on prend l'index de la proba la + élevée
        # pour récupérer les classes
        y_pred = y_pred_proba_arr.argmax(axis=1)
        y_pred
        # Pour ajouter une dimension en plus
        y_pred = np.reshape(y_pred, (-1, 1))
        return(metrics.classification_report(y_test, y_pred))
    
print("Evaluation détaillée de la Classification :\n \n" , get_classif_report("1"))