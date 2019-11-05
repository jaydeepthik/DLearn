# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 23:26:06 2019

@authors: jaydeep thik , Vasudev Purandare
"""

from tensorflow import keras
import numpy as np
import cv2
import time

#emotion =  ['Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
emotion =  ['Confused', 'Happy', 'Stressed', 'Tran']


font = cv2.FONT_HERSHEY_SIMPLEX
face_cas = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')

def cam_run():
    lab = [-1]*20
    cam = cv2.VideoCapture(0)
    model = keras.models.load_model("new_model_f1.h5")        
    model._make_predict_function()
    start = time.time()
    
    while True:
        
        ret, frame = cam.read()
        
        if ret==True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #gray = cv2.flip(gray,1)
            faces = face_cas.detectMultiScale(gray, 1.3,5)
            
            for (x, y, w, h) in faces:
                face_component = gray[y:y+h, x:x+w]
                fc = cv2.resize(face_component, (48, 48))
                #cv2.imshow("fc", face_component)
                inp = np.reshape(fc,(1,48,48,1)).astype(np.float32)
                inp = inp/255.
                prediction = model.predict_proba(inp)
                
                em = emotion[np.argmax(prediction)]
                
                del[lab[0]]
                lab.append(em)
                #print()   
                if (lab.count("Stressed") + lab.count("Confused")) >15: # change
                    cam.release()
                    cv2.destroyAllWindows()
                    keras.backend.clear_session()
                    end = time.time() -  start
                    return "confused", end
                
                score = np.max(prediction)
                cv2.putText(frame, em+"  "+str(score*100)+'%', (x, y), font, 1, (0, 255, 0), 2)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.imshow("image", frame)
            
            if cv2.waitKey(1) == 27:
                break
        else:
            print ('Error')
    
    cam.release()
    cv2.destroyAllWindows()
    keras.backend.clear_session()
    
    
if __name__=="__main__":
    cam_run()