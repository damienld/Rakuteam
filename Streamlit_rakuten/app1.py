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
import pandas as pd
from sample import get_random_article
from Dataviz import *

clf1, scaler=loadRF()

from bs4 import BeautifulSoup
import requests
import streamlit.components.v1 as components

def getAmazon(URL):   
    HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/44.0.2403.157 Safari/537.36',
                               'Accept-Language': 'en-US, en;q=0.5'})  
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    try:
        body=soup.find('body').text.strip()
    except:
        body="" 
    try:
        desi=soup.find('h1', attrs={'id': 'title'}).text.strip()
    except:
        desi=""
    try:
        desc=soup.find('div', attrs={'id': 'feature-bullets'}).text.strip().replace('\n', ' ').replace('À propos de cet article', '').replace('Voir plus de détails', '')
    except:
        desc=""
    try:
        img=soup.find('img', attrs={'id': 'landingImage'})['data-old-hires']
    except:
        img=""
    try:
        categ=soup.find('div', attrs={'id': 'wayfinding-breadcrumbs_container'}).text.strip().replace("\n","").replace("  ","")
    except:
        categ="" 
    return desi, desc, img, body, categ
#getAmazon('http://www.amazon.fr/dp/B07MMNG46Y')

def getRakuten(URL):    
    HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/44.0.2403.157 Safari/537.36',
                               'Accept-Language': 'en-US, en;q=0.5'})  
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    try:
        body=soup.find('body').text.strip()
    except:
        body="" 
    try:
        desi=soup.find('span', attrs={'class': 'detailHeadline'}).text.strip()
    except:
        desi=""
    print(desi)
    try:
        desc=soup.find('div', attrs={'id': 'fp_info'}).text.strip()
    except:
        desc=""
    print(desc)
    try:
        img=soup.find('a', attrs={'class': 'prdMainPhoto'}).img["src"]
    except:
        img=""
    print(img)
    try:
        categ=soup.find('ul', attrs={'class': 'prdBreadcrumb'}).text.strip()
    except:
        categ="" 
    print(categ)
    return desi, desc, img, body, categ

def predict(desi, descr, img, clf1, scaler, inclRF, inclCNN, inclDNN):
    
    print("img:",img)
    dfcleaned=clean_manualdata(desi,descr)
    print("RF")
    #img="test2.jpg"
    df=add_features_to_manualdf(dfcleaned, img)
    #st.dataframe(df)   
    df=df.fillna(0)
    df_rf=df.drop(["prdtypecode","designation","description","productid","best_idf"], axis=1)
    #ypred_proba_RF=RF_predict(True, df_rf)
   
    weightRF=0
    ypred_proba_RF=0
    if (inclRF):
        print("RF")
        weightRF=0.73
        df_rf=scaler.transform(df_rf)
        ypred_proba_RF = clf1.predict_proba(df_rf)
        df_ypred_proba_RF = pd.DataFrame(ypred_proba_RF).T
        df_ypred_proba_RF=df_ypred_proba_RF.sort_index(axis=0)
        print (ypred_proba_RF)
    
    weightCNN=0
    ypred_proba_CNN=0
    if (inclCNN):
        print("CNN")
        weightCNN=0.54
        ypred_proba_CNN=Cnnimage_predict(img)
        df_ypred_proba_CNN = pd.DataFrame(ypred_proba_CNN).T
        df_ypred_proba_CNN = df_ypred_proba_CNN.sort_index(axis=0)
        print (ypred_proba_CNN)    
    
    weightDNN=0
    ypred_proba_DNN=0
    if (inclDNN):
        print("DNN")
        weightDNN=0.82
        ypred_proba_DNN=Dnntexte_predict(desi, descr)
        df_ypred_proba_DNN = pd.DataFrame(ypred_proba_DNN).T
        df_ypred_proba_DNN=df_ypred_proba_DNN.sort_index(axis=0)
        print (ypred_proba_DNN)
    
    print("Proba")
    ypred_proba=(ypred_proba_DNN*weightDNN+ypred_proba_RF*weightRF+ypred_proba_CNN*weightCNN)/(weightDNN+weightRF+weightCNN)
    df_ypred_proba = pd.DataFrame(ypred_proba).T
    df_ypred_proba =df_ypred_proba.sort_index(axis=0)
    print (ypred_proba)
    

    df_code = load_df_code_designation(3).sort_index(axis=0)
    if (inclRF and inclCNN and inclDNN):
        df_ypred_proba=pd.concat([df_ypred_proba,df_code,df_ypred_proba_RF,df_ypred_proba_CNN,df_ypred_proba_DNN],axis=1)
        df_ypred_proba=df_ypred_proba.drop("Unnamed: 0", axis=1)
        df_ypred_proba.columns=["Proba","classe","libellé","RF","CNN img","DNN txt"]
    elif (inclRF and inclCNN):    
        df_ypred_proba=pd.concat([df_ypred_proba,df_code,df_ypred_proba_RF,df_ypred_proba_CNN],axis=1)
        df_ypred_proba=df_ypred_proba.drop("Unnamed: 0", axis=1)
        df_ypred_proba.columns=["Proba","classe","libellé","RF","CNN img"]
    elif (inclRF and inclDNN):    
        df_ypred_proba=pd.concat([df_ypred_proba,df_code,df_ypred_proba_RF,df_ypred_proba_DNN],axis=1)
        df_ypred_proba=df_ypred_proba.drop("Unnamed: 0", axis=1)
        df_ypred_proba.columns=["Proba","classe","libellé","RF","DNN txt"]
    elif (inclCNN and inclDNN):    
        df_ypred_proba=pd.concat([df_ypred_proba,df_code,df_ypred_proba_CNN,df_ypred_proba_DNN],axis=1)
        df_ypred_proba=df_ypred_proba.drop("Unnamed: 0", axis=1)
        df_ypred_proba.columns=["Proba","classe","libellé","CNN img","DNN txt"]
    else:    
        df_ypred_proba=pd.concat([df_ypred_proba,df_code],axis=1)
        df_ypred_proba=df_ypred_proba.drop("Unnamed: 0", axis=1)
        df_ypred_proba.columns=["Proba","classe","libellé"]
        
    df_ypred_proba=df_ypred_proba.sort_values(by='Proba', ascending=False)
    df_ypred_proba=df_ypred_proba.reset_index()
    df_ypred_proba=df_ypred_proba.drop("index",axis=1)    
    #df_ypred_proba.sort()
    #print(df_ypred_proba.head(5))
    st.markdown("**Classe prédite: **"+str(int(df_ypred_proba.iloc[0,1]))+" "+str(df_ypred_proba.iloc[0,2]))
    
    
    

    if (inclRF and inclCNN and inclDNN):
        st.markdown("**Probabilités des 3 premières classes calculées par les différents modèles**")
        p = get_proba_bar(df_ypred_proba)
        st.bokeh_chart(p)
    else:
        st.markdown("**Probabilités calculées par les modèles sélectionnés**")
        df_ypred_proba = df_ypred_proba.astype({'classe': object})
        st.dataframe(df_ypred_proba.style.highlight_max(axis=0))

    st.markdown("**Analyse de l'image**")
    p = get_colors_bar(df)
    st.bokeh_chart(p)

    st.markdown("**Analyse du texte**")
    p = get_text_features_bar(df)
    st.bokeh_chart(p)

    classe_code_best_proba=int(df_ypred_proba.iloc[0,1])
    df_keywords=display_keywords_fromclasscodes(classe_code_best_proba)#,2583)
    st.markdown("**Mots-clés de la classe prédite**")
    p = get_keywords_bar(df_keywords)
    st.bokeh_chart(p)


    st.markdown("**Echantillon d'images de la classe prédite**")
    path="./echantillons/subplot_classe_" + str(int(df_ypred_proba.iloc[0,1])) +".png"
    st.image(path, width=600)


    #st.markdown("** DataFrame Features Textes & Image **")
    #st.dataframe(df)





    #st.dataframe(df_keywords)
    #st.markdown("**Classe réelle: **"+str(int(df_ypred_proba.iloc[0,1]))+" "+str(df_ypred_proba.iloc[0,2]))

#predict("bébé","","https://www.amazon.fr/Support-Perlegear-%C3%A9crans-Inclinable-orientable/dp/B01MS4N45A",clf1, scaler)

#predict("bébé","","",clf1,scaler)
#import streamlit.components.v1 as components
def app():
    file_input2=""
    #desiinit="jeu chaise longue pcs textilène noir noir"
    #descinit="cet ensemble deux chaises longues haute qualité petite table assortie idéal passer après-midi détente jardin camping chaises longues durables faciles nettoyer revêtues textilène doux confortable construites cadre acier robuste deux chaises longues d'extérieur durables résistants intempéries l'ensemble complété table assortie élégant dessus table verre lequel pouvez mettre boissons garder livre téléphone portée main cet ensemble excellent ajout espace vie extérieur couleur noir matériau chaise longue structure acier 43 siège dossier textilène dimensions chaise longue 200 58 32 cm dimensions table 30 30 295 cm hauteur dossier réglable 62/72/80/89/95 cm comprend table dessus table verre mm d'épaisseur résistance intempéries matériel polyester 30 pvc 70"
    st.title('PREDICTION')
    st.subheader("Modèles")
    chkRF=st.checkbox("Random Forest: accu=0.73%, features utilisées:regexp, nb mots/phrases, moy. couleurs ...", True)
    chkCNN=st.checkbox("CNN: accu=0.54%, feature utilisée: image de l''article", True)
    chkDNN=st.checkbox("DNN: accu=0.82%, features utilisées: désignation et description de l'article", True)
    alg = ['Aléatoire','Manuel','Site: Amazon','Site: Rakuten']
    classifier = st.selectbox('Sélection:', alg)
    if classifier=='Site: Amazon':
        st.subheader("Amazon")
        components.html('<a href="https://www.amazon.fr/gcx/Cadeaux-pour-Femmes-et-Hommes/gfhz/">Page Amazon (CTRL+click)</a>', height=25)
        url=st.text_area("URL")
        if (url != ""):
            indexref=url.find("/ref=")
            if (indexref > -1):
                url=url[:indexref]
            st.text(url)
            desi,descr,img,src,categ=getAmazon(url)
            st.text_area("Page Source", src)
            desi=st.text_area("Entrer la désignation", desi)
            descr=st.text_area('Entrer la description', descr)
            st.image(img, width=200)
            if (categ != ""):
                st.markdown("**Catégorie: ** "+categ) #TODO ajouter libellé classe
            predict(desi, descr, img, clf1,scaler,chkRF,chkCNN, chkDNN)
    elif classifier=='Site: Rakuten':
        st.subheader("Rakuten")
        components.html('<a href="https://fr.shopping.rakuten.com/event/rakuten-deals#xtatc=PUB-[fonc]-[Header]-[Rakuten-Deals]-[ToutUnivers]-[]-[]-[]">Page Rakuten (CTRL+click)</a>', height=25)
        url=st.text_area("URL")
        if (url != ""):
            indexref=url.find("?")
            if (indexref > -1):
                url=url[:indexref]
            st.text(url)
            desi,descr,img,src,categ=getRakuten(url)
            st.text_area("Page Source", src)
            desi=st.text_area("Entrer la désignation", desi)
            descr=st.text_area('Entrer la description', descr)
            st.image(img, width=200)
            if (categ != ""):
                st.markdown("**Catégorie: ** "+categ) #TODO ajouter libellé classe
            predict(desi, descr, img, clf1,scaler,chkRF,chkCNN, chkDNN)
    elif classifier=='Manuel':
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
            predict(desi, descr, img, clf1,scaler,chkRF, chkCNN, chkDNN)
            #st.markdown("**Classe réelle: **"+int(df_ypred_proba.iloc[0,0])+" "+str(ligne.iloc[0,1]))

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
        predict(desi, descr, img, clf1,scaler,chkRF,chkCNN, chkDNN)
        

        
