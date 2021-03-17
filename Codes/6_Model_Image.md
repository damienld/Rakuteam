```python
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import time, cv2
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.layers import Dense, Dropout, Flatten, GlobalAveragePooling2D
from keras.optimizers import Adam
from keras.models import Model, Sequential
from keras.preprocessing.image import ImageDataGenerator
import keras
from keras import backend as K
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import VGG16
```


```python
#télécharger les datasets
X_train = pd.read_csv("/Users/ayseaylinkaya/Desktop/Datascientist/2 Project Rakuten/X_train_update.csv") 
X_test = pd.read_csv("/Users/ayseaylinkaya/Desktop/Datascientist/2 Project Rakuten/X_test_update.csv") 
y_train = pd.read_csv("/Users/ayseaylinkaya/Desktop/Datascientist/2 Project Rakuten/Y_train_CVw08PX.csv")
```


```python
#fusionner les training sets pour analyser les articles par classe
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
df['class'] = df['prdtypecode']

df = df.replace({'class': {10: 1, 2280:2,   50:3, 1280:4, 2705:5, 2522:6, 2582:7, 1560:8, 1281:9, 1920:10, 2403:11,
       1140:12, 2583:13, 1180:14, 1300:15, 2462:16, 1160:17, 2060:18,   40:19,   60:20, 1320:21, 1302:22,
       2220:23, 2905:24, 2585:25, 1940:26, 1301:0}})
```


```python
data = df.drop(["Unnamed: 0","prdtypecode", "imageid", "image_name"], axis=1)
data.head()
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
      <th>productid</th>
      <th>fullpath</th>
      <th>class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3804725264</td>
      <td>/Users/ayseaylinkaya/Desktop/Datascientist/2 P...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>436067568</td>
      <td>/Users/ayseaylinkaya/Desktop/Datascientist/2 P...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>201115110</td>
      <td>/Users/ayseaylinkaya/Desktop/Datascientist/2 P...</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>50418756</td>
      <td>/Users/ayseaylinkaya/Desktop/Datascientist/2 P...</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>278535884</td>
      <td>/Users/ayseaylinkaya/Desktop/Datascientist/2 P...</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_train, data_test = train_test_split(data, test_size = 0.2, random_state = 123)
```


```python
train_data_generator = ImageDataGenerator(preprocessing_function = preprocess_input)
test_data_generator = ImageDataGenerator(preprocessing_function = preprocess_input)

batch_size = 32
data_train["class"] = data_train["class"].astype(str)
data_test["class"] = data_test["class"].astype(str)

train_generator = train_data_generator.flow_from_dataframe(dataframe=data_train,
                                                           directory="",
                                                           x_col = "fullpath",
                                                           class_mode ="sparse",
                                                           target_size = (224 , 224),
                                                           zoom_range = [0.5,1.0],
                                                           batch_size = batch_size)

test_generator = test_data_generator.flow_from_dataframe(dataframe=data_test,
                                                         directory="",
                                                         x_col = "fullpath",
                                                         class_mode ="sparse",
                                                         target_size = (224,224), 
                                                         batch_size = batch_size,
                                                         shuffle = False)
```

    <ipython-input-12-56dd82ff4b0e>:5: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      data_train["class"] = data_train["class"].astype(str)
    <ipython-input-12-56dd82ff4b0e>:6: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      data_test["class"] = data_test["class"].astype(str)


    Found 67932 validated image filenames belonging to 27 classes.
    Found 16984 validated image filenames belonging to 27 classes.



```python
base_model = VGG16(weights='imagenet', include_top=False)

for layer in base_model.layers: 
    layer.trainable = False

model = Sequential()

model.add(base_model) 

model.add(GlobalAveragePooling2D())
model.add(Dense(1024,activation='relu'))

model.add(Dropout(rate=0.2))
model.add(Dense(512, activation='relu'))

model.add(Dropout(rate=0.2))
model.add(Dense(27, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])
model.summary()
```

    Model: "sequential_1"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    vgg16 (Functional)           (None, None, None, 512)   14714688  
    _________________________________________________________________
    global_average_pooling2d_1 ( (None, 512)               0         
    _________________________________________________________________
    dense_3 (Dense)              (None, 1024)              525312    
    _________________________________________________________________
    dropout_2 (Dropout)          (None, 1024)              0         
    _________________________________________________________________
    dense_4 (Dense)              (None, 512)               524800    
    _________________________________________________________________
    dropout_3 (Dropout)          (None, 512)               0         
    _________________________________________________________________
    dense_5 (Dense)              (None, 27)                13851     
    =================================================================
    Total params: 15,778,651
    Trainable params: 1,063,963
    Non-trainable params: 14,714,688
    _________________________________________________________________



```python
from keras.callbacks import EarlyStopping, ModelCheckpoint

my_callbacks = [
    EarlyStopping(monitor = 'val_loss', patience = 3, mode = 'min', restore_best_weights = True),
    ModelCheckpoint(filepath='/Users/ayseaylinkaya/Desktop/Datascientist/2 Project Rakuten/model_image.{epoch:02d}-{val_loss:.2f}.h5'),
]
```


```python
history = model.fit_generator(generator=train_generator, 
                                epochs = 5,
                                steps_per_epoch = len(data_train)//batch_size,
                                validation_data = test_generator,
                                validation_steps = len(data_test)//batch_size,
                                callbacks=my_callbacks)
```

    /opt/anaconda3/lib/python3.8/site-packages/tensorflow/python/keras/engine/training.py:1844: UserWarning: `Model.fit_generator` is deprecated and will be removed in a future version. Please use `Model.fit`, which supports generators.
      warnings.warn('`Model.fit_generator` is deprecated and '


    Epoch 1/5
      66/2122 [..............................] - ETA: 2:32:39 - loss: 4.1992 - acc: 0.1772


```python
plt.figure(figsize=(12,4))
plt.subplot(121)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss by epoch')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='right')
plt.subplot(122)
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model acc by epoch')
plt.ylabel('acc')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='right')
plt.show()
```


    
![png](output_10_0.png)
    

