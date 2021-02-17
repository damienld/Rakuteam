# Présentation des premières data visualisation des données RAKUTEN

Les fichiers images (.PNG) sont disponibles [ici](https://github.com/JulienJ-44/rakuteam/tree/main/Pictures)

## Répartition des classes
Parmi les 27 classes du jeux de données, ont peut constater que:
* la classe 2583 / PISCINE & ACCESSOIRES est surreprésentée avec plus de 10 000 articles 
* 18 classes ont entre 2000 et 5 000 articles.
* 8 classes ont moins de 2000 articles
![Répartition des classes](https://github.com/JulienJ-44/rakuteam/blob/main/Pictures/Nb%20articles%20par%20classe.png)

## Fréquences d'unités par classes
![Voir l'image](https://github.com/JulienJ-44/rakuteam/blob/main/Pictures/Frequence_unites_par_classe.png)

On génère une heatmap pour étudier (cf. les expressions régulières de la liste suivante) le nombre d'articles contenant une des expressions de mesures suivantes:
1. **"2chiffres+"**: présence d'un nombre à au moins 2 chiffres
1. **"poids"**: présence d'une unité de poids (kg, g, ..)
1. **"longueur"**: présence d'une unité de longueur (cm,m,..)
1. **"dimension"**: présence d'une valeur de dimension sous la forme [nombre1] x [nombre 2]
1. **"volume"**: présence d'une unité de volume (L, cl, ..)
1. **"ans"**: présence d'une valeur années (an, ans, ..)
1. **"N°"**: présence d'un N° suivi d'un nombre (N° XX..)

La présence est testée par la recherche des expressions régulières suivantes:
1. [0-9]{2,}
1. ([\d.]+)\s+(KG|Kg|g|kg|mg)
1. ([\d.]+)\s+(cm|mm|m|M)
1. ([\d.]+)\s+[xX]\s+[\d.]+
1. ([\d.]+)\s+(mL|L|ml|l|cl)
1. ([\d.]+)\s+(an|ans)
1. [Nn][°]?[ ]?[\d]+

*Lecture de la heatmap: 63% des articles de la classe 60 contiennent au moins un nombres à au moins 2 chiffres.*
