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

## Modèle GradientBoostingClassifier 

### Présentation
Paramètres par défauts

### Résultats du modèle
#### Scores par classe
     precision    recall  f1-score   support

          10       0.45      0.56      0.50       615
          40       0.65      0.60      0.62       490
          50       0.73      0.58      0.65       348
          60       0.92      0.83      0.87       159
        1140       0.66      0.65      0.65       529
        1160       0.81      0.85      0.83       782
        1180       0.71      0.45      0.55       159
        1280       0.65      0.62      0.63      1033
        1281       0.46      0.37      0.41       387
        1300       0.88      0.87      0.87      1047
        1301       0.85      0.66      0.74       185
        1302       0.77      0.58      0.66       485
        1320       0.61      0.50      0.55       669
        1560       0.59      0.70      0.64      1007
        1920       0.85      0.82      0.84       849
        1940       0.68      0.68      0.68       146
        2060       0.70      0.69      0.69      1044
        2220       0.75      0.68      0.71       147
        2280       0.70      0.76      0.73       958
        2403       0.68      0.74      0.71       928
        2462       0.78      0.73      0.76       279
        2522       0.67      0.73      0.70       978
        2582       0.64      0.55      0.59       510
        2583       0.84      0.90      0.87      2018
        2585       0.78      0.55      0.65       502
        2705       0.69      0.83      0.75       549
        2905       0.99      0.99      0.99       181

    accuracy                           0.72     16984
    macro avg       0.72      0.69      0.70     16984
    weighted avg    0.72      0.72      0.71     16984

Classes prédites  10    40    50    60    1140  ...  2582  2583  2585  2705  2905
Classes réelles                                 ...                              

#### Heatmap de la matrice de confusion
![Heatmap](https://github.com/JulienJ-44/rakuteam/blob/main/Pictures/Heatmap%20Gradient%20Boosting%20Classifier.png)
## Modèle SVM Classifier 

### Présentation
Modèle svm.SVC avec paramètres par défauts

### Résultats du modèle
#### Scores par classe
precision    recall  f1-score   support

          10       0.32      0.55      0.40       643
          40       0.66      0.45      0.54       508
          50       0.74      0.62      0.68       370
          60       0.99      0.81      0.89       167
        1140       0.69      0.60      0.64       525
        1160       0.73      0.83      0.78       825
        1180       0.52      0.48      0.50       136
        1280       0.54      0.60      0.57       950
        1281       0.50      0.31      0.38       405
        1300       0.89      0.83      0.86      1043
        1301       0.93      0.56      0.70       177
        1302       0.83      0.56      0.67       460
        1320       0.56      0.48      0.52       653
        1560       0.61      0.71      0.65      1051
        1920       0.88      0.82      0.85       841
        1940       0.72      0.51      0.60       167
        2060       0.70      0.68      0.69       984
        2220       0.79      0.68      0.73       146
        2280       0.66      0.74      0.70       949
        2403       0.67      0.65      0.66       961
        2462       0.76      0.70      0.73       286
        2522       0.63      0.69      0.66       972
        2582       0.68      0.49      0.57       529
        2583       0.80      0.89      0.84      2023
        2585       0.85      0.53      0.65       485
        2705       0.62      0.70      0.66       567
        2905       1.00      0.98      0.99       161

    accuracy                           0.68     16984
    macro avg       0.71      0.65      0.67     16984
    weighted avg    0.70      0.68      0.68     16984

#### Heatmap de la matrice de confusion
![Heatmap](https://github.com/JulienJ-44/rakuteam/blob/main/Pictures/Heatmap%20SVM%20Classifier.png)

