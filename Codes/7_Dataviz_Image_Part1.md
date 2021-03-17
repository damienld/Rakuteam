```python
pip install opencv-python
```

    Collecting opencv-python
      Downloading opencv_python-4.5.1.48-cp38-cp38-macosx_10_13_x86_64.whl (40.3 MB)
    [K     |████████████████████████████████| 40.3 MB 19.7 MB/s eta 0:00:01
    [?25hRequirement already satisfied: numpy>=1.17.3 in /opt/anaconda3/lib/python3.8/site-packages (from opencv-python) (1.19.2)
    Installing collected packages: opencv-python
    Successfully installed opencv-python-4.5.1.48
    Note: you may need to restart the kernel to use updated packages.



```python
pip install keras
```

    Collecting keras
      Downloading Keras-2.4.3-py2.py3-none-any.whl (36 kB)
    Requirement already satisfied: scipy>=0.14 in /opt/anaconda3/lib/python3.8/site-packages (from keras) (1.5.2)
    Requirement already satisfied: numpy>=1.9.1 in /opt/anaconda3/lib/python3.8/site-packages (from keras) (1.19.2)
    Requirement already satisfied: pyyaml in /opt/anaconda3/lib/python3.8/site-packages (from keras) (5.3.1)
    Requirement already satisfied: h5py in /opt/anaconda3/lib/python3.8/site-packages (from keras) (2.10.0)
    Requirement already satisfied: six in /opt/anaconda3/lib/python3.8/site-packages (from h5py->keras) (1.15.0)
    Installing collected packages: keras
    Successfully installed keras-2.4.3
    Note: you may need to restart the kernel to use updated packages.



```python
pip install tensorflow
```

    Collecting tensorflow
      Downloading tensorflow-2.4.1-cp38-cp38-macosx_10_11_x86_64.whl (173.9 MB)
    [K     |████████████████████████████████| 173.9 MB 20.5 MB/s eta 0:00:01
    [?25hCollecting keras-preprocessing~=1.1.2
      Downloading Keras_Preprocessing-1.1.2-py2.py3-none-any.whl (42 kB)
    [K     |████████████████████████████████| 42 kB 4.2 MB/s  eta 0:00:01
    [?25hCollecting gast==0.3.3
      Downloading gast-0.3.3-py2.py3-none-any.whl (9.7 kB)
    Collecting tensorboard~=2.4
      Downloading tensorboard-2.4.1-py3-none-any.whl (10.6 MB)
    [K     |████████████████████████████████| 10.6 MB 13.1 MB/s eta 0:00:01
    [?25hCollecting astunparse~=1.6.3
      Downloading astunparse-1.6.3-py2.py3-none-any.whl (12 kB)
    Requirement already satisfied: numpy~=1.19.2 in /opt/anaconda3/lib/python3.8/site-packages (from tensorflow) (1.19.2)
    Collecting grpcio~=1.32.0
      Downloading grpcio-1.32.0-cp38-cp38-macosx_10_9_x86_64.whl (3.3 MB)
    [K     |████████████████████████████████| 3.3 MB 15.5 MB/s eta 0:00:01
    [?25hCollecting absl-py~=0.10
      Downloading absl_py-0.11.0-py3-none-any.whl (127 kB)
    [K     |████████████████████████████████| 127 kB 16.5 MB/s eta 0:00:01
    [?25hCollecting tensorflow-estimator<2.5.0,>=2.4.0
      Downloading tensorflow_estimator-2.4.0-py2.py3-none-any.whl (462 kB)
    [K     |████████████████████████████████| 462 kB 15.7 MB/s eta 0:00:01
    [?25hRequirement already satisfied: typing-extensions~=3.7.4 in /opt/anaconda3/lib/python3.8/site-packages (from tensorflow) (3.7.4.3)
    Collecting wrapt~=1.12.1
      Downloading wrapt-1.12.1.tar.gz (27 kB)
    Collecting google-pasta~=0.2
      Downloading google_pasta-0.2.0-py3-none-any.whl (57 kB)
    [K     |████████████████████████████████| 57 kB 11.0 MB/s eta 0:00:01
    [?25hRequirement already satisfied: wheel~=0.35 in /opt/anaconda3/lib/python3.8/site-packages (from tensorflow) (0.35.1)
    Collecting termcolor~=1.1.0
      Downloading termcolor-1.1.0.tar.gz (3.9 kB)
    Requirement already satisfied: six~=1.15.0 in /opt/anaconda3/lib/python3.8/site-packages (from tensorflow) (1.15.0)
    Collecting protobuf>=3.9.2
      Downloading protobuf-3.14.0-cp38-cp38-macosx_10_9_x86_64.whl (1.0 MB)
    [K     |████████████████████████████████| 1.0 MB 13.5 MB/s eta 0:00:01
    [?25hRequirement already satisfied: h5py~=2.10.0 in /opt/anaconda3/lib/python3.8/site-packages (from tensorflow) (2.10.0)
    Collecting flatbuffers~=1.12.0
      Downloading flatbuffers-1.12-py2.py3-none-any.whl (15 kB)
    Collecting opt-einsum~=3.3.0
      Downloading opt_einsum-3.3.0-py3-none-any.whl (65 kB)
    [K     |████████████████████████████████| 65 kB 7.9 MB/s  eta 0:00:01
    [?25hCollecting google-auth<2,>=1.6.3
      Downloading google_auth-1.24.0-py2.py3-none-any.whl (114 kB)
    [K     |████████████████████████████████| 114 kB 14.3 MB/s eta 0:00:01
    [?25hCollecting google-auth-oauthlib<0.5,>=0.4.1
      Downloading google_auth_oauthlib-0.4.2-py2.py3-none-any.whl (18 kB)
    Requirement already satisfied: requests<3,>=2.21.0 in /opt/anaconda3/lib/python3.8/site-packages (from tensorboard~=2.4->tensorflow) (2.24.0)
    Requirement already satisfied: setuptools>=41.0.0 in /opt/anaconda3/lib/python3.8/site-packages (from tensorboard~=2.4->tensorflow) (50.3.1.post20201107)
    Requirement already satisfied: werkzeug>=0.11.15 in /opt/anaconda3/lib/python3.8/site-packages (from tensorboard~=2.4->tensorflow) (1.0.1)
    Collecting markdown>=2.6.8
      Downloading Markdown-3.3.3-py3-none-any.whl (96 kB)
    [K     |████████████████████████████████| 96 kB 9.0 MB/s  eta 0:00:01
    [?25hCollecting tensorboard-plugin-wit>=1.6.0
      Downloading tensorboard_plugin_wit-1.8.0-py3-none-any.whl (781 kB)
    [K     |████████████████████████████████| 781 kB 12.1 MB/s eta 0:00:01
    [?25hCollecting rsa<5,>=3.1.4; python_version >= "3.6"
      Downloading rsa-4.7-py3-none-any.whl (34 kB)
    Collecting cachetools<5.0,>=2.0.0
      Downloading cachetools-4.2.1-py3-none-any.whl (12 kB)
    Collecting pyasn1-modules>=0.2.1
      Downloading pyasn1_modules-0.2.8-py2.py3-none-any.whl (155 kB)
    [K     |████████████████████████████████| 155 kB 17.0 MB/s eta 0:00:01
    [?25hCollecting requests-oauthlib>=0.7.0
      Downloading requests_oauthlib-1.3.0-py2.py3-none-any.whl (23 kB)
    Requirement already satisfied: idna<3,>=2.5 in /opt/anaconda3/lib/python3.8/site-packages (from requests<3,>=2.21.0->tensorboard~=2.4->tensorflow) (2.10)
    Requirement already satisfied: certifi>=2017.4.17 in /opt/anaconda3/lib/python3.8/site-packages (from requests<3,>=2.21.0->tensorboard~=2.4->tensorflow) (2020.6.20)
    Requirement already satisfied: chardet<4,>=3.0.2 in /opt/anaconda3/lib/python3.8/site-packages (from requests<3,>=2.21.0->tensorboard~=2.4->tensorflow) (3.0.4)
    Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /opt/anaconda3/lib/python3.8/site-packages (from requests<3,>=2.21.0->tensorboard~=2.4->tensorflow) (1.25.11)
    Collecting pyasn1>=0.1.3
      Downloading pyasn1-0.4.8-py2.py3-none-any.whl (77 kB)
    [K     |████████████████████████████████| 77 kB 11.5 MB/s eta 0:00:01
    [?25hCollecting oauthlib>=3.0.0
      Downloading oauthlib-3.1.0-py2.py3-none-any.whl (147 kB)
    [K     |████████████████████████████████| 147 kB 11.0 MB/s eta 0:00:01
    [?25hBuilding wheels for collected packages: wrapt, termcolor
      Building wheel for wrapt (setup.py) ... [?25ldone
    [?25h  Created wheel for wrapt: filename=wrapt-1.12.1-py3-none-any.whl size=19552 sha256=a38c9e05859ba36b4043a63f23f65def4739b3967241fb60124228a76bf354ac
      Stored in directory: /Users/ayseaylinkaya/Library/Caches/pip/wheels/5f/fd/9e/b6cf5890494cb8ef0b5eaff72e5d55a70fb56316007d6dfe73
      Building wheel for termcolor (setup.py) ... [?25ldone
    [?25h  Created wheel for termcolor: filename=termcolor-1.1.0-py3-none-any.whl size=4830 sha256=9854c8754a3aae3f5a7baf79390ff929711e879976dc16553f30ca2288d939b4
      Stored in directory: /Users/ayseaylinkaya/Library/Caches/pip/wheels/a0/16/9c/5473df82468f958445479c59e784896fa24f4a5fc024b0f501
    Successfully built wrapt termcolor
    Installing collected packages: keras-preprocessing, gast, pyasn1, rsa, cachetools, pyasn1-modules, google-auth, oauthlib, requests-oauthlib, google-auth-oauthlib, grpcio, protobuf, markdown, absl-py, tensorboard-plugin-wit, tensorboard, astunparse, tensorflow-estimator, wrapt, google-pasta, termcolor, flatbuffers, opt-einsum, tensorflow
      Attempting uninstall: wrapt
        Found existing installation: wrapt 1.11.2
        Uninstalling wrapt-1.11.2:
          Successfully uninstalled wrapt-1.11.2
    Successfully installed absl-py-0.11.0 astunparse-1.6.3 cachetools-4.2.1 flatbuffers-1.12 gast-0.3.3 google-auth-1.24.0 google-auth-oauthlib-0.4.2 google-pasta-0.2.0 grpcio-1.32.0 keras-preprocessing-1.1.2 markdown-3.3.3 oauthlib-3.1.0 opt-einsum-3.3.0 protobuf-3.14.0 pyasn1-0.4.8 pyasn1-modules-0.2.8 requests-oauthlib-1.3.0 rsa-4.7 tensorboard-2.4.1 tensorboard-plugin-wit-1.8.0 tensorflow-2.4.1 tensorflow-estimator-2.4.0 termcolor-1.1.0 wrapt-1.12.1
    Note: you may need to restart the kernel to use updated packages.



```python
pip install Pillow
```

    Requirement already satisfied: Pillow in /opt/anaconda3/lib/python3.8/site-packages (8.0.1)
    Note: you may need to restart the kernel to use updated packages.



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
#import les datasets
X_train = pd.read_csv("/Users/ayseaylinkaya/Desktop/Datascientist/Project Rakuten/X_train_update.csv") 
X_test = pd.read_csv("/Users/ayseaylinkaya/Desktop/Datascientist/Project Rakuten/X_test_update.csv") 
y_train = pd.read_csv("/Users/ayseaylinkaya/Desktop/Datascientist/Project Rakuten/Y_train_CVw08PX.csv") 
```


```python
X_train.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 84916 entries, 0 to 84915
    Data columns (total 5 columns):
     #   Column       Non-Null Count  Dtype 
    ---  ------       --------------  ----- 
     0   Unnamed: 0   84916 non-null  int64 
     1   designation  84916 non-null  object
     2   description  55116 non-null  object
     3   productid    84916 non-null  int64 
     4   imageid      84916 non-null  int64 
    dtypes: int64(3), object(2)
    memory usage: 3.2+ MB



```python
#identifier les classes de produits
y_train["prdtypecode"].unique()
```




    array([  10, 2280,   50, 1280, 2705, 2522, 2582, 1560, 1281, 1920, 2403,
           1140, 2583, 1180, 1300, 2462, 1160, 2060,   40,   60, 1320, 1302,
           2220, 2905, 2585, 1940, 1301])




```python
#merge les training sets pour analyses les articles par classe
X_train = X_train.sort_values(by = 'Unnamed: 0', ascending = True)
y_train = y_train.sort_values(by = 'Unnamed: 0', ascending = True)
part2 = X_train[X_train.columns[3:]]
df = pd.concat([y_train,part2], axis=1)
df["image_name"] = "image_" + df.imageid.map(str)+ "_product_" + df.productid.map(str) + ".jpg"
df["image_name"] = df["image_name"].astype(str)
df['fullpath']= '/Users/ayseaylinkaya/Desktop/Datascientist/Project Rakuten/images/image_train/'+ df['image_name']
df.head()
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
      <th>Unnamed: 0</th>
      <th>prdtypecode</th>
      <th>productid</th>
      <th>imageid</th>
      <th>image_name</th>
      <th>fullpath</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>10</td>
      <td>3804725264</td>
      <td>1263597046</td>
      <td>image_1263597046_product_3804725264.jpg</td>
      <td>/Users/ayseaylinkaya/Desktop/Datascientist/Pro...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2280</td>
      <td>436067568</td>
      <td>1008141237</td>
      <td>image_1008141237_product_436067568.jpg</td>
      <td>/Users/ayseaylinkaya/Desktop/Datascientist/Pro...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>50</td>
      <td>201115110</td>
      <td>938777978</td>
      <td>image_938777978_product_201115110.jpg</td>
      <td>/Users/ayseaylinkaya/Desktop/Datascientist/Pro...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>1280</td>
      <td>50418756</td>
      <td>457047496</td>
      <td>image_457047496_product_50418756.jpg</td>
      <td>/Users/ayseaylinkaya/Desktop/Datascientist/Pro...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>2705</td>
      <td>278535884</td>
      <td>1077757786</td>
      <td>image_1077757786_product_278535884.jpg</td>
      <td>/Users/ayseaylinkaya/Desktop/Datascientist/Pro...</td>
    </tr>
  </tbody>
</table>
</div>




```python
#analyses rapides sur les classes
df_sorted = df.sort_values("prdtypecode")
sns.countplot(x = "prdtypecode", data= df_sorted);
```


    
![png](output_9_0.png)
    



```python
df_grouped = df.groupby("prdtypecode").count()
df_grouped = df_grouped.reset_index()
df_grouped = df_grouped.sort_values("productid",ascending = False)
df_grouped["shareintotal"]= df_grouped["productid"]/ df_grouped["productid"].sum()
df_grouped.head()
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
      <th>prdtypecode</th>
      <th>Unnamed: 0</th>
      <th>productid</th>
      <th>imageid</th>
      <th>image_name</th>
      <th>fullpath</th>
      <th>shareintotal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>23</th>
      <td>2583</td>
      <td>10209</td>
      <td>10209</td>
      <td>10209</td>
      <td>10209</td>
      <td>10209</td>
      <td>0.120225</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1560</td>
      <td>5073</td>
      <td>5073</td>
      <td>5073</td>
      <td>5073</td>
      <td>5073</td>
      <td>0.059741</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1300</td>
      <td>5045</td>
      <td>5045</td>
      <td>5045</td>
      <td>5045</td>
      <td>5045</td>
      <td>0.059412</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2060</td>
      <td>4993</td>
      <td>4993</td>
      <td>4993</td>
      <td>4993</td>
      <td>4993</td>
      <td>0.058799</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2522</td>
      <td>4989</td>
      <td>4989</td>
      <td>4989</td>
      <td>4989</td>
      <td>4989</td>
      <td>0.058752</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_grouped.plot(x='prdtypecode', y='productid', kind='bar',figsize=(15,4), width = 0.8)
plt.title("# de produits par classe");
plt.savefig("Répartition des classes.png")
```


    
![png](output_11_0.png)
    



```python
cum_sales = np.cumsum(df_grouped["shareintotal"])
# Borrowing the linspace trick from ebarr
x_vals = np.linspace(0, 100, len(cum_sales))
plt.plot(x_vals/100, cum_sales)
plt.title("% des produits vs % des classes")
plt.show()
```


    
![png](output_12_0.png)
    



```python
df_2583 = df[df['prdtypecode']==2583]
df_2583 = df_2583.head(20)

images_2583 = np.array([np.array(Image.open(fname)) for fname in df_2583['fullpath']])
images_2583.shape 

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_2583[i])
#Piscine et accessoire
```


    
![png](output_13_0.png)
    



```python
df_2583 = df[df['prdtypecode']==2583]

images_2583 = np.array([np.array(Image.open(fname)) for fname in df_2583['fullpath']])

white_pix_tot_ = 0
for image in images_2583:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_2583)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_2583:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_2583)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_2583:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_2583)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.5795076082681064
    % des pixels noirs:  0.003441213284578332
    Couleur moyenne RGB :  [206.74182312 211.31940057 212.72021775]



```python
df_1560 = df[df['prdtypecode']==1560]
df_1560 = df_1560.head(20)

images_1560 = np.array([np.array(Image.open(fname)) for fname in df_1560['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_1560[i])
#Equipement cuisine 
```


    
![png](output_15_0.png)
    



```python
df_1560 = df[df['prdtypecode']==1560]

images_1560 = np.array([np.array(Image.open(fname)) for fname in df_1560['fullpath']])

white_pix_tot_ = 0
for image in images_1560:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_1560)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_1560:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_1560)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_1560:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_1560)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.4774209253449514
    % des pixels noirs:  0.003933554611988572
    Couleur moyenne RGB :  [210.09719206 204.78980796 201.92204634]



```python
df_1300 = df[df['prdtypecode']==1300]
df_1300 = df_1300.head(20)

images_1300 = np.array([np.array(Image.open(fname)) for fname in df_1300['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_1300[i])
#Drone/Quadcopter
```


    
![png](output_17_0.png)
    



```python
df_1300 = df[df['prdtypecode']==1300]

images_1300 = np.array([np.array(Image.open(fname)) for fname in df_1300['fullpath']])

white_pix_tot_ = 0
for image in images_1300:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_1300)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_1300:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_1300)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_1300:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_1300)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.5136730409498536
    % des pixels noirs:  0.006641245104977612
    Couleur moyenne RGB :  [199.36332156 196.66363691 195.74157053]



```python
df_2060 = df[df['prdtypecode']==2060]
df_2060 = df_2060.head(20)

images_2060 = np.array([np.array(Image.open(fname)) for fname in df_2060['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_2060[i])
#Equipement intérieur/Salle de bain/Lampe
```


    
![png](output_19_0.png)
    



```python
df_2060 = df[df['prdtypecode']==2060]

images_2060 = np.array([np.array(Image.open(fname)) for fname in df_2060['fullpath']])

white_pix_tot_ = 0
for image in images_2060:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_2060)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_2060:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_2060)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_2060:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_2060)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.328828147881891
    % des pixels noirs:  0.013230872270199251
    Couleur moyenne RGB :  [185.4992341  178.4481019  173.98050274]



```python
df_2522 = df[df['prdtypecode']==2522]
df_2522 = df_2522.head(20)

images_2522 = np.array([np.array(Image.open(fname)) for fname in df_2522['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_2522[i])
#Fourniture bureau
```


    
![png](output_21_0.png)
    



```python
df_2522 = df[df['prdtypecode']==2522]

images_2522 = np.array([np.array(Image.open(fname)) for fname in df_2522['fullpath']])

white_pix_tot_ = 0
for image in images_2522:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_2522)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_2522:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_2522)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_2522:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_2522)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.5530082910699294
    % des pixels noirs:  0.005561309054373662
    Couleur moyenne RGB :  [218.83646585 214.76287372 211.56872808]



```python
df_1280 = df[df['prdtypecode']==1280]
df_1280 = df_1280.head(20)

images_1280 = np.array([np.array(Image.open(fname)) for fname in df_1280['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_1280[i])
#Jouet enfant
```


    
![png](output_23_0.png)
    



```python
df_1280 = df[df['prdtypecode']==1280]

images_1280 = np.array([np.array(Image.open(fname)) for fname in df_1280['fullpath']])

white_pix_tot_ = 0
for image in images_1280:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_1280)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_1280:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_1280)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_1280:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_1280)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.4538742784991934
    % des pixels noirs:  0.004389549892345181
    Couleur moyenne RGB :  [201.41407457 194.97894764 190.36577028]



```python
df_2403 = df[df['prdtypecode']==2403]
df_2403 = df_2403.head(20)

images_2403 = np.array([np.array(Image.open(fname)) for fname in df_2403['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_2403[i])
#Livre/magazine
```


    
![png](output_25_0.png)
    



```python
df_2403 = df[df['prdtypecode']==2403]

images_2403 = np.array([np.array(Image.open(fname)) for fname in df_2403['fullpath']])

white_pix_tot_ = 0
for image in images_2403:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_2403)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_2403:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_2403)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_2403:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_2403)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.31931610660770154
    % des pixels noirs:  0.003912907739818253
    Couleur moyenne RGB :  [174.86598119 164.96307473 158.46783282]



```python
df_2280 = df[df['prdtypecode']==2280]
df_2280 = df_2280.head(20)

images_2280 = np.array([np.array(Image.open(fname)) for fname in df_2280['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_2280[i])
#Livre histoire /magazine
```


    
![png](output_27_0.png)
    



```python
df_2280 = df[df['prdtypecode']==2280]

images_2280 = np.array([np.array(Image.open(fname)) for fname in df_2280['fullpath']])

white_pix_tot_ = 0
for image in images_2280:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_2280)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_2280:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_2280)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_2280:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_2280)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.435788945400548
    % des pixels noirs:  0.003082600470813688
    Couleur moyenne RGB :  [195.88667463 189.27717792 182.63522754]



```python
df_1920 = df[df['prdtypecode']==1920]
df_1920 = df_1920.head(20)

images_1920 = np.array([np.array(Image.open(fname)) for fname in df_1920['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_1920[i])
#Textile maison
```


    
![png](output_29_0.png)
    



```python
df_1920 = df[df['prdtypecode']==1920]

images_1920 = np.array([np.array(Image.open(fname)) for fname in df_1920['fullpath']])

white_pix_tot_ = 0
for image in images_1920:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_1920)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_1920:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_1920)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_1920:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_1920)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.3221919298811843
    % des pixels noirs:  0.008748094492324129
    Couleur moyenne RGB :  [194.06333385 185.42840536 179.96852998]



```python
df_1160 = df[df['prdtypecode']==1160]
df_1160 = df_1160.head(20)

images_1160 = np.array([np.array(Image.open(fname)) for fname in df_1160['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_1160[i])
#Carte de jeux collection 
```


    
![png](output_31_0.png)
    



```python
df_1160 = df[df['prdtypecode']==1160]

images_1160 = np.array([np.array(Image.open(fname)) for fname in df_1160['fullpath']])

white_pix_tot_ = 0
for image in images_1160:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_1160)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_1160:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_1160)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_1160:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_1160)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.39480313852682636
    % des pixels noirs:  0.004779293724890555
    Couleur moyenne RGB :  [182.04366613 176.76750748 170.52956861]



```python
df_1320 = df[df['prdtypecode']==1320]
df_1320 = df_1320.head(20)

images_1320 = np.array([np.array(Image.open(fname)) for fname in df_1320['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_1320[i])
#Equipement bébé
```


    
![png](output_33_0.png)
    



```python
df_1320 = df[df['prdtypecode']==1320]

images_1320 = np.array([np.array(Image.open(fname)) for fname in df_1320['fullpath']])

white_pix_tot_ = 0
for image in images_1320:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_1320)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_1320:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_1320)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_1320:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_1320)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.4891579110784299
    % des pixels noirs:  0.004368086997960995
    Couleur moyenne RGB :  [212.95463618 208.97689725 207.00468861]



```python
df_10 = df[df['prdtypecode']==10]
df_10 = df_10.head(20)

images_10 = np.array([np.array(Image.open(fname)) for fname in df_10['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_10[i])
#Livre histoire geographie
```


    
![png](output_35_0.png)
    



```python
df_10 = df[df['prdtypecode']==10]

images_10 = np.array([np.array(Image.open(fname)) for fname in df_10['fullpath']])

white_pix_tot_ = 0
for image in images_10:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_10)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_10:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_10)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_10:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_10)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.4463844507630748
    % des pixels noirs:  0.00947515706685858
    Couleur moyenne RGB :  [196.51835007 189.66800433 181.44670057]



```python
df_2705 = df[df['prdtypecode']==2705]
df_2705 = df_2705.head(20)

images_2705 = np.array([np.array(Image.open(fname)) for fname in df_2705['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_2705[i])
#Livre histoire politique
```


    
![png](output_37_0.png)
    



```python
df_2705 = df[df['prdtypecode']==2705]

images_2705 = np.array([np.array(Image.open(fname)) for fname in df_2705['fullpath']])

white_pix_tot_ = 0
for image in images_2705:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_2705)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_2705:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_2705)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_2705:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_2705)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.6692904229569338
    % des pixels noirs:  0.00800904038044193
    Couleur moyenne RGB :  [219.88170746 215.70000705 212.82604253]



```python
df_1140 = df[df['prdtypecode']==1140]
df_1140 = df_1140.head(20)

images_1140 = np.array([np.array(Image.open(fname)) for fname in df_1140['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_1140[i])
```


    
![png](output_39_0.png)
    



```python
df_1140 = df[df['prdtypecode']==1140]

images_1140 = np.array([np.array(Image.open(fname)) for fname in df_1140['fullpath']])

white_pix_tot_ = 0
for image in images_1140:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_1140)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_1140:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_1140)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_1140:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_1140)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.5082254201009445
    % des pixels noirs:  0.006416657821183246
    Couleur moyenne RGB :  [200.82853763 195.19383462 191.74096515]



```python
df_2582 = df[df['prdtypecode']==2582]
df_2582 = df_2582.head(20)

images_2582 = np.array([np.array(Image.open(fname)) for fname in df_2582['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_2582[i])
#Equipement extérieurs 
```


    
![png](output_41_0.png)
    



```python
df_2582 = df[df['prdtypecode']==2582]

images_2582 = np.array([np.array(Image.open(fname)) for fname in df_2582['fullpath']])

white_pix_tot_ = 0
for image in images_2582:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_2582)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_2582:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_2582)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_2582:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_2582)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.46637138460928373
    % des pixels noirs:  0.007111423969803496
    Couleur moyenne RGB :  [202.2249929  199.65391673 194.77248131]



```python
df_40 = df[df['prdtypecode']==40]
df_40 = df_40.head(20)

images_40 = np.array([np.array(Image.open(fname)) for fname in df_40['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_40[i])
#Jeux video import international
```


    
![png](output_43_0.png)
    



```python
df_40 = df[df['prdtypecode']==40]

images_40 = np.array([np.array(Image.open(fname)) for fname in df_40['fullpath']])

white_pix_tot_ = 0
for image in images_40:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_40)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_40:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_40)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_40:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_40)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.47300761963766985
    % des pixels noirs:  0.01023486739392734
    Couleur moyenne RGB :  [188.9888008  183.61928141 179.76686204]



```python
df_2585 = df[df['prdtypecode']==2585]
df_2585 = df_2585.head(20)

images_2585 = np.array([np.array(Image.open(fname)) for fname in df_2585['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_2585[i])
#Outils jardin
```


    
![png](output_45_0.png)
    



```python
df_2585 = df[df['prdtypecode']==2585]

images_2585 = np.array([np.array(Image.open(fname)) for fname in df_2585['fullpath']])

white_pix_tot_ = 0
for image in images_2585:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_2585)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_2585:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_2585)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_2585:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_2585)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.5634035757023116
    % des pixels noirs:  0.004856776255633261
    Couleur moyenne RGB :  [210.34162189 208.50850759 205.55865135]



```python
df_1302 = df[df['prdtypecode']==1302]
df_1302 = df_1302.head(20)

images_1302 = np.array([np.array(Image.open(fname)) for fname in df_1302['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_1302[i])
#Equipement camping/pêche
```


    
![png](output_47_0.png)
    



```python
df_1302 = df[df['prdtypecode']==1302]

images_1302 = np.array([np.array(Image.open(fname)) for fname in df_1302['fullpath']])

white_pix_tot_ = 0
for image in images_1302:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_1302)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_1302:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_1302)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_1302:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_1302)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.5256113944503017
    % des pixels noirs:  0.008326311565471306
    Couleur moyenne RGB :  [206.23057955 202.2515228  199.20387045]



```python
df_1281 = df[df['prdtypecode']==1281]
df_1281 = df_1281.head(20)

images_1281 = np.array([np.array(Image.open(fname)) for fname in df_1281['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_1281[i])
#Jouet enfant / Collection carte / Animaux / parfum/ DIVERS
```


    
![png](output_49_0.png)
    



```python
df_1281 = df[df['prdtypecode']==1281]

images_1281 = np.array([np.array(Image.open(fname)) for fname in df_1281['fullpath']])

white_pix_tot_ = 0
for image in images_1281:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_1281)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_1281:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_1281)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_1281:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_1281)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.4418627803837914
    % des pixels noirs:  0.006470853290611341
    Couleur moyenne RGB :  [196.91847581 190.37658281 184.0894689 ]



```python
df_50 = df[df['prdtypecode']==50]
df_50 = df_50.head(20)

images_50 = np.array([np.array(Image.open(fname)) for fname in df_50['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_50[i])
#Jeux video avec intitulé de console
```


    
![png](output_51_0.png)
    



```python
df_50 = df[df['prdtypecode']==50]

images_50 = np.array([np.array(Image.open(fname)) for fname in df_50['fullpath']])

white_pix_tot_ = 0
for image in images_50:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_50)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_50:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_50)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_50:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_50)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.5419373643349491
    % des pixels noirs:  0.006834823033882968
    Couleur moyenne RGB :  [198.77979611 196.19917432 195.40793259]



```python
df_2462 = df[df['prdtypecode']==2462]
df_2462 = df_2462.head(20)

images_2462 = np.array([np.array(Image.open(fname)) for fname in df_2462['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_2462[i])
#Jeux video avec intitulé de console 2
```


    
![png](output_53_0.png)
    



```python
df_2462 = df[df['prdtypecode']==2462]

images_2462 = np.array([np.array(Image.open(fname)) for fname in df_2462['fullpath']])

white_pix_tot_ = 0
for image in images_2462:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_2462)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_2462:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_2462)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_2462:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_2462)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.34072606429580277
    % des pixels noirs:  0.004763972899155912
    Couleur moyenne RGB :  [169.37356314 161.70507774 155.68122158]



```python
df_2905 = df[df['prdtypecode']==2905]
df_2905 = df_2905.head(20)

images_2905 = np.array([np.array(Image.open(fname)) for fname in df_2905['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_2905[i])
#Telechargement Jeux video dématerialisé ( Extension de jeux)
```


    
![png](output_55_0.png)
    



```python
df_2905 = df[df['prdtypecode']==2905]

images_2905 = np.array([np.array(Image.open(fname)) for fname in df_2905['fullpath']])

white_pix_tot_ = 0
for image in images_2905:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_2905)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_2905:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_2905)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_2905:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_2905)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.6303238815722046
    % des pixels noirs:  0.012919191100419511
    Couleur moyenne RGB :  [200.14356212 197.13175394 194.93702039]



```python
df_60 = df[df['prdtypecode']==60]
df_60 = df_60.head(20)

images_60 = np.array([np.array(Image.open(fname)) for fname in df_60['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_60[i])
#Console Jeux video portable
```


    
![png](output_57_0.png)
    



```python
df_60 = df[df['prdtypecode']==60]

images_60 = np.array([np.array(Image.open(fname)) for fname in df_60['fullpath']])

white_pix_tot_ = 0
for image in images_60:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_60)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_60:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_60)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_60:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_60)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.44781113607560713
    % des pixels noirs:  0.00960231473289312
    Couleur moyenne RGB :  [192.76890399 189.2811015  188.78745238]



```python
df_2220 = df[df['prdtypecode']==2220]
df_2220 = df_2220.head(20)

images_2220 = np.array([np.array(Image.open(fname)) for fname in df_2220['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_2220[i])
#Animaux/pets
```


    
![png](output_59_0.png)
    



```python
df_2220 = df[df['prdtypecode']==2220]

images_2220 = np.array([np.array(Image.open(fname)) for fname in df_2220['fullpath']])

white_pix_tot_ = 0
for image in images_2220:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_2220)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_2220:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_2220)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_2220:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_2220)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.5331490102784092
    % des pixels noirs:  0.004794561061569042
    Couleur moyenne RGB :  [210.70336512 205.1240997  202.38616497]



```python
df_1301 = df[df['prdtypecode']==1301]
df_1301 = df_1301.head(20)

images_1301 = np.array([np.array(Image.open(fname)) for fname in df_1301['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_1301[i])
#Habillement bébé enfant garçon fille
```


    
![png](output_61_0.png)
    



```python
df_1301 = df[df['prdtypecode']==1301]

images_1301 = np.array([np.array(Image.open(fname)) for fname in df_1301['fullpath']]) #IMPORTER PLUS PETIT
#Habillement bébé enfant garçon fille

white_pix_tot_ = 0
for image in images_1301:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_1301)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_1301:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_1301)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_1301:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_1301)

print("Couleur moyenne RGB : ", image_mean)
```

    % des pixels blancs:  0.5101167992692418
    % des pixels noirs:  0.00217477062502466
    Couleur moyenne RGB :  [252.757612 252.706628 252.664224]



```python
df_1940 = df[df['prdtypecode']==1940]
df_1940 = df_1940.head(20)

images_1940 = np.array([np.array(Image.open(fname)) for fname in df_1940['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_1940[i])
#Café/Dosette ==> Café/Dosette/Thé
```


    
![png](output_63_0.png)
    



```python
df_1940 = df[df['prdtypecode']==1940]

images_1940 = np.array([np.array(Image.open(fname)) for fname in df_1940['fullpath']])

white_pix_tot_ = 0
for image in images_1940:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_1940)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_1940:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_1940)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_1940:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_1940)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.5454090935648839
    % des pixels noirs:  0.006333295272675407
    Couleur moyenne RGB :  [214.3493057  205.89624731 198.17929848]



```python
df_1180 = df[df['prdtypecode']==1180]
df_1180 = df_1180.head(20)

images_1180 = np.array([np.array(Image.open(fname)) for fname in df_1180['fullpath']])

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_1180[i])
#JEUX DE GUERRE sur TABLE
```


    
![png](output_65_0.png)
    



```python
df_1180 = df[df['prdtypecode']==1180]

images_1180 = np.array([np.array(Image.open(fname)) for fname in df_1180['fullpath']])

white_pix_tot_ = 0
for image in images_1180:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_1180)

print("% des pixels blancs: ", white_pix_tot)

black_pix_tot_ = 0
for image in images_1180:
    n_white_pix = np.sum(image == [0,0,0])/750000
    black_pix_tot += n_white_pix

black_pix_tot = black_pix_tot/len(df_1180)

print("% des pixels noirs: ", black_pix_tot)

image_mean_tot=0

for image in images_1180:
    image_mean = np.mean(image, axis=(0, 1))
    image_mean_tot += image_mean
    
image_mean_tot = image_mean_tot/len(df_1180)

print("Couleur moyenne RGB : ", image_mean_tot)
```

    % des pixels blancs:  0.45159507647499775
    % des pixels noirs:  0.003902973772171911
    Couleur moyenne RGB :  [190.0476498  185.43161412 181.35085259]



```python

```


```python

```


```python

```


```python
#for clas in df['prdtypecode']:
#    print("Classe #: ", clas)
#    images = np.array([np.array(Image.open(fname)) for fname in df[df['prdtypecode']==clas]]['fullpath'].head(20)])
#    fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
#    for i, axi in enumerate(ax.flat):
#        axi.imshow(images[i])
```


```python

```


```python

```


```python
white_pix_tot_ = 0
for image in images_1940:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/20

white_pix_tot
```


```python
rgb_weights = [0.2989, 0.5870, 0.1140]

prod_cat = {}
prod_cat_n = y_train["prdtypecode"].unique()

df_1940 = df[df['prdtypecode']==1940]

white_pix_tot_ = 0

for image in images_1940:
    grayscale_image = np.dot(image[:,:,:3], rgb_weights)
    n_white_pix = np.sum(grayscale_image==255)/250000
    white_pix_tot += n_white_pix

white_pix_tot = white_pix_tot/len(df_1940)

print("Pixels blancs: ", white_pix_tot*100, "%")

black_pix_tot = 0

for image in images_1940:
    grayscale_image = np.dot(image[:,:,:3], rgb_weights)
    n_black_pix = np.sum(grayscale_image==0)/250000
    black_pix_tot += n_black_pix

black_pix_tot = white_pix_tot/len(df_1940)

print("Pixels noirs: ", black_pix_tot*100, "%")
```

    Pixels blancs:  6.2495093786230274e-06 %
    Pixels noirs:  7.78270159230763e-09 %



```python
rgb_weights = [0.2989, 0.5870, 0.1140]

prod_cat = {}
prod_cat_n = y_train["prdtypecode"].unique()

df_2220 = df[df['prdtypecode']==2220]

white_pix_tot_ = 0

for image in images_2220:
    grayscale_image = np.dot(image[:,:,:3], rgb_weights)
    n_white_pix = np.sum(grayscale_image==255)
    white_pix_tot = white_pix_tot+n_white_pix

white_pix_tot = white_pix_tot #/(len(df_2220)*500*500)

print("Pixels blancs: ", white_pix_tot, "%")

black_pix_tot = 0

for image in images_2220:
    grayscale_image = np.dot(image[:,:,:3], rgb_weights)
    n_black_pix = np.sum(grayscale_image==0)
    black_pix_tot =  black_pix_tot+n_black_pix

black_pix_tot = black_pix_tot #/(len(df_2220)*500*500)

print("Pixels noirs: ", black_pix_tot, "%")
grayscale_image.shape
```

    Pixels blancs:  4.211626318821439e-44 %
    Pixels noirs:  119 %





    (500, 500)




```python
images_1301.shape

images_1301_red = images_1301[:,100:400,100:400,:]

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_1301_red[i])
```


    
![png](output_76_0.png)
    



```python
rgb_weights = [0.2989, 0.5870, 0.1140]
images_1301_gray = np.zeros((20,500,500))

for i in range(20):
    grayscale_image = np.dot(images_1301[i,:,:,:3], rgb_weights)
    images_1301_gray[i,:,:]=grayscale_image

images_1301_gray.shape

fig, ax = plt.subplots(4, 5, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(images_1301_gray[i], cmap = 'gray')
```


    
![png](output_77_0.png)
    



```python
images_1301_gray = images_1301_gray.reshape(20,250000)
```


```python
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.manifold import Isomap
from sklearn.feature_selection import SelectPercentile
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

from matplotlib.image import imread
from matplotlib import offsetbox
%matplotlib inline

def plot_components(data, model, images=None, ax=None,
                    thumb_frac=0.05, cmap='gray_r', prefit = False):
    ax = ax or plt.gca()
    
    if not prefit :
        proj = model.fit_transform(data)
    else:
        proj = data
    ax.plot(proj[:, 0], proj[:, 1], '.b')
    
    if images is not None:
        min_dist_2 = (thumb_frac * max(proj.max(0) - proj.min(0))) ** 2
        shown_images = np.array([2 * proj.max(0)])
        for i in range(data.shape[0]):
            dist = np.sum((proj[i] - shown_images) ** 2, 1)
            if np.min(dist) < min_dist_2:
                # On ne montre pas le points trop proches
                continue
            shown_images = np.vstack([shown_images, proj[i]])
            imagebox = offsetbox.AnnotationBbox(
                offsetbox.OffsetImage(images[i], cmap=cmap),
                                      proj[i])
            ax.add_artist(imagebox)
```


```python
fig, ax = plt.subplots(figsize=(50, 500))

plot_components(images_1301_gray,
                model=Isomap(n_components=2),
                images=images_1301_gray.reshape((-1, 500, 500)),
                cmap = 'gray',
                thumb_frac = .01)
```


    
![png](output_80_0.png)
    



```python
import sys                      # System bindings
import cv2                      # OpenCV bindings
import numpy as np
from collections import Counter

class BackgroundColorDetector():
    def __init__(self, imageLoc):
        self.img = cv2.imread(imageLoc, 1)
        self.manual_count = {}
        self.w, self.h, self.channels = self.img.shape
        self.total_pixels = self.w*self.h

    def count(self):
        for y in range(0, self.h):
            for x in range(0, self.w):
                RGB = (self.img[x, y, 2], self.img[x, y, 1], self.img[x, y, 0])
                if RGB in self.manual_count:
                    self.manual_count[RGB] += 1
                else:
                    self.manual_count[RGB] = 1

    def average_colour(self):
        red = 0
        green = 0
        blue = 0
        sample = 10
        for top in range(0, sample):
            red += self.number_counter[top][0][0]
            green += self.number_counter[top][0][1]
            blue += self.number_counter[top][0][2]

        average_red = red / sample
        average_green = green / sample
        average_blue = blue / sample
        print("Average RGB for top ten is: (", average_red,
              ", ", average_green, ", ", average_blue, ")")
        

    def twenty_most_common(self):
        self.count()
        self.number_counter = Counter(self.manual_count).most_common(20)
        for rgb, value in self.number_counter:
            print(rgb, value, ((float(value)/self.total_pixels)*100))

    def detect(self):
        self.twenty_most_common()
        self.percentage_of_first = (
            float(self.number_counter[0][1])/self.total_pixels)
        print(self.percentage_of_first)
        if self.percentage_of_first > 0.5:
            print("Background color is ", self.number_counter[0][0])
        else:
            self.average_colour()


if __name__ == "__main__":
    if (len(sys.argv) != 2):                        # Checks if image was given as cli argument
        print("error: syntax is 'python main.py /example/image/location.jpg'")
    else:
        BackgroundColor = BackgroundColorDetector(sys.argv[1])
        BackgroundColor.detect()
```

    error: syntax is 'python main.py /example/image/location.jpg'



```python
img_color = cv2.imread('/Users/ayseaylinkaya/Desktop/Datascientist/Project Rakuten/images/image_train/image_1261419198_product_3898725495.jpg', cv2.IMREAD_COLOR)
img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

plt.figure(figsize = (8,5))
plt.imshow(img_color)
plt.xticks([])
plt.yticks([])

plt.show();
```


    
![png](output_82_0.png)
    



```python
BC = BackgroundColorDetector('/Users/ayseaylinkaya/Desktop/Datascientist/Project Rakuten/images/image_train/image_1261419198_product_3898725495.jpg')
```


```python
most_common = BC.twenty_most_common()
most_common

average_colour = BC.average_colour()
average_colour
```

    (255, 255, 255) 166978 66.79119999999999
    (254, 255, 255) 1739 0.6956
    (255, 254, 255) 1670 0.668
    (255, 255, 253) 1148 0.4592
    (252, 255, 255) 850 0.33999999999999997
    (255, 253, 255) 531 0.2124
    (254, 255, 253) 477 0.1908
    (251, 255, 255) 374 0.14959999999999998
    (255, 255, 251) 362 0.1448
    (255, 254, 253) 265 0.106
    (252, 255, 253) 226 0.0904
    (249, 255, 255) 196 0.0784
    (255, 254, 251) 193 0.0772
    (254, 254, 254) 164 0.0656
    (255, 252, 255) 157 0.0628
    (254, 255, 251) 123 0.0492
    (251, 255, 253) 118 0.0472
    (255, 253, 253) 116 0.0464
    (255, 255, 250) 112 0.0448
    (248, 255, 255) 105 0.042
    Average RGB for top ten is: ( 254.1 ,  254.6 ,  254.0 )



```python

```


```python

```


```python

```
