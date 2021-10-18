# Multimodal Product Data Classification
<br>
In order to complete training as a Data Scientist, we developped this project as a team of 4 people.<br>
For this [contest organized by ENS](https://challengedata.ens.fr/participants/challenges/35/), we worked on the classification of e-commerce articles by aggregating several models.<br>
The data provided for each article included both some text(title and description) and a picture.

## Dataset
99 000 articles (85 000 in train + 14 000 in test) and 27 categories<br>
Each article includes:<br>
text data (2 fields: description and title)
![text data](https://github.com/damienld/Rakuteam/blob/main/Pictures/presentation/dataset1.png)<br>
one picture
![picture data](https://github.com/damienld/Rakuteam/blob/main/Pictures/presentation/dataset2.png)

## EDA
15 most frequent words from the description field for category/class #1560
![15 most frequent words from the description field for category/class #1560](https://github.com/damienld/Rakuteam/blob/main/Pictures/presentation/EDA1.png)<br>
15 random images for category/class #10
![15 random images for category/class #10](https://github.com/damienld/Rakuteam/blob/main/Pictures/presentation/EDA2.png)<br>

## Model 1: Random Forest

### Features engineering
tf-idf for category/class 1281
![tf-idf for category/class 1281](https://github.com/damienld/Rakuteam/blob/main/Pictures/presentation/tdidf.png)<br>
frequency of regular expressions
![frequency of regular expressions](https://github.com/damienld/Rakuteam/blob/main/Pictures/presentation/regex.png)<br>
% of pixels in green
![% of pixels in green](https://github.com/damienld/Rakuteam/blob/main/Pictures/presentation/pixelsrgb.png)<br>
### Best Model selected
![](https://github.com/damienld/Rakuteam/blob/main/Pictures/presentation/ML1.png)<br>
![](https://github.com/damienld/Rakuteam/blob/main/Pictures/presentation/ML2.png)<br>
![](https://github.com/damienld/Rakuteam/blob/main/Pictures/presentation/ML3.png)<br>
Result: Accuracy 0.77
## Model 2: Convolutional neural network (on the pictures)
![](https://github.com/damienld/Rakuteam/blob/main/Pictures/presentation/cnn.png)<br>
Result: Accuracy 0.58 
## Model 3: Dense neural network (on the text)
![](https://github.com/damienld/Rakuteam/blob/main/Pictures/presentation/dnn.png)<br>
Result: Accuracy 0.82
## Final Model: Voting Classifier between all the 3 weighted odels
Result: Accuracy 0.84
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

 
