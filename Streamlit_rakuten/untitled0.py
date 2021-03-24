# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:47:38 2021

@author: Lenovo
"""

from modelisation import *
from sample import *

df_code = load_df_code_designation(1)

# print(df_code.head())

# print(df_code)

alg = list(df_code['désignation'])
desi_classe = st.selectbox('Selection de la classe', alg)

alg_1 = list(range(1,11,1))
nb_article = st.selectbox("Nombre d'articles à afficher", alg_1) 


# if st.button("Chercher"):
code_classe_1 = df_code[df_code['désignation']==desi_classe]
code_classe = code_classe_1.index #['prdtypecode']
    
st.text(print('désignation classe: ', desi_classe))
st.text(print('code classe: ',code_classe))
st.text(print('nb article: ', nb_article))
   
 



# export = get_random_article(code_classe, nb_article)

# st.dataframe(export)