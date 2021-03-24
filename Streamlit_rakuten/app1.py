# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 01:45:08 2021

@author: slam_
"""

# app1.py
import streamlit as st
from cleaning import clean_manualdata
from creation_features import add_features_to_manualdf
from creation_features import add_imgfeatures
from Random_Forest import RF_predict
from DNN_texte import Dnntexte_predict
from modelisation import load_df_code_designation, display_keywords_fromclasscodes
import cv2
import numpy as np
import streamlit as st
import pandas as pd
#df=clean_manualdata("bébé","")
#df=add_features_to_manualdf(df)

#Textbox for text user is entering
#st.subheader("Entrer la description.")
#st.long_text_input("Entrer la désignation.")

#text = st.text_input('Enter text') #text is stored in this variable

#add_imgfeatures(df, file_bytes)
#uploaded_file = st.file_uploader("Choose a image file", type="jpg")

#df_keywords=display_keywords_fromclasscodes(10)#,2583)
#df_keywords.head(15)
#article 77312 / 2582
#y_predproba DNN:3.510231e-09,1.3902971e-16,3.0522055e-15,5.5146954e-09,5.431842e-08,3.6039685e-13,4.7371586e-06,0.9474246,0.051802292,1.4928757e-07,0.00032929692,5.3290102e-14,1.42541e-13,1.1241913e-06,1.3613869e-09,2.1363553e-10,5.1120828e-09,1.5232825e-17,9.299475e-06,1.6853333e-12,4.857436e-13,2.281767e-05,0.00038954898,1.3751665e-05,8.9084694e-12,1.671928e-06,7.500114e-07
desiinit="jeu chaise longue pcs textilène noir noir"
descinit="cet ensemble deux chaises longues haute qualité petite table assortie idéal passer après-midi détente jardin camping chaises longues durables faciles nettoyer revêtues textilène doux confortable construites cadre acier robuste deux chaises longues d'extérieur durables résistants intempéries l'ensemble complété table assortie élégant dessus table verre lequel pouvez mettre boissons garder livre téléphone portée main cet ensemble excellent ajout espace vie extérieur couleur noir matériau chaise longue structure acier 43 siège dossier textilène dimensions chaise longue 200 58 32 cm dimensions table 30 30 295 cm hauteur dossier réglable 62/72/80/89/95 cm comprend table dessus table verre mm d'épaisseur résistance intempéries matériel polyester 30 pvc 70"


def app():
    st.title('PREDICTION')
    st.subheader("Entrée manuelle")
    
    desi = st.text_area("Entrer la désignation", desiinit)#designation is stored in this variable
    descr = st.text_area('Entrer la description', descinit) #description is stored in this variable
    #text_des = st.long_text_input(num_lines=3)
    #text_des = st.text_area()
    
    #for n in range(1):
    #    desi.append(st.text_input(label='', key=f'Texts {n}'))
    
    # creating a file uploader 
    #file_input="test2.jpg"#for testing only
    file_input = st.file_uploader("Choose a image file", type="jpg")
    if file_input is not None: """
        # Convert the file to an opencv image.
        file_bytes = np.asarray(bytearray(file_input.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
    
        # Afficher l'image:
        st.image(opencv_image, channels="BGR")
        
        df=clean_manualdata(descr,desi)
        df=add_features_to_manualdf(df,file_input)
        #img="test2.jpg"
        add_imgfeatures(df, file_input)
        
        st.dataframe(df)"""
    
    if st.button("Chercher"):
    #    desi=desiinit
    #descr=descinit
        dfcleaned=clean_manualdata(desi,descr)
        print("RF")
        weightRF=0.73
        #img="test2.jpg"
        df=add_features_to_manualdf(dfcleaned, file_input)
        df=df.fillna(0)
        df_rf=df.drop(["prdtypecode","designation","description","productid","best_idf"], axis=1)
        ypred_proba_RF=RF_predict(True, df_rf)
        df_ypred_proba_RF = pd.DataFrame(ypred_proba_RF).T
        df_ypred_proba_RF=df_ypred_proba_RF.sort_index(axis=0)
        print (ypred_proba_RF)
        
        print("DNN")
        weightDNN=0.82
        ypred_proba_DNN=Dnntexte_predict(desi, descr)
        df_ypred_proba_DNN = pd.DataFrame(ypred_proba_DNN).T
        df_ypred_proba_DNN=df_ypred_proba_DNN.sort_index(axis=0)
        print (ypred_proba_DNN)
        
        print("Voting")
        ypred_proba=(ypred_proba_DNN*weightDNN+ypred_proba_RF*weightRF)/(weightDNN+weightRF)
        df_ypred_proba = pd.DataFrame(ypred_proba).T
        df_ypred_proba =df_ypred_proba.sort_index(axis=0)
        print (ypred_proba)
        
        
        df_code = load_df_code_designation(3).sort_index(axis=0)
        df_ypred_proba=pd.concat([df_ypred_proba,df_code,df_ypred_proba_RF,df_ypred_proba_DNN],axis=1)
        df_ypred_proba=df_ypred_proba.drop("Unnamed: 0", axis=1)
        df_ypred_proba.columns=["Voting","classe","libellé","RF","DNN"]
        df_ypred_proba=df_ypred_proba.sort_values(by='Voting', ascending=False)
        df_ypred_proba=df_ypred_proba.reset_index()
        df_ypred_proba=df_ypred_proba.drop("index",axis=1)
        #df_ypred_proba.sort()
        #print(df_ypred_proba.head(5))
        st.dataframe(df_ypred_proba)
        classe_code_best_proba=int(df_ypred_proba.iloc[0,1])
        df_keywords=display_keywords_fromclasscodes(classe_code_best_proba)#,2583)
        st.dataframe(df_keywords.head(15))