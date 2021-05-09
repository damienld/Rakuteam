import streamlit as st

def app():

    st.title("**Présentation du jeu de données**")
    st.write("""Nous avons utilisé les données transmises par Rakuten France, constitué d'une liste d’environ 99K produits, 
    comprenant l’ensemble d’entraînement (84 916 articles) et l'ensemble de test (13 812 articles).""")
    st.subheader("**Fichier d'entrées (entrainement et test)**")
    path="./présentation/Pres_dataset_"
    st.image(path+"texte.jpg")
    st.write("En outre, nous disposions d’un fichier images.zip contenant les images associées à tous les articles.")
    st.image(path+"image.jpg")
    st.subheader("**Fichier de sorties d'entraînement**")
    st.write("""Enfin, dans le fichier y_train, on retrouve la classe associée à chaque produit:""")
    st.image(path+"sorties.jpg")