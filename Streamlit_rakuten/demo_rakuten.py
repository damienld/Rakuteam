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
    section{
        background: #318CE7;        
        color: #fff;
    }
                       
   h1 {
   	
      color:#ffa04a ;
   	
   }



   .css-hi6a2p {
       max-width: 830px;
       }
   
   h2 {
   
       color: #fff;
       

   	
   }

   .bk{
        border-radius: 15px;
        border: solid 1px black; 
        
   }

   .bk.bk-canvas-underlays{
       background: rgba(0, 0, 255, 1);
   }


   img {
    #    width: 50%;
       margin: auto;
       border-radius: 15px;
       border: solid 1px black;

   }
   
   h3 {
   
   color : #ffa04a;
   	
   }
   
    div>div>label {
        color: #fff;
   }

   .st-c0{
       color: #fff;

   }

   .st-ch{
       color: #fff;

   }

   div .css-1l02zno {
       background: #1F618D;
       border-right: solid 3px #ffa04a
       
       
   }

   .css-xq1lnh-EmotionIconBase {
    color: white;
    fill: currentcolor;
    font-size: 0.9rem;
}

    .st-e3 {
        fill: black;
    }


   .st-dd {
    margin: auto;
    color: black;
    font-style: italic;
    font-weight: bold;
    font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    
   }

   .st-ex{
    margin: auto;
    color: black;
    font-style: italic;
    font-weight: bold;
    font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    
   }

   

#     .st-ax{
#     margin: auto;
#     color: black;
#     font-style: italic;
#     font-weight: bold;
#     font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    
#    }


   
   .stAlert{
       background: #cf3;
       border: solid 1px green;
       border-radius: 15px;

   }

   pre{
       padding: 8px;
       border-radius: 10px;
       margin: 50px;
    #    background: #7d828a;
       background: #686d75;
       color: white;
       font-weight: bold;

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
st.sidebar.header("Items classifier")
st.sidebar.header("Menu")



selection = st.sidebar.radio("",list(PAGES.keys()))
page = PAGES[selection]
page.app()

st.sidebar.info("""
                    Projet DS - Promotion Bootcamp Janvier 2020

    Participants:
        
    Aylin KAYA https://www.linkedin.com/in/alexis-teskrat-a879a7195/ 
    
    Damien LE DIRACH https://www.linkedin.com/in/dld-76/
    
    Julien JUHEL https://www.linkedin.com/in/julien-juhel/

    Manh NGUYEN
                    
                    """)

