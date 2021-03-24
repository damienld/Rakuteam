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


import cv2
import numpy as np
import streamlit as st

#df=clean_manualdata("bébé","")
#df=add_features_to_manualdf(df)

#Textbox for text user is entering
#st.subheader("Entrer la description.")
#st.long_text_input("Entrer la désignation.")

#text = st.text_input('Enter text') #text is stored in this variable

#add_imgfeatures(df, file_bytes)



#uploaded_file = st.file_uploader("Choose a image file", type="jpg")




def app():
    st.title('PREDICTION')
    st.subheader("Entrée manuelle")
    

    descr = st.text_input('Entrer la description') #description is stored in this variable
    #text_des = st.long_text_input(num_lines=3)
    #text_des = st.text_area()
    
    desi = st.text_input("Entrer la désignation")#designation is stored in this variable
    #for n in range(1):
    #    desi.append(st.text_input(label='', key=f'Texts {n}'))
    
    # creating a file uploader 
    file_input = st.file_uploader("Choose a image file", type="jpg")
    if file_input is not None: 
        # Convert the file to an opencv image.
        file_bytes = np.asarray(bytearray(file_input.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
    
        # Afficher l'image:
        st.image(opencv_image, channels="BGR")
        
        df=clean_manualdata(descr,desi)
        df=add_features_to_manualdf(df,file_input)
        #img="test2.jpg"
        add_imgfeatures(df, file_input)
        
        st.dataframe(df)
        

     