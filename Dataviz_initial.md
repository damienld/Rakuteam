# Présentation des premières data visualisation des données RAKUTEN

Les fichiers images (.PNG) sont disponibles [ici](https://github.com/JulienJ-44/rakuteam/tree/main/Pictures)

## Répartition des classes
Parmi les 27 classes du jeux de données, ont peut constater que:
* la classe 2583 / PISCINE & ACCESSOIRES est surreprésentée avec plus de 10 000 articles 
* 18 classes ont entre 2 000 et 5 000 articles.
* 8 classes ont moins de 2 000 articles
![Répartition des classes](https://github.com/JulienJ-44/rakuteam/blob/main/Pictures/Nb%20articles%20par%20classe.png)

## Fréquences d'unités par classes
![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/main/Pictures/Frequence_unites_par_classe.png)

On génère une heatmap pour étudier (cf. les expressions régulières de la liste suivante) le nombre d'articles contenant une des expressions de mesures suivantes:
1. **"2chiffres+"**: présence d'un nombre à au moins 2 chiffres
1. **"poids"**: présence d'une unité de poids (kg, g, ..)
1. **"longueur"**: présence d'une unité de longueur (cm,m,..)
1. **"volume"**: présence d'une unité de volume (L, cl, ..)
1. **"ans_mois"**: présence d'une valeur années/mois (ans, mois, ..)
1. **"N°"**: présence d'un N° suivi d'un nombre (N° XX..)
1. **"pourcent"**: présence d'une valeur en pourcentage
1. **"pièces**: présence d'un nombre de pièces ( XX pcs ..)

La présence est testée par la recherche des expressions régulières suivantes:
1. [0-9]{2,}
1. ([\d.]+)\s+(KG|Kg|g|kg|mg)
1. ([\d.]+)\s?(cm|mm|m|M)[\s.]
1. ([\d.]+)\s+(mL|L|ml|l|cl)[\s.]
1. ([\d.]+)\s?(an|ans|An|Ans|mois|Mois)[\s.]
1. [Nn][°]?[ ]?[\d]+
1. ([\d.]+)\s?%[\s.]
1. ([\d.]+)\s?(pc|pcs|pièces|pièce)[\s.]

*Lecture de la heatmap: 63% des articles de la classe 60 contiennent au moins un nombres à au moins 2 chiffres.*

## Part des pixels noirs et blancs des images par classe
Parmi les 27 classes du jeux de données:
* la classe 2705 / ROMAN: Livre histoire a le plus de pourcentage des pixels blancs en moyenne (~67%)
* la classe 2403 / LIVRES MAGASINES: histoire, info, musées, spirou a le moins de pourcentage des pixels blancs en moyenne (~32%)

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/main/Pictures/Pourcentage%20des%20pixels%20blancs%20sur%20les%20images.png)

et,
* la classe 2060 / LUMINAIRES, DECO et la classe 2905 / Jeux PC ont le plus de pourcentage des pixels noirs en moyenne (~1.3%)
* la classe 1301 / VETEMENTS ENFANTS/BEBE a le moins de pourcentage des pixels noirs en moyenne (~0.2%)

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/main/Pictures/Pourcentage%20des%20pixels%20noirs%20sur%20les%20images.png)

## Moyennes des couleurs R,G et B sur des images par classe

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/main/Pictures/Moyenne%20de%20valeur%20R%20sur%20les%20images.png)

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/main/Pictures/Moyenne%20de%20valeur%20G%20sur%20les%20images.png)

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/main/Pictures/Moyenne%20de%20valeur%20B%20sur%20les%20images.png)

## Affichage d'un échantillon de 20 images par classes par éléments croissants


**Classe: 2583-
 10209  éléments-
PISCINE: piscine et accessoires**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/main/Pictures/subplot_classe_2583.png)

**Classe: 1560- 
 5073  éléments-
MAISON: cusine, fournitures, mobiliers, rangement**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_1560.png)

**Classe: 1300-
 5045  éléments-
JEUX MINIATURES, radio commandés: drone, maquettes, voitures miniatures**            

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_1300.png)

**Classe: 2060- 
 4993  éléments-
LUMINAIRES, DECO**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_2060.png)

**Classe: 2522 -
 4989  éléments-
FOURNITURE de BUREAU: cahiers, carnets**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_2522.png)

**Classe: 1280 -
 4870  éléments-
JOUETS ENFANTS: peluche, puzzle, DIY**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_1280.png)

**Classe: 2403 -
 4774  éléments-
LIVRES MAGASINES: histoire, info, musées, spirou**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_2403.png)

**Classe: 2280 -
 4760  éléments-
MAGASINES/REVUES d'ARTS et SPECTACLES**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_2280.png)

**Classe: 1920 -
 4303  éléments-
LITERIE, TEXTILE MAISON: eqipements intérieur, coussin, housse**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_1920.png)

**Classe: 1160 (10)-
 3953  éléments-
CARTES collection: cartes pokemon**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_1160.png)

**Classe: 1320 -
 3241  éléments-
BEBES accessoires**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_1320.png)

**Classe: 10 -
 3116  éléments-
LITTERATURE/ROMANS: livres d occasions?? [à vérifier, regarder "description"]**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_10.png)

**Classe: 2705 -
 2761  éléments-
ROMAN: livre histoire?**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_2705.png)

**Classe: 1140 -
 2671  éléments-
FIGURINES/MANGAS/UNIVERS FANTASTIQUES**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_1140.png)

**Classe: 2582 -
 2589  éléments-
MOBILIER extérieur et accessoires extérieur maison**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_2582.png)

**Classe: 40 -
 2508  éléments-
JEUX VIDEOS: import slmt?**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_40.png)

**Classe: 2585 -
 2496  éléments-
OUTILS JARDINS**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_2585.png)

**Classe: 1302 -
 2491  éléments-
LOISIRS/EQUIPEMENT extérieur: camping, pêche, trampo**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_1302.png)

**Classe: 1281 -
 2070  éléments-
JEUX EDUCATIFS ENFANTS, jeux de cartes**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_1281.png)

**Classe: 50  (20)-
 1681  éléments-
Acessoires pour JEUX VIDEOS! et consoles??(non-portable) [à vérifier ]**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_50.png)

**Classe: 2462 -
 1421  éléments-
JEUX VIDEOS OCASSIONS (Acessoires/jeux par LOT! pour JEUX VIDEOS)**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_2462.png)

**Classe: 2905 -
 872  éléments-
Jeux PC (en TELECHARGEMENT ou pas)**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_2905.png)

**Classe: 60 -
 832  éléments-
CONSOLES de jeux**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_60.png)

**Classe: 2220 -
 824  éléments-
Accessoires ANIMAUX domestiques**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_2220.png)

**Classe: 1301 -
 807  éléments-
VETEMENTS ENFANTS/BEBE: (billard???, babyfoot???)**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_1301.png)

**Classe: 1940 -
 803  éléments-
ALIMENTATIONS, CONFISERIES, CAFE**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_1940.png)

**Classe: 1180 -
 803  éléments-
JEUX DE GUERRE sur TABLE**

![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/mainPictures/subplot_classe_1180.png)



