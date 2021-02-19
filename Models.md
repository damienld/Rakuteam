# Modèles

## Modèle best_tf_idf 

### Présentation
Après avoir calculé le tf_idf de chaque mot par rapport à chaque classe, nous créons un score pour estimer l'appartenance d'un article à chacune des classes.
Ce score est calculé de la manière suivante:
- pour chaque classe on conserve les 15 mots avec le meilleur tf_idf
- pour chaque article on calcule les 27 scores (pour chacune des 27 classes)
- le score est l'addition du nombre d'occurences du mot clé (parmi la liste des 15) multiplié par son nombre d'occurences dans la **désignation** de l'article
- dans le cas où tous les scores sont nuls, on affecte l'article à la classe majoritaire: 2583
### Exemple: 
Les meilleurs mots clés (15 meilleurs tf_idf) de la classe 1940 sont:
- bio 0.473
- café 0.223
- ...
La description de l'article est: "Article bio. Ceci est un café bio."

=> Le score appelé "class_1940" pour cet article est: 0.473x2 + 0.223

### Résultats du modèle
#### Scores par classe
       precision    recall  f1-score   support

          10       0.24      0.11      0.15      3116
          40       0.38      0.32      0.35      2508
          50       0.52      0.41      0.46      1681
          60       0.31      0.80      0.45       832
        1140       0.61      0.52      0.56      2671
        1160       0.43      0.65      0.52      3953
        1180       0.37      0.33      0.35       764
        1280       0.54      0.31      0.40      4870
        1281       0.28      0.18      0.22      2070
        1300       0.62      0.77      0.68      5045
        1301       0.35      0.57      0.44       807
        1302       0.84      0.42      0.56      2491
        1320       0.38      0.40      0.39      3241
        1560       0.57      0.41      0.48      5073
        1920       0.79      0.73      0.76      4303
        1940       0.17      0.39      0.24       803
        2060       0.66      0.52      0.58      4993
        2220       0.31      0.66      0.42       824
        2280       0.37      0.47      0.41      4760
        2403       0.44      0.48      0.46      4774
        2462       0.63      0.47      0.54      1421
        2522       0.51      0.29      0.37      4989
        2582       0.27      0.36      0.31      2589
        2583       0.53      0.68      0.60     10209
        2585       0.38      0.28      0.32      2496
        2705       0.25      0.14      0.18      2761
        2905       0.35      0.99      0.52       872
	accuracy                           0.48     84916
	macro avg       0.45      0.47      0.43     84916
	weighted avg    0.49      0.48      0.47     84916

#### Heatmap de la matrice de confusion

![Heatmap](https://github.com/JulienJ-44/rakuteam/blob/main/Models/Heatmap_best_tfidf.png)