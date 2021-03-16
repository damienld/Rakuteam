# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:56:04 2021

@author: Lenovo
"""

import matplotlib.pyplot as plt
%matplotlib inline 
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing

#*****************************************************************************

#Création d'une Heatmap de la fréquence d'occurence des caractères spéciaux et des symboles dans les champs designation et déscription

#Création dictionnaire de correspondance entre code et désignation des classes
tab_designation = {2583:'PISCINE & ACCESSOIRES',1560:'MAISON: cusine, mobiliers',1300:'JOUETS RADIO COMMANDES'
,2060:'LUMINAIRES, DECO',2522:'FOURNITURE de BUREAU',1280:'JOUETS ENFANTS',2403:'LIVRES & MAGASINES: histoire, musées'
,2280:"REVUES d'ARTS et SPECTACLES",1920:"LITERIE, TEXTILE MAISON",1160:"CARTES à COLLECTIONNER",
1320:"ACCESSOIRES BEBES",10:"LITTERATURE/ROMANS (occasions?)",2705:"ROMAN: livre histoire?",1140:"FIGURINES MANGAS"
,2582:"MOBILIER & ACCESSOIRES extérieur",40:"JEUX VIDEOS (import?)",2585:"OUTILS JARDINS",1302:"LOISIRS/EQUIPEMENT extérieur"
,1281:"JEUX EDUCATIFS ENFANTS",50:"ACCESSOIRES CONSOLES de JEUX",2462:"JEUX VIDEOS OCCASIONS",2905:"JEUX PC",
60:"CONSOLES de JEUX",2220: "ACCESSOIRES ANIMAUX",1301:"VETEMENTS ENFANTS/BEBE",1940:"ALIMENTATIONS, CONFISERIES, CAFE",1180:"JEUX DE GUERRE sur TABLE"}

classes_codes=sorted(classes_codes)
#on étudie le champ description
colonneClass = "description" 
df_results = pd.DataFrame(columns=['2chiffres+','poids','longueur','volume','ans_mois','N°','pourcent','pièces'])#, 'date','octets','dimension'

class_text_cols = []
#on parcourt la liste des classes
for class_code in classes_codes:
  #on copie dans un df temporaire les lignes correspondant au code de classe actuel
  df_current_class = df[df["prdtypecode"]==class_code]
  #affichage des infos de la classe
  #print("Classe:", class_code, "\n", len(df_current_class.index), " éléments")
  nb_total = len(df_current_class.index)
  #nb d articles contenant la regexp / nb d articles total dans la classe
  nb_occur1=(len(df_current_class[df_current_class["desc_nb2chiffres+"] > 0]))/nb_total
  nb_occur4=(len(df_current_class[df_current_class["desc_poids"] > 0]))/nb_total
  nb_occur5=(len(df_current_class[df_current_class["desc_long"] > 0]))/nb_total
  nb_occur7=(len(df_current_class[df_current_class["desc_vol"] > 0]))/nb_total
  #nb_occur2=(len(df_current_class[df_current_class["desc_Go"] > 0]))/nb_total
  nb_occur3=(len(df_current_class[df_current_class["desc_num"] > 0]))/nb_total
  nb_occur12=(len(df_current_class[df_current_class["desi_num"] > 0]))/nb_total
  nb_occur8=(len(df_current_class[df_current_class["desc_ans_mois"] > 0]))/nb_total
  nb_occur9=(len(df_current_class[df_current_class["desc_pieces"] > 0]))/nb_total
  nb_occur11=(len(df_current_class[df_current_class["desc_pourcent"] > 0]))/nb_total
  new_row = pd.Series(data={'2chiffres+':nb_occur1,
                            #,'dimension':nb_occur6, 'date':nb_occur10 'octets':nb_occur2,
                            'poids':nb_occur4,'longueur':nb_occur5,'volume':nb_occur7
                            ,'ans_mois':nb_occur8,'N°(desi)':nb_occur12,'N°':nb_occur3,'pièces':nb_occur9,'pourcent':nb_occur11}
                      , name=str(class_code)+ "-"+tab_designation[class_code])
  df_results = df_results.append(new_row, ignore_index=False)


plt.figure(figsize=(25,12))
sns.heatmap(df_results, annot=True, cmap='YlGnBu');
p = plt.title("Fréquences des différences unités de mesures au sein de chacune des classes");
images_dir = '/Drive/My Drive/Colab Notebooks'
plt.savefig(f"{images_dir}/Frequence_unites_par_classe.png")