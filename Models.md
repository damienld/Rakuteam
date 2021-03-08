# Modèles
## Récapitulatif

 | Modèle           |     Paramètres    |   Accuracy  |
 | -----------------|:----------------: | :---------: |
 | Best_tfidf       |                   |    **0.48** |
 | GradientBoosting |                   |    **0.72** |
 | SVM              |                   |    **0.68** |
 | Rég. Log.        | *liblinear*       |    **0.55** |
 | Random Forest    |                   |    **0.77** |
 | Voting - Soft    | *rf, lr, knn*     |    **0.75** |
 | Voting - Hard    | *rf, lr, knn*     |    **0.77** |
 | KNN		    | *k = 3*		|    **0.65** |
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


## Modèle Régression Logistique

### Présentation
linear_model.LogisticRegression(random_state = 0, solver = 'liblinear', multi_class = 'auto')

### Résultats du modèle
#### Scores par classe
       precision    recall  f1-score   support

          10       0.25      0.35      0.29       623
          40       0.52      0.32      0.39       502
          50       0.75      0.28      0.41       336
          60       0.93      0.72      0.81       166
        1140       0.69      0.48      0.57       534
        1160       0.59      0.75      0.66       791
        1180       0.93      0.08      0.16       153
        1280       0.53      0.49      0.51       974
        1281       0.55      0.09      0.16       414
        1300       0.82      0.77      0.79      1009
        1301       0.90      0.50      0.64       161
        1302       0.82      0.36      0.50       498
        1320       0.83      0.09      0.16       648
        1560       0.39      0.37      0.38      1015
        1920       0.80      0.78      0.79       861
        1940       0.68      0.42      0.52       161
        2060       0.52      0.63      0.57       999
        2220       0.92      0.33      0.49       165
        2280       0.53      0.76      0.63       952
        2403       0.48      0.72      0.58       955
        2462       0.68      0.64      0.66       284
        2522       0.46      0.47      0.47       998
        2582       0.51      0.34      0.41       518
        2583       0.53      0.86      0.66      2042
        2585       0.75      0.15      0.25       499
        2705       0.46      0.60      0.52       552
        2905       0.84      0.79      0.82       174

    accuracy                           0.55     16984
    macro avg       0.65      0.49      0.51     16984
    weighted avg    0.59      0.55      0.53     16984

#### Heatmap de la matrice de confusion
![Heatmap](https://github.com/JulienJ-44/rakuteam/blob/main/Pictures/Heatmap_regressionlog1.png)


## Modèle Random Forest

### Présentation
RandomForestClassifier(n_jobs=-1, random_state=321)

### Résultats du modèle
#### Scores par classe
	precision    recall  f1-score   support

          10       0.54      0.64      0.59       601
          40       0.69      0.64      0.67       475
          50       0.78      0.64      0.71       341
          60       0.97      0.82      0.89       176
        1140       0.68      0.65      0.67       552
        1160       0.82      0.89      0.86       791
        1180       0.78      0.45      0.57       139
        1280       0.65      0.69      0.67       944
        1281       0.67      0.48      0.56       415
        1300       0.92      0.88      0.90      1006
        1301       0.91      0.69      0.79       154
        1302       0.93      0.65      0.76       505
        1320       0.66      0.55      0.60       635
        1560       0.63      0.80      0.71       967
        1920       0.91      0.87      0.89       866
        1940       0.86      0.70      0.77       175
        2060       0.78      0.74      0.76      1060
        2220       0.93      0.51      0.66       151
        2280       0.78      0.79      0.78       964
        2403       0.70      0.80      0.75       979
        2462       0.81      0.75      0.78       298
        2522       0.71      0.76      0.74       993
        2582       0.80      0.62      0.70       524
        2583       0.86      0.96      0.91      2045
        2585       0.93      0.61      0.74       527
        2705       0.67      0.89      0.76       536
        2905       0.99      0.99      0.99       165

        accuracy                           0.77     16984
       macro avg       0.79      0.72      0.75     16984
    weighted avg       0.77      0.77      0.76     16984
	

#### Importance par feature (Top 20)

				Importance
	class_2583		0.044457
	desi_capitals		0.042364
	blanc			0.034393
	class_1300		0.034078
	class_1920		0.028432
	B			0.026205
	G			0.025577
	desi_word_density	0.025452
	R			0.025192
	noir			0.024079
	desi_char_count (w/o space)	0.022967
	desi_length		0.022933
	desi_char_count		0.022904
	desi_total_length	0.022601
	class_1160		0.021263
	desi_num_symbols	0.020023
	desi_nb_mots+		0.018874
	class_2060		0.017385
	class_2522		0.017129
	desi_num_unique_words	0.015823

#### Heatmap de la matrice de confusion
![Heatmap](https://github.com/JulienJ-44/rakuteam/blob/main/Pictures/Heatmap_RandomForest.png)

## Modèle Voting Classifier (Soft)

### Présentation
VotingClassifier(estimators=[('rf',
                              RandomForestClassifier(n_jobs=-1,
                                                     random_state=321)),
                             ('knn', KNeighborsClassifier(n_neighbors=3)),
                             ('lr', LogisticRegression(max_iter=1000))],
                 voting='soft')

### Résultats du modèle
#### Scores par classe
	precision    recall  f1-score   support

          10       0.59      0.51      0.55       601
          40       0.63      0.57      0.60       475
          50       0.72      0.56      0.63       341
          60       0.97      0.83      0.89       176
        1140       0.63      0.60      0.62       552
        1160       0.66      0.75      0.70       791
        1180       0.64      0.47      0.54       139
        1280       0.69      0.67      0.68       944
        1281       0.70      0.53      0.60       415
        1300       0.87      0.84      0.86      1006
        1301       0.86      0.79      0.82       154
        1302       0.85      0.69      0.76       505
        1320       0.72      0.66      0.69       635
        1560       0.76      0.84      0.80       967
        1920       0.89      0.88      0.88       866
        1940       0.71      0.58      0.64       175
        2060       0.81      0.79      0.80      1060
        2220       0.83      0.67      0.74       151
        2280       0.74      0.71      0.73       964
        2403       0.57      0.69      0.62       979
        2462       0.73      0.61      0.67       298
        2522       0.77      0.82      0.79       993
        2582       0.85      0.77      0.80       524
        2583       0.81      0.96      0.88      2045
        2585       0.83      0.70      0.76       527
        2705       0.76      0.83      0.80       536
        2905       0.95      0.96      0.96       165

        accuracy                           0.75     16984
       macro avg       0.76      0.71      0.73     16984
    weighted avg       0.76      0.75      0.75     16984

#### Heatmap de la matrice de confusion
![Heatmap](https://github.com/JulienJ-44/rakuteam/blob/main/Pictures/Heatmap_VotingSoft.png)

## Modèle Voting Classifier (Hard)

### Présentation
VotingClassifier(estimators=[('rf',
                              RandomForestClassifier(n_jobs=-1,
                                                     random_state=321)),
                             ('knn', KNeighborsClassifier(n_neighbors=3)),
                             ('lr', LogisticRegression(max_iter=1000))])

### Résultats du modèle
#### Scores par classe
precision    recall  f1-score   support

          10       0.50      1.00      0.67       601
          40       0.55      0.85      0.67       475
          50       0.55      0.91      0.69       341
          60       0.81      0.95      0.88       176
        1140       0.55      0.84      0.66       552
        1160       0.57      0.73      0.64       791
        1180       0.51      0.64      0.57       139
        1280       0.69      0.81      0.74       944
        1281       0.68      0.74      0.71       415
        1300       0.83      0.85      0.84      1006
        1301       0.89      0.81      0.85       154
        1302       0.80      0.80      0.80       505
        1320       0.74      0.75      0.75       635
        1560       0.80      0.83      0.82       967
        1920       0.88      0.88      0.88       866
        1940       0.77      0.55      0.64       175
        2060       0.90      0.77      0.83      1060
        2220       0.86      0.62      0.72       151
        2280       0.91      0.67      0.77       964
        2403       0.82      0.36      0.50       979
        2462       0.69      0.20      0.31       298
        2522       0.97      0.71      0.82       993
        2582       0.97      0.70      0.82       524
        2583       0.90      1.00      0.95      2045
        2585       1.00      0.64      0.78       527
        2705       1.00      0.53      0.70       536
        2905       1.00      0.69      0.82       165

        accuracy                           0.77     16984
       macro avg       0.78      0.73      0.73     16984
    weighted avg       0.80      0.77      0.76     16984

#### Heatmap de la matrice de confusion
![Heatmap](https://github.com/JulienJ-44/rakuteam/blob/main/Pictures/Heatmap_VotingSoft.png)

## Modèle Word2vec

### Présentation
Calcul de la moyenne en utilisant la base word2vec FastText pré-entraînée.

### Résultats du modèle
#### Scores par classe
              precision    recall  f1-score   support

          10       0.27      0.35      0.30       614
          40       0.50      0.29      0.37       457
          50       0.82      0.27      0.41       333
          60       0.96      0.78      0.86       167
        1140       0.46      0.34      0.39       535
        1160       0.48      0.68      0.56       778
        1180       0.89      0.09      0.17       175
        1280       0.43      0.37      0.40       998
        1281       0.61      0.14      0.22       410
        1300       0.67      0.70      0.69       997
        1301       1.00      0.57      0.72       153
        1302       0.75      0.41      0.53       500
        1320       0.71      0.34      0.46       633
        1560       0.49      0.64      0.55      1056
        1920       0.89      0.71      0.79       858
        1940       1.00      0.09      0.17       155
        2060       0.48      0.64      0.55       982
        2220       0.92      0.14      0.24       158
        2280       0.60      0.73      0.66       956
        2403       0.37      0.64      0.47       945
        2462       0.74      0.50      0.60       312
        2522       0.69      0.50      0.58      1010
        2582       0.73      0.37      0.49       517
        2583       0.54      0.87      0.66      2013
        2585       0.90      0.28      0.43       505
        2705       0.65      0.46      0.54       594
        2905       0.92      0.90      0.91       173

    accuracy                           0.55     16984
    macro avg      0.68      0.47      0.51     16984
    weighted avg   0.61      0.55      0.54     16984

#### Heatmap de la matrice de confusion
![Heatmap](https://github.com/JulienJ-44/rakuteam/blob/main/Pictures/Heatmap_word2vec1.png)

## Modèle LeNet sur les Images

### Présentation
Entrainement d'un modèle de base similaire au LeNet sur les images téléchagées en format 128x128x3:

lenet = Sequential()

conv_1 = Conv2D(filters = 30,kernel_size = (5, 5), padding = 'valid', input_shape = (128, 128, 3), activation = 'relu')

max_pool_1 = MaxPooling2D(pool_size = (2, 2))

conv_2 = Conv2D(filters = 16, kernel_size = (3, 3), padding = 'valid',activation = 'relu')

max_pool_2 = MaxPooling2D(pool_size = (2, 2))

flatten = Flatten()

dropout = Dropout(rate = 0.2)

dense_1 = Dense(units = 128, activation = 'relu')

dense_2 = Dense(units = 28, activation = 'softmax')

Compile avec loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy']

Fit avec epochs = 5,batch_size = 200

### Résultats du modèle
#### Scores par classe

		precision    recall  f1-score   support

           1       0.51      0.42      0.46       601
           2       0.55      0.67      0.60       964
           3       0.22      0.16      0.18       341
           4       0.19      0.23      0.20       944
           5       0.71      0.77      0.74       536
           6       0.39      0.47      0.43       993
           7       0.43      0.13      0.20       524
           8       0.28      0.37      0.32       967
           9       0.14      0.11      0.12       415
          10       0.59      0.60      0.59       866
          11       0.40      0.46      0.43       979
          12       0.35      0.24      0.28       552
          13       0.43      0.80      0.56      2045
          14       0.19      0.08      0.11       139
          15       0.39      0.40      0.40      1006
          16       0.35      0.13      0.19       298
          17       0.71      0.78      0.74       791
          18       0.39      0.23      0.28      1060
          19       0.49      0.34      0.40       475
          20       0.30      0.15      0.20       176
          21       0.27      0.18      0.22       635
          22       0.18      0.10      0.13       505
          23       0.18      0.02      0.04       151
          24       0.89      0.81      0.84       165
          25       0.44      0.13      0.20       527
          26       0.40      0.08      0.13       175
          27       0.41      0.11      0.17       154

        accuracy                           0.42     16984
       macro avg       0.40      0.33      0.34     16984
    weighted avg       0.41      0.42      0.40     16984

