# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 22:08:56 2021

@author: Dam
"""
import numpy as np
from skimage import io

def image_url_to_numpy_array_skimage(url,format=None):
    
    image = io.imread(url)
    image = np.asarray(image, dtype="uint8")
    if format=='BGR' :
        ## return BGR format array
        return image[...,[2,1,0]]
    return image