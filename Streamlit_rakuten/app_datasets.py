import streamlit as st
import constants
def app():

    st.title("**Présentation du jeu de données**")
    st.write("""Nous avons utilisé les données transmises par Rakuten France, constitué d'une liste d’environ 99K produits, 
    comprenant l’ensemble d’entraînement (84 916 articles) et l'ensemble de test (13 812 articles).""")
    st.subheader("**Fichier d'entrées (entrainement et test)**")
    path=constants.path+"presentation/Pres_dataset_"
    st.image(constants.path+"presentation/Pres_dataset_texte.JPG")
    st.write("En outre, nous disposions d’un fichier images.zip contenant les images associées à tous les articles.")
    st.image(path+"image.JPG")
    st.subheader("**Fichier de sorties d'entraînement**")
    st.write("""Enfin, dans le fichier y_train, on retrouve la classe associée à chaque produit:""")
    st.image(path+"sorties.JPG")