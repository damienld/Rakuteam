```python
import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

from os import listdir
from os.path import isfile, join

import PIL
from PIL import Image
```


```python
class_data = pd.read_excel("/Users/ayseaylinkaya/Desktop/Datascientist/2 Project Rakuten/Class_analysis_image.xlsx")
```


```python
class_data.drop(['Unnamed: 9'], axis=1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Classe</th>
      <th>NombreElements</th>
      <th>Nom</th>
      <th>Blanc</th>
      <th>Noir</th>
      <th>R</th>
      <th>G</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>12</td>
      <td>10</td>
      <td>3116</td>
      <td>LITTERATURE/ROMANS: livres d occasions?? [à vé...</td>
      <td>0.446384</td>
      <td>0.009475</td>
      <td>196.518350</td>
      <td>189.668004</td>
      <td>181.446701</td>
    </tr>
    <tr>
      <th>1</th>
      <td>16</td>
      <td>40</td>
      <td>2508</td>
      <td>JEUX VIDEOS: import slmt?</td>
      <td>0.473008</td>
      <td>0.010235</td>
      <td>188.988801</td>
      <td>183.619281</td>
      <td>179.766862</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20</td>
      <td>50</td>
      <td>1681</td>
      <td>Acessoires pour JEUX VIDEOS! et consoles??(non...</td>
      <td>0.541937</td>
      <td>0.006835</td>
      <td>198.779796</td>
      <td>196.199174</td>
      <td>195.407933</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23</td>
      <td>60</td>
      <td>832</td>
      <td>CONSOLES de jeux</td>
      <td>0.447811</td>
      <td>0.009602</td>
      <td>192.768904</td>
      <td>189.281101</td>
      <td>188.787452</td>
    </tr>
    <tr>
      <th>4</th>
      <td>14</td>
      <td>1140</td>
      <td>2671</td>
      <td>FIGURINES/MANGAS/UNIVERS FANTASTIQUES</td>
      <td>0.508225</td>
      <td>0.006417</td>
      <td>200.828538</td>
      <td>195.193835</td>
      <td>191.740965</td>
    </tr>
    <tr>
      <th>5</th>
      <td>10</td>
      <td>1160</td>
      <td>3953</td>
      <td>CARTES collection: cartes pokemon</td>
      <td>0.394803</td>
      <td>0.004779</td>
      <td>182.043666</td>
      <td>176.767507</td>
      <td>170.529569</td>
    </tr>
    <tr>
      <th>6</th>
      <td>27</td>
      <td>1180</td>
      <td>803</td>
      <td>JEUX DE GUERRE sur TABLE</td>
      <td>0.451595</td>
      <td>0.003903</td>
      <td>190.047650</td>
      <td>185.431614</td>
      <td>181.350853</td>
    </tr>
    <tr>
      <th>7</th>
      <td>6</td>
      <td>1280</td>
      <td>4870</td>
      <td>JOUETS ENFANTS: peluche, puzzle, DIY</td>
      <td>0.453874</td>
      <td>0.004390</td>
      <td>201.414075</td>
      <td>194.978948</td>
      <td>190.365770</td>
    </tr>
    <tr>
      <th>8</th>
      <td>19</td>
      <td>1281</td>
      <td>2070</td>
      <td>JEUX EDUCATIFS ENFANTS, jeux de cartes</td>
      <td>0.441863</td>
      <td>0.006471</td>
      <td>196.918476</td>
      <td>190.376583</td>
      <td>184.089469</td>
    </tr>
    <tr>
      <th>9</th>
      <td>3</td>
      <td>1300</td>
      <td>5045</td>
      <td>JEUX MINIATURES, radio commandés: drone, maque...</td>
      <td>0.513673</td>
      <td>0.006641</td>
      <td>199.363322</td>
      <td>196.663637</td>
      <td>195.741570</td>
    </tr>
    <tr>
      <th>10</th>
      <td>25</td>
      <td>1301</td>
      <td>807</td>
      <td>VETEMENTS ENFANTS/BEBE: (billard???, babyfoot???)</td>
      <td>0.510117</td>
      <td>0.002175</td>
      <td>252.757612</td>
      <td>252.706628</td>
      <td>252.664224</td>
    </tr>
    <tr>
      <th>11</th>
      <td>18</td>
      <td>1302</td>
      <td>2491</td>
      <td>LOISIRS/EQUIPEMENT extérieur: camping, pêche, ...</td>
      <td>0.525611</td>
      <td>0.008326</td>
      <td>206.230580</td>
      <td>202.251523</td>
      <td>199.203870</td>
    </tr>
    <tr>
      <th>12</th>
      <td>11</td>
      <td>1320</td>
      <td>3241</td>
      <td>BEBES accessoires</td>
      <td>0.489158</td>
      <td>0.004368</td>
      <td>212.954636</td>
      <td>208.976897</td>
      <td>207.004689</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2</td>
      <td>1560</td>
      <td>5073</td>
      <td>MAISON: cusine, fournitures, mobiliers, rangement</td>
      <td>0.477421</td>
      <td>0.003934</td>
      <td>210.097192</td>
      <td>204.789808</td>
      <td>201.922046</td>
    </tr>
    <tr>
      <th>14</th>
      <td>9</td>
      <td>1920</td>
      <td>4303</td>
      <td>LITERIE, TEXTILE MAISON: eqipements intérieur,...</td>
      <td>0.322192</td>
      <td>0.008748</td>
      <td>194.063334</td>
      <td>185.428405</td>
      <td>179.968530</td>
    </tr>
    <tr>
      <th>15</th>
      <td>26</td>
      <td>1940</td>
      <td>803</td>
      <td>ALIMENTATIONS, CONFISERIES, CAFE</td>
      <td>0.545409</td>
      <td>0.006333</td>
      <td>214.349306</td>
      <td>205.896247</td>
      <td>198.179298</td>
    </tr>
    <tr>
      <th>16</th>
      <td>4</td>
      <td>2060</td>
      <td>4993</td>
      <td>LUMINAIRES, DECO</td>
      <td>0.328828</td>
      <td>0.013231</td>
      <td>185.499234</td>
      <td>178.448102</td>
      <td>173.980503</td>
    </tr>
    <tr>
      <th>17</th>
      <td>24</td>
      <td>2220</td>
      <td>824</td>
      <td>Accessoires ANIMAUX domestiques</td>
      <td>0.533149</td>
      <td>0.004795</td>
      <td>210.703365</td>
      <td>205.124100</td>
      <td>202.386165</td>
    </tr>
    <tr>
      <th>18</th>
      <td>8</td>
      <td>2280</td>
      <td>4760</td>
      <td>MAGASINES/REVUES d'ARTS et SPECTACLES</td>
      <td>0.435789</td>
      <td>0.003083</td>
      <td>195.886675</td>
      <td>189.277178</td>
      <td>182.635228</td>
    </tr>
    <tr>
      <th>19</th>
      <td>7</td>
      <td>2403</td>
      <td>4774</td>
      <td>LIVRES MAGASINES: histoire, info, musées, spirou</td>
      <td>0.319316</td>
      <td>0.003913</td>
      <td>174.865981</td>
      <td>164.963075</td>
      <td>158.467833</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>2462</td>
      <td>1421</td>
      <td>JEUX VIDEOS OCASSIONS (Acessoires/jeux par LOT...</td>
      <td>0.340726</td>
      <td>0.004764</td>
      <td>169.373563</td>
      <td>161.705078</td>
      <td>155.681222</td>
    </tr>
    <tr>
      <th>21</th>
      <td>5</td>
      <td>2522</td>
      <td>4989</td>
      <td>FOURNITURE de BUREAU: cahiers, carnets</td>
      <td>0.553008</td>
      <td>0.005561</td>
      <td>218.836466</td>
      <td>214.762874</td>
      <td>211.568728</td>
    </tr>
    <tr>
      <th>22</th>
      <td>15</td>
      <td>2582</td>
      <td>2589</td>
      <td>MOBILIER extérieur et accessoires extérieur ma...</td>
      <td>0.466371</td>
      <td>0.007111</td>
      <td>202.224993</td>
      <td>199.653917</td>
      <td>194.772481</td>
    </tr>
    <tr>
      <th>23</th>
      <td>1</td>
      <td>2583</td>
      <td>10209</td>
      <td>PISCINE: piscine et accessoires</td>
      <td>0.579508</td>
      <td>0.003441</td>
      <td>206.741823</td>
      <td>211.319401</td>
      <td>212.720218</td>
    </tr>
    <tr>
      <th>24</th>
      <td>17</td>
      <td>2585</td>
      <td>2496</td>
      <td>OUTILS JARDINS</td>
      <td>0.563404</td>
      <td>0.004857</td>
      <td>210.341622</td>
      <td>208.508508</td>
      <td>205.558651</td>
    </tr>
    <tr>
      <th>25</th>
      <td>13</td>
      <td>2705</td>
      <td>2761</td>
      <td>ROMAN: livre histoire?</td>
      <td>0.669290</td>
      <td>0.008009</td>
      <td>219.881707</td>
      <td>215.700007</td>
      <td>212.826043</td>
    </tr>
    <tr>
      <th>26</th>
      <td>22</td>
      <td>2905</td>
      <td>872</td>
      <td>Jeux PC (en TELECHARGEMENT ou pas)</td>
      <td>0.630324</td>
      <td>0.012919</td>
      <td>200.143562</td>
      <td>197.131754</td>
      <td>194.937020</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.catplot(y = 'Classe', x='Blanc', color='w', edgecolor='k', kind='bar', orient = 'h', data=class_data)
plt.title("Pourcentage des pixels blancs sur les images")
plt.savefig("Pourcentage des pixels blancs sur les images.png", bbox_inches = "tight");
```


    
![png](output_3_0.png)
    



```python
sns.catplot(y = 'Classe', x='Noir', color='k', kind='bar', orient = 'h', data=class_data)
plt.title("Pourcentage des pixels noirs sur les images");
plt.savefig("Pourcentage des pixels noirs sur les images.png", bbox_inches = "tight");
```


    
![png](output_4_0.png)
    



```python
sns.catplot(y = 'Classe', x='R', color='r', kind='bar', orient = 'h', data=class_data)
plt.title("Moyenne de valeur R sur les images")
plt.xlim(150, 255);
plt.savefig("Moyenne de valeur R sur les images.png", bbox_inches = "tight");
```


    
![png](output_5_0.png)
    



```python
sns.catplot(y = 'Classe', x='G', color='g', kind='bar', orient = 'h', data=class_data)
plt.title("Moyenne de valeur G sur les images")
plt.xlim(150, 255);
plt.savefig("Moyenne de valeur G sur les images.png", bbox_inches = "tight");
```


    
![png](output_6_0.png)
    



```python
sns.catplot(y = 'Classe', x='B', color='b', kind='bar', orient = 'h', data=class_data)
plt.title("Moyenne de valeur B sur les images")
plt.xlim(150, 255);
plt.savefig("Moyenne de valeur B sur les images.png", bbox_inches = "tight");
```


    
![png](output_7_0.png)
    

