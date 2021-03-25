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
from Random_Forest import RF_predict,initRF
from DNN_texte import Dnntexte_predict
from CNN_image import Cnnimage_predict
from modelisation import load_df_code_designation, display_keywords_fromclasscodes
import cv2
import numpy as np
import streamlit as st
import pandas as pd
from sample import get_random_article
from sklearn.preprocessing import StandardScaler


clf1, scaler=initRF()
    
def predict(desi, descr, img, clf1, scaler):
    dfcleaned=clean_manualdata(desi,descr)
    print("RF")
    weightRF=0.73
    #img="test2.jpg"
    df=add_features_to_manualdf(dfcleaned, img)
    #st.dataframe(df)   
    df=df.fillna(0)
    df_rf=df.drop(["prdtypecode","designation","description","productid","best_idf"], axis=1)
    #ypred_proba_RF=RF_predict(True, df_rf)
    print("model RF fitted")
    print(df_rf.head(1))
    df_rf=scaler.transform(df_rf)
    ypred_proba_RF = clf1.predict_proba(df_rf)
    df_ypred_proba_RF = pd.DataFrame(ypred_proba_RF).T
    df_ypred_proba_RF=df_ypred_proba_RF.sort_index(axis=0)
    print (ypred_proba_RF)
    
    print("CNN")
    weightCNN=0.54
    ypred_proba_CNN=Cnnimage_predict(img)
    df_ypred_proba_CNN = pd.DataFrame(ypred_proba_CNN).T
    df_ypred_proba_CNN = df_ypred_proba_CNN.sort_index(axis=0)
    print (ypred_proba_CNN)    
    
    print("DNN")
    weightDNN=0.82
    ypred_proba_DNN=Dnntexte_predict(desi, descr)
    df_ypred_proba_DNN = pd.DataFrame(ypred_proba_DNN).T
    df_ypred_proba_DNN=df_ypred_proba_DNN.sort_index(axis=0)
    print (ypred_proba_DNN)
    
    print("Voting")
    ypred_proba=(ypred_proba_DNN*weightDNN+ypred_proba_RF*weightRF+ypred_proba_CNN*weightCNN)/(weightDNN+weightRF+weightCNN)
    df_ypred_proba = pd.DataFrame(ypred_proba).T
    df_ypred_proba =df_ypred_proba.sort_index(axis=0)
    print (ypred_proba)
    
    df_code = load_df_code_designation(3).sort_index(axis=0)
    df_ypred_proba=pd.concat([df_ypred_proba,df_code,df_ypred_proba_RF,df_ypred_proba_DNN,df_ypred_proba_CNN],axis=1)
    df_ypred_proba=df_ypred_proba.drop("Unnamed: 0", axis=1)
    df_ypred_proba.columns=["Voting","classe","libellé","RF","DNN txt","CNN img"]
    df_ypred_proba=df_ypred_proba.sort_values(by='Voting', ascending=False)
    df_ypred_proba=df_ypred_proba.reset_index()
    df_ypred_proba=df_ypred_proba.drop("index",axis=1)
    #df_ypred_proba.sort()
    #print(df_ypred_proba.head(5))
    st.write("Probabilités des différents modèles par classe")
    df_ypred_proba = df_ypred_proba.astype({'classe': object})
    st.dataframe(df_ypred_proba.style.highlight_max(axis=0))
    classe_code_best_proba=int(df_ypred_proba.iloc[0,1])
    df_keywords=display_keywords_fromclasscodes(classe_code_best_proba)#,2583)
    st.write("Mots-clés de la classe prédite")
    st.dataframe(df_keywords)


#predict("bébé","","",clf1,scaler)

def app():
    file_input2=""
    #desiinit="jeu chaise longue pcs textilène noir noir"
    #descinit="cet ensemble deux chaises longues haute qualité petite table assortie idéal passer après-midi détente jardin camping chaises longues durables faciles nettoyer revêtues textilène doux confortable construites cadre acier robuste deux chaises longues d'extérieur durables résistants intempéries l'ensemble complété table assortie élégant dessus table verre lequel pouvez mettre boissons garder livre téléphone portée main cet ensemble excellent ajout espace vie extérieur couleur noir matériau chaise longue structure acier 43 siège dossier textilène dimensions chaise longue 200 58 32 cm dimensions table 30 30 295 cm hauteur dossier réglable 62/72/80/89/95 cm comprend table dessus table verre mm d'épaisseur résistance intempéries matériel polyester 30 pvc 70"
    st.title('PREDICTION')
    
    alg = ['Manuel','Aléatoire']
    classifier = st.selectbox('Sélection:', alg)
    if classifier=='Manuel':
        st.subheader("Mode Manuel")
        desi=st.text_area("Entrer la désignation")
        descr=st.text_area('Entrer la description')
        file_input = st.file_uploader("Choose a image file", type="jpg")
        img=""
        if file_input is not None: 
            # Convert the file to an opencv image.
            file_bytes = np.asarray(bytearray(file_input.read()), dtype=np.uint8)
            opencv_image = cv2.imdecode(file_bytes, 1)
            st.image(opencv_image, channels="BGR")
            img=file_input
        if st.button("Chercher"):
            predict(desi, descr, img, clf1,scaler)
    else:
        st.subheader("Mode Aléatoire")
        df=get_random_article()
        #st.dataframe(df)
        desi=str(df.iloc[0,0])
        descr=str(df.iloc[0,1])
        desi=st.text_area("Entrer la désignation", desi)
        descr=st.text_area('Entrer la description', descr)
        file_input2="."+df.iloc[0,5]
        img=file_input2
        st.image(img)
        
        codeclasse=(int(df.iloc[0,4]))
        dataf_code_designation=load_df_code_designation()
        ligne=dataf_code_designation[dataf_code_designation["prdtypecode"]==codeclasse]
        classe_reelle_name=str(ligne.iloc[0,1])
        st.markdown("**Classe réelle: **"+str(codeclasse)+" "+classe_reelle_name) #TODO ajouter libellé classe
        predict(desi, descr, img, clf1,scaler)
        
        st.write("Echantillon d'images de la classe réelle")
        
        path="./echantillons/subplot_classe_" + str(codeclasse) +".png"
        st.image(path)