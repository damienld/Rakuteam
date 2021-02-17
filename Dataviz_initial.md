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

## Affichage 20 image des différentes classes
**Classe: 40 
2508  éléments
JEUX VIDEOS: import slmt?**



