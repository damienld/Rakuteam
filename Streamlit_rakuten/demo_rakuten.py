import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st

#app.py
import app1
import app2
import app3
import app4

# General formating in CSS
page_bg_img = '''
   <style>
    section{
        background-color:#4db3e9;
    color: #fff
    }
                       
   h1 {
   	color:#ffa04a
   	
   }
   
   h2 {
   
   color : #000000
   	
   }
   
   h3 {
   
   color : #ffa04a
   	
   }
   
   label {
   color: #fff;
   
   ;
   }
   

   </style>
   '''
st.markdown(page_bg_img, unsafe_allow_html=True)

PAGES = {
    "Présentation du projet": app4,
    "Exploration des données": app3,
    "Modélisation": app2,
    "Notre démo": app1
}

# st.sidebar.title('Classification d\'articles de e-commerce')


 ## hide streamlit menu since it doesn’t really serve any purpose to the user, so there’s no reason the user should see it
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>   
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)   

# Activate sidebar functions
st.sidebar.header("Analyse de données (texte et image) d'un site de e-commerce")
st.sidebar.header("Menu")



selection = st.sidebar.radio("",list(PAGES.keys()))
page = PAGES[selection]
page.app()

st.sidebar.info("""
                    Projet DS - Promotion Bootcamp Janvier 2020

    Participants:
        
    Aylin KAYA https://www.linkedin.com/in/alexis-teskrat-a879a7195/ 
    
    Damien LE DIRACH https://www.linkedin.com/in/f%C3%A9lix-peyre-8997b940/
    
    Julien JUHEL https://www.linkedin.com/in/robin-biron-48448282/

    Manh NGUYEN
                    
                    """)

