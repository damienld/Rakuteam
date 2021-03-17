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
X_train = pd.read_csv("/Users/ayseaylinkaya/Desktop/Datascientist/2 Project Rakuten/X_train_update.csv") 
X_test = pd.read_csv("/Users/ayseaylinkaya/Desktop/Datascientist/2 Project Rakuten/X_test_update.csv") 
y_train = pd.read_csv("/Users/ayseaylinkaya/Desktop/Datascientist/2 Project Rakuten/Y_train_CVw08PX.csv")
df_image= pd.read_csv("/Users/ayseaylinkaya/Desktop/Datascientist/2 Project Rakuten/features_images.csv")
```


```python
#merge les training sets pour analyses les articles par classe
X_train = X_train.sort_values(by = 'Unnamed: 0', ascending = True)
y_train = y_train.sort_values(by = 'Unnamed: 0', ascending = True)
part2 = X_train[X_train.columns[3:]]
df = pd.concat([y_train,part2], axis=1)
df["image_name"] = "image_" + df.imageid.map(str)+ "_product_" + df.productid.map(str) + ".jpg"
df["image_name"] = df["image_name"].astype(str)
df['fullpath']= '/Users/ayseaylinkaya/Desktop/Datascientist/2 Project Rakuten/images/image_train/'+ df['image_name']
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
      <td>/Users/ayseaylinkaya/Desktop/Datascientist/2 P...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2280</td>
      <td>436067568</td>
      <td>1008141237</td>
      <td>image_1008141237_product_436067568.jpg</td>
      <td>/Users/ayseaylinkaya/Desktop/Datascientist/2 P...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>50</td>
      <td>201115110</td>
      <td>938777978</td>
      <td>image_938777978_product_201115110.jpg</td>
      <td>/Users/ayseaylinkaya/Desktop/Datascientist/2 P...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>1280</td>
      <td>50418756</td>
      <td>457047496</td>
      <td>image_457047496_product_50418756.jpg</td>
      <td>/Users/ayseaylinkaya/Desktop/Datascientist/2 P...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>2705</td>
      <td>278535884</td>
      <td>1077757786</td>
      <td>image_1077757786_product_278535884.jpg</td>
      <td>/Users/ayseaylinkaya/Desktop/Datascientist/2 P...</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_image.shape
```




    (80014, 11)




```python
df_2905 = df[df['prdtypecode']==2905]

images_2905 = np.array([np.array(Image.open(fname)) for fname in df_2905['fullpath']])

blanc = []
noir = []
R = []
G = []
B = []

for image in images_2905:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    n_black_pix = np.sum(image == [0,0,0])/750000
    image_mean = np.mean(image, axis=(0, 1))
    blanc.append(n_white_pix)
    noir.append(n_black_pix)
    R.append(image_mean[0])
    G.append(image_mean[1])
    B.append(image_mean[2])

df_2905['blanc']=blanc
df_2905['noir']=noir
df_2905['R']= R
df_2905['G']= G
df_2905['B']= B


df_image = pd.concat([df_image, df_2905])
df_image.to_csv(index=False)
df_image.shape
```

    <ipython-input-7-6898b955ee28>:21: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_2905['blanc']=blanc
    <ipython-input-7-6898b955ee28>:22: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_2905['noir']=noir
    <ipython-input-7-6898b955ee28>:23: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_2905['R']= R
    <ipython-input-7-6898b955ee28>:24: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_2905['G']= G
    <ipython-input-7-6898b955ee28>:25: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_2905['B']= B





    (80886, 11)




```python
df_60 = df[df['prdtypecode']==60]

images_60 = np.array([np.array(Image.open(fname)) for fname in df_60['fullpath']])

blanc = []
noir = []
R = []
G = []
B = []

for image in images_60:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    n_black_pix = np.sum(image == [0,0,0])/750000
    image_mean = np.mean(image, axis=(0, 1))
    blanc.append(n_white_pix)
    noir.append(n_black_pix)
    R.append(image_mean[0])
    G.append(image_mean[1])
    B.append(image_mean[2])

df_60['blanc']=blanc
df_60['noir']=noir
df_60['R']= R
df_60['G']= G
df_60['B']= B


df_image = pd.concat([df_image, df_60])
df_image.to_csv(index=False)
df_image.shape
```

    <ipython-input-8-74ca7b63038f>:21: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_60['blanc']=blanc
    <ipython-input-8-74ca7b63038f>:22: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_60['noir']=noir
    <ipython-input-8-74ca7b63038f>:23: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_60['R']= R
    <ipython-input-8-74ca7b63038f>:24: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_60['G']= G
    <ipython-input-8-74ca7b63038f>:25: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_60['B']= B





    (81718, 11)




```python
df_2220 = df[df['prdtypecode']==2220]

images_2220 = np.array([np.array(Image.open(fname)) for fname in df_2220['fullpath']])

blanc = []
noir = []
R = []
G = []
B = []

for image in images_2220:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    n_black_pix = np.sum(image == [0,0,0])/750000
    image_mean = np.mean(image, axis=(0, 1))
    blanc.append(n_white_pix)
    noir.append(n_black_pix)
    R.append(image_mean[0])
    G.append(image_mean[1])
    B.append(image_mean[2])

df_2220['blanc']=blanc
df_2220['noir']=noir
df_2220['R']= R
df_2220['G']= G
df_2220['B']= B


df_image = pd.concat([df_image, df_2220])
df_image.to_csv(index=False)
df_image.shape
```

    <ipython-input-9-05c2aedd7036>:21: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_2220['blanc']=blanc
    <ipython-input-9-05c2aedd7036>:22: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_2220['noir']=noir
    <ipython-input-9-05c2aedd7036>:23: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_2220['R']= R
    <ipython-input-9-05c2aedd7036>:24: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_2220['G']= G
    <ipython-input-9-05c2aedd7036>:25: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_2220['B']= B





    (82542, 11)




```python
df_1301 = df[df['prdtypecode']==1301]

images_1301 = np.array([np.array(Image.open(fname)) for fname in df_1301['fullpath']])

blanc = []
noir = []
R = []
G = []
B = []

for image in images_1301:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    n_black_pix = np.sum(image == [0,0,0])/750000
    image_mean = np.mean(image, axis=(0, 1))
    blanc.append(n_white_pix)
    noir.append(n_black_pix)
    R.append(image_mean[0])
    G.append(image_mean[1])
    B.append(image_mean[2])

df_1301['blanc']=blanc
df_1301['noir']=noir
df_1301['R']= R
df_1301['G']= G
df_1301['B']= B


df_image = pd.concat([df_image, df_1301])
df_image.to_csv(index=False)
df_image.shape
```

    <ipython-input-10-f5f8a0101947>:21: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_1301['blanc']=blanc
    <ipython-input-10-f5f8a0101947>:22: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_1301['noir']=noir
    <ipython-input-10-f5f8a0101947>:23: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_1301['R']= R
    <ipython-input-10-f5f8a0101947>:24: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_1301['G']= G
    <ipython-input-10-f5f8a0101947>:25: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_1301['B']= B





    (83349, 11)




```python
df_1180 = df[df['prdtypecode']==1180]

images_1180 = np.array([np.array(Image.open(fname)) for fname in df_1180['fullpath']])

blanc = []
noir = []
R = []
G = []
B = []

for image in images_1180:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    n_black_pix = np.sum(image == [0,0,0])/750000
    image_mean = np.mean(image, axis=(0, 1))
    blanc.append(n_white_pix)
    noir.append(n_black_pix)
    R.append(image_mean[0])
    G.append(image_mean[1])
    B.append(image_mean[2])

df_1180['blanc']=blanc
df_1180['noir']=noir
df_1180['R']= R
df_1180['G']= G
df_1180['B']= B


df_image = pd.concat([df_image, df_1180])
df_image.to_csv(index=False)
df_image.shape
```

    <ipython-input-11-8def9edb200c>:21: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_1180['blanc']=blanc
    <ipython-input-11-8def9edb200c>:22: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_1180['noir']=noir
    <ipython-input-11-8def9edb200c>:23: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_1180['R']= R
    <ipython-input-11-8def9edb200c>:24: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_1180['G']= G
    <ipython-input-11-8def9edb200c>:25: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_1180['B']= B





    (84113, 11)




```python
df_1940 = df[df['prdtypecode']==1940]

images_1940 = np.array([np.array(Image.open(fname)) for fname in df_1940['fullpath']])

blanc = []
noir = []
R = []
G = []
B = []

for image in images_1940:
    n_white_pix = np.sum(image == [255, 255, 255])/750000
    n_black_pix = np.sum(image == [0,0,0])/750000
    image_mean = np.mean(image, axis=(0, 1))
    blanc.append(n_white_pix)
    noir.append(n_black_pix)
    R.append(image_mean[0])
    G.append(image_mean[1])
    B.append(image_mean[2])

df_1940['blanc']=blanc
df_1940['noir']=noir
df_1940['R']= R
df_1940['G']= G
df_1940['B']= B


df_image = pd.concat([df_image, df_1940])
df_image.to_csv(index=False)
df_image.shape
```

    <ipython-input-12-1668ba26c42a>:21: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_1940['blanc']=blanc
    <ipython-input-12-1668ba26c42a>:22: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_1940['noir']=noir
    <ipython-input-12-1668ba26c42a>:23: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_1940['R']= R
    <ipython-input-12-1668ba26c42a>:24: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_1940['G']= G
    <ipython-input-12-1668ba26c42a>:25: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df_1940['B']= B





    (84916, 11)




```python
X_train.shape
```




    (84916, 5)




```python
df_image.columns
```




    Index(['Unnamed: 0', 'prdtypecode', 'productid', 'imageid', 'image_name',
           'fullpath', 'blanc', 'noir', 'R', 'G', 'B'],
          dtype='object')




```python
#df_image = df_image.drop(['Unnamed: 0', 'imageid', 'image_name', 'fullpath'], axis=1)
df_image.to_csv('df_features_images.csv',index=False)
```


```python

```


```python

```
