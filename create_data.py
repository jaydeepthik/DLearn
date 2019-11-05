# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 15:27:26 2019

@authors: jaydeep thik , Vasudev Purandare
"""

import pandas as pd
import numpy as np
from PIL import Image

def generate():
    data_folder = "./hackdataset"
    df = pd.read_csv("./fer2013/fer2013.csv")
    
    train_samples = df[df['Usage']=="Training"]
    validation_samples = df[df["Usage"]=="PublicTest"]
    test_samples = df[df["Usage"]=="PrivateTest"]
    
    y_train = train_samples.emotion.astype(np.int32).values
    y_valid = validation_samples.emotion.astype(np.int32).values
    y_test = test_samples.emotion.astype(np.int32).values
    i=0
    for image, label in zip(train_samples.pixels, y_train):
        #print(label)
        img_array = np.fromstring(image, np.uint8, sep=" ").reshape((48,48))
        if label==0:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/train/Angry/A_'+str(i)+'.jpg')
            i+=1
    
        elif label==1:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/train/Disgust/D_'+str(i)+'.jpg')
            i+=1
            
        elif label==2:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/train/Fear/F_'+str(i)+'.jpg')
            i+=1
        elif label==3:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/train/Happy/H_'+str(i)+'.jpg')
            i+=1
        
        elif label==4:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/train/Sad/S_'+str(i)+'.jpg')
            i+=1
        elif label==5:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/train/Surprise/S_'+str(i)+'.jpg')
            i+=1
        elif label==6:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/train/Tran/T_'+str(i)+'.jpg')
            i+=1
        print(i)  
            
    for image, label in zip(test_samples.pixels, y_test):
        #print(label)
        img_array = np.fromstring(image, np.uint8, sep=" ").reshape((48,48))
        if label==0:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/test/Angry/A_'+str(i)+'.jpg')
            i+=1
    
        elif label==1:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/test/Disgust/D_'+str(i)+'.jpg')
            i+=1
            
        elif label==2:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/test/Fear/F_'+str(i)+'.jpg')
            i+=1
        elif label==3:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/test/Happy/H_'+str(i)+'.jpg')
            i+=1
        
        elif label==4:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/test/Sad/S_'+str(i)+'.jpg')
            i+=1
        elif label==5:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/test/Surprise/S_'+str(i)+'.jpg')
            i+=1
        elif label==6:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/test/Tran/T_'+str(i)+'.jpg')
            i+=1
        print(i)
    
    for image, label in zip(validation_samples.pixels, y_valid):
       # print(label)
        img_array = np.fromstring(image, np.uint8, sep=" ").reshape((48,48))
        if label==0:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/valid/Angry/A_'+str(i)+'.jpg')
            i+=1
    
        elif label==1:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/valid/Disgust/D_'+str(i)+'.jpg')
            i+=1
            
        elif label==2:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/valid/Fear/F_'+str(i)+'.jpg')
            i+=1
        elif label==3:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/valid/Happy/H_'+str(i)+'.jpg')
            i+=1
        
        elif label==4:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/valid/Sad/S_'+str(i)+'.jpg')
            i+=1
        elif label==5:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/valid/Surprise/S_'+str(i)+'.jpg')
            i+=1
        elif label==6:
            
            im = Image.fromarray(img_array, 'L')
            im.save(data_folder+'/valid/Tran/T_'+str(i)+'.jpg')
            i+=1
    #X_train =np.array([ np.fromstring(image, np.uint8, sep=" ").reshape((48,48)) for image in train_samples.pixels])
    #X_valid =np.array([ np.fromstring(image, np.uint8, sep=" ").reshape((48,48)) for image in validation_samples.pixels])
    #X_test =np.array([ np.fromstring(image, np.uint8, sep=" ").reshape((48,48)) for image in test_samples.pixels])
    
        print(i)
    #return X_train, y_train, X_valid, y_valid, X_test, y_test