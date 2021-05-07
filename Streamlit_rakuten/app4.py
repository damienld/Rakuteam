# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 09:24:15 2021

@author: slam_
"""


import streamlit as st
     
# app3.py
def app():
    st.title("Contexte et objectifs")
    st.write("""La mise en catalogue de listes de produits via la catégorisation des titres et des images, 
    est un problème fondamental pour toute place de marché électronique, avec des applications allant 
    de la recherche et recommandations personnalisées, à la compréhension des requêtes. """)
    st.write("""Dans le cadre d’un challenge organisé par l'ENS et de notre formation data scientist au sein de DataScientest,
     nous avons pu travailler sur la classification de produits à grande échelle, en développant un projet visant à prédire le type 
     de chaque produit tel que défini dans le catalogue de Rakuten France.""")
    st.write("""Sachant que les progrès dans ce domaine de recherche ont été limités en raison du manque de données disponibles, 
    le fait que la société Rakuten propose un set de données exploitable a constitué une vraie opportunité.""")
    # st.write("Ce projet nous a immédiatement intéressé car il permet de mettre en oeuvre de nombreux concepts de data science, tels que la manipulation de textes et d'images, la réduction de dimensions, l'utilisation de modèles de machine learning et de deep learning, ou encore le traitement de la nature bruyante des étiquettes et des images des produits. De cette manière nous avons pu concrètement expérimenter l'importance ainsi que l'impact de toutes ces étapes et méthodes liées à un projet de data science.")
    st.markdown("**Pour résumer, nos objectifs lors de ce projet étaient:**"
                "\n\n"
                "•  entraîner différents modèles de machine et deep learning afin de classer parmi les différentes catégories les articles du jeu d' entraînement."
                "\n\n"
                "•  construire une méthode exploitant les modèles les plus performants."
                "\n\n"
                "•  appliquer la méthode développée sur l’ensemble de test fourni par Rakuten afin de  valider la généralisation du modèle."
                "\n\n"
                "•  développer une application permettant de classer en direct tout nouvel article proposé.")






# 
# "
   