# -*- coding: utf-8 -*-
"""4_Model_Reseaux_Text.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TWC2hdXarDgK2d8rVHIh5eIrnf9FJHfW
"""
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import pickle
from cleaning import clean_manualdata
import constants
#from keras.utils.data_utils import get_file
#import requests

def Dnntexte_predict(desi, desc):
    dfmanual=clean_manualdata(desi,desc)
    dfmanual['sentences'] = dfmanual['designation'] + " " + dfmanual['description']
    sentences_test = dfmanual['sentences']
    with open(constants.path+'tokenizer_dnn.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    X_test = tokenizer.texts_to_sequences(sentences_test)
    maxlen = 400#defautl was 250, best 400
    X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)

    #url = "https://drive.google.com/u/1/open?id=1es-p47fLuDD-BLJQqdOYJgLbkF6xoubp" 
    #download = requests.get(url).content    
    #print("downloaded hdf5")
    #model = load_model(download)
    model = load_model(constants.path+"text-dnn.hdf5") 
   
    ypred_proba=model.predict(X_test)
    
    #score = model.evaluate(X_test, y_test, verbose = 0) 
    #print('Test loss:', score[0]) 
    #print('Test accuracy:', score[1])
    return (ypred_proba)


"""
loss, accuracy = model.evaluate(X_train, y_train, verbose=False)
print("Training Accuracy: {:.4f}".format(accuracy))
loss, accuracy = model.evaluate(X_test, y_test, verbose=False)
print("Testing Accuracy:  {:.4f}".format(accuracy))
plot_history(history)

df_tosave=pd.DataFrame(ypred_proba)
path = '/Drive/My Drive/Projet Rakuten'
df_tosave.to_csv(f'{path}/ypred_proba_DnnText_score0_82.csv')
"""