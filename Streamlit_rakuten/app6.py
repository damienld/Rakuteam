
import streamlit as st

def app():
    path="./présentation/"

    st.title('Présentation des modèles sélectionnés')
    st.subheader('**Machine learning**')
    st.markdown("""Pour la suite, nos modèles devant exploiter à la fois les textes et les images, nous avons choisi de créer des features construites sur  
    * la partie texte:  
    * dénombrement de certaines expressions régulières
Scoring TF-IDF de chaque classe
Nombre de mots, phrases, caractères spéciaux, majuscules, symboles...
la partie image:
moyenne des pixels en canal de couleur R 
moyenne des pixels en canal de couleur G
moyenne des pixels en canal de couleur  B
pourcentage de pixel Noir
pourcentage de pixel  Blanc
""")



    st.subheader('**Architecture CNN pour l’analyse des images:**')
    st.markdown("Pour optimiser l'analyse des images, nous avons retenu le modèle construit avec l'architecture ci-dessous:")
    st.image(path+"cnn_images.jpg", width=950)
    st.markdown('Ce modèle a permis d’obtenir une **validation accuracy de 58%**')
    

    st.subheader('**Architecture DNN pour l’analyse du texte**')
    st.markdown("""Après plusieurs essais, pour la partie texte nous avons selectionné le modèle le plus performant 
    qui est basé sur le prétraitement et le réseau de neurones suivant:  """)
    st.markdown(""" D'abord nous avons utilisé une méthode de tokenization, et de construction d’un dictionnaire 
    basé sur le corpus des champs description et désignation de l’ensemble des articles.""") 
    st.markdown("""Avec cette méthode, nous classons par ordre de fréquence décroissante les 20 000 mots les plus importants du corpus, 
    chaque mot étant remplacé par son index au sein du dictionnaire. Tous les articles n’ayant pas le même nombre de mots, 
    nous complétons avec des zéros les emplacements vides jusqu’à l’équivalent de 400 mots.""")
    st.markdown("""A partir des index de chaque mot, nous avons appliqué une couche d’Embedding de Keras qui crée un vecteur dense de dimension 100 associé à chaque mot.""")
    st.markdown("""L’utilisation d’une couche de Flatten nous permet de transformer la matrice 400*100 
    (sortie de la couche d’embedding) en un vecteur (longueur 40 000) afin d’alimenter la 1ère couche dense. 
    Suite à cela nous appliquons une couche de dropout, et pour finir une couche dense de sortie composée de 27 neurones correspondant 
    au nombre de catégories dans lesquelles nous devons classer les articles.""")
    st.image(path+"dnn_textes.jpg", width=950)
    st.markdown('Ce modèle a permis d’obtenir une **validation accuracy de 82.5%**')


    st.subheader('**Architecture globale**')
    st.markdown("""  test  """)
    # path="./présentation/global.jpg"
    st.image(path+"global.jpg", width=950)

   
