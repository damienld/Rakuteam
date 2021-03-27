# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:45:33 2021

@author: slam_
"""

import numpy as np
import pandas as pd
import cv2
from PIL import Image
from keras.models import load_model
from utils import image_url_to_numpy_array_skimage

def Cnnimage_predict(imgpath):
    X_img=[]

    # Load image
    
    #file_bytes = np.asarray(bytearray(imgpath.read()), dtype=np.uint8)
    #img=cv2.imread(imgpath)
    if (imgpath.startswith("http")):
        img=image=image_url_to_numpy_array_skimage(imgpath)
    else:
        img = np.array(Image.open(imgpath))
    #img = Image.open(imgpath)
    # Resize image
    print(img.shape)
    img=cv2.resize(img,(224,224))
    # for the black and white image
    if img.shape==(224, 224):
        img=img.reshape([224,224,1])
        img=np.concatenate([img,img,img],axis=2)
        # cv2 load the image BGR sequence color (not RGB)
    X_img.append(img[...,::-1])
    
    image = np.array(X_img)
    
    model = load_model("model_image_all.06-1.20.h5")
    y_pred_proba = model.predict(image)
    y_pred_df = pd.DataFrame(y_pred_proba)
    
    y_pred_df_1=y_pred_df.iloc[:,0:2]
    y_pred_df_2=y_pred_df.iloc[:,12]
    y_pred_df_3=y_pred_df.iloc[:,20:27]
    y_pred_df_4=y_pred_df.iloc[:,2:12]
    y_pred_df_5=y_pred_df.iloc[:,13:20]
    y_pred_dff = pd.concat([y_pred_df_1,y_pred_df_2,y_pred_df_3,y_pred_df_4,y_pred_df_5], axis=1)
    
    y_pred_proba = y_pred_dff.to_numpy()
    return (y_pred_proba)

Cnnimage_predict("test2.jpg")