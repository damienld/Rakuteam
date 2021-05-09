
import streamlit as st

def app():
    path="./présentation/"

    st.title('Présentation des modèles sélectionnés')
    st.subheader('**Machine learning**')
   

    texte_ml = """
                <div>Pour la suite, nos modèles devant exploiter à la fois les textes et les images, nous avons choisi de créer des features construites sur:</div>
                <ul>
                    <li><div style="font-weight: bold">la partie texte:</div>
                        <ul>
                            <li>dénombrement de certaines expressions régulières</li>
                            <li>scoring TF-IDF de chaque classe</li>
                            <li>nombre de mots, phrases, caractères spéciaux, majuscules, symboles...</li>
                        </ul>
                    </li>
                    <li><div style="font-weight: bold">la partie image:</div>
                        <ul>
                            <li>moyenne des pixels en canal de couleur R</li>
                            <li>moyenne des pixels en canal de couleur G</li>
                            <li>moyenne des pixels en canal de couleur B</li>
                            <li>pourcentage de pixel Noir</li>
                            <li>pourcentage de pixel Blanc</li>
                        </ul>
                    </li>
                </ul>
"""

    st.markdown(texte_ml,  unsafe_allow_html=True)

    st.write("TODO: traduire commentaires => The original dataset is separated into a training set containing features (X_train) and labels (y_train) and a test set (X_test and y_test).")
    code_ml = """
        <xmp>
            
                from sklearn.model_selection import train_test_split

                df =df.dropna(subset=['prdtypecode_x'])
                y = df['prdtypecode_x'].values
                df =df.drop('prdtypecode_x', axis=1)
                X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=123)
            
        </xmp>
    """
    st.markdown(code_ml,  unsafe_allow_html=True)
    st.write("")
    st.write("TODO ajouter commentaire.")
    code_ml = """
        <xmp>

                from sklearn.preprocessing import StandardScaler

                scaler = StandardScaler().fit(X_train)
                X_train  = scaler.transform(X_train)
                X_test = scaler.transform(X_test)
        </xmp>
    """
    st.markdown(code_ml,  unsafe_allow_html=True)
    st.write("")
    st.write("TODO ajouter commentaire.")
    code_ml = """
    <xmp>

                from sklearn.ensemble import RandomForestClassifier

                clf1 = RandomForestClassifier(max_features ='sqrt', n_jobs = -1,n_estimators = 500)
                clf1.fit(X_train, y_train)

                y_pred = clf1.predict(X_test)
    </xmp>
    """
    st.markdown(code_ml,  unsafe_allow_html=True)

    st.subheader('**Architecture CNN pour l’analyse des images:**')
    st.markdown("Pour optimiser l'analyse des images, nous avons retenu le modèle construit avec l'architecture ci-dessous:")
    st.image(path+"cnn_images.jpg", width=950)
    st.markdown('Ce modèle a permis d’obtenir une **validation accuracy de 58%**')
    

    st.subheader('**Architecture DNN pour l’analyse du texte**')
    # st.markdown("""Après plusieurs essais, pour la partie texte nous avons selectionné le modèle le plus performant 
    # qui est basé sur le prétraitement et le réseau de neurones suivant:  """)
    st.markdown(""" Pour la partie texte, nous avons d'abord appliqué une méthode de tokenization, puis nous avons construit un dictionnaire 
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
    st.markdown("""Afin de traiter à la fois la partie texte et la partie image nous avons décidé d’exploiter au mieux les spécificités 
    des différents modèles définis ci-dessus, par le biais d’un système de vote.Pour cela nous nous sommes inspirés du Voting Classifier 
    de la bibliothèque scikit-learn qui permet de combiner plusieurs estimateurs de Machine Learning conceptuellement différents.""")
    st.markdown("""Plus précisément,  sur l’ensemble des articles, chaque modèle retourne une probabilité pour chaque classe, et la moyenne des probabilités
     est calculée pour prédire la classe finale. De plus, nous avons appliqué une pondération à chaque estimateur afin de moduler le poids 
     de chacun des trois modèles (RF, CNN, DNN) selon son accuracy.""")
    st.markdown("""En appliquant ce modèle nous avons atteint une **validation accuracy de 84%, qui est supérieure à l’accuracy 
    obtenue par chacun des modèles pris séparément.**""")
    # path="./présentation/global.jpg"
    st.image(path+"global.jpg", width=950)

   
