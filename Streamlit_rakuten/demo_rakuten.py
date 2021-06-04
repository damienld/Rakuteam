import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st

#app.py
import app1
import app2
import app3
import app4
import app6
import app7

# General formating in CSS
page_bg_img = '''
   <style>

   .main {
       background: #318CE7; 
       font-family:'Franklin Gothic Medium';
   }

    h1, strong {
   
        color:#ffa04a ; 
    }   

    .stAlert {
        background: #cf3;
        color: green;
        border: solid 1px green;
        border-radius: 15px;
    }

     .stAlert div p {
        
        color: green;
      
    }

    .main p, li {
        color: #fff;
    }

    .main div {
        color: #fff;
    }

    .main label {
        color: #fff;
    }

    .element-container {
        color: #fff;
        font-weight: bold;
        font-size: 1.2 em;
    }
    
    pre{
        padding: 8px;
        border-radius: 10px;
        margin: 50px;
        background: #7d828a;
        color: white;
        font-weight: bold;
    }

    .stSelectbox div {
        color: black;
    }

    img {
        #width: 50%;
        margin: auto;
        border-radius: 15px;
        border: solid 1px black;
    }

    .bk{
        border-radius: 15px;
        border: solid 1px black;  
    }

   </style>
   '''
st.markdown(page_bg_img, unsafe_allow_html=True)

PAGES = {
    "Présentation du projet": app4,
    "Datasets": app7,
    "Analyse exploratoire": app3,
    "Démarche": app6,
    "Modélisation": app2,
    "Notre démo": app1
}

# st.sidebar.title('Classification d\'articles de e-commerce')


 ## hide streamlit menu since it doesn’t really serve any purpose to the user, so there’s no reason the user should see it
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
# .css-15uahz3.ehezqtx2 {visibility: hidden;}
</style>   
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)   

# Activate sidebar functions
#st.sidebar.header("Items classifier")
st.sidebar.header("Menu")



selection = st.sidebar.radio("",list(PAGES.keys()))
page = PAGES[selection]
page.app()

st.sidebar.info("""
                    Projet DS - Promotion Bootcamp Janvier 2021

    Participants:
        
    Aylin KAYA https://www.linkedin.com/in/ay%C5%9Fe-aylin-kaya-11805441/
    
    Damien LE DIRACH https://www.linkedin.com/in/dld-76/
    
    Julien JUHEL https://www.linkedin.com/in/julien-juhel/

    Manh NGUYEN https://www.linkedin.com/in/manh-nguyen-86651b90/
                    
                    """)

