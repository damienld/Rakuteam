# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 01:45:08 2021

@author: slam_
"""

# app1.py
import streamlit as st

def app():
    st.title('PREDICTION')
    st.write('Selection du modèle')
    
    # creating a file uploader 
    file_input = st.file_uploader(label='Please upload a photo:') 
    if file_input is not None: 
     # reading the content of the file 
     file_bytes = file_input.read() 
     # displaying the text 
     st.success('Successfully reading the file:') 
     st.text(file_bytes)
     