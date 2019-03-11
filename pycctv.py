import numpy as np
import _thread as thread
import cv2
import matplotlib.pyplot as plt
import speech_recognition as sr
from pynput.mouse import Button, Controller
cap = cv2.VideoCapture(0)
mouse = Controller()
mic = sr.Microphone()
r = sr.Recognizer()
profile_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
profile_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
i = 0

# values for point of ref
# ex 344
# ey 229
#
# Previous position holder
prevx = 300
prevy = 200
diffx = 0
diffy = 0
tick = 0
img_counter = 0

while True:
    # Initialize the stream and settings
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    profiles = profile_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (ex,ey,ew,eh) in profiles:
        
        cv2.rectangle(img, (ex,ey), (ex+ew, ey+eh), (255,255,0) ,2)

    for (x,y,w,h) in faces:        
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0) ,2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        # smiles = smile_cascade.detectMultiScale(roi_gray)
        # for (ax,ay,aw,ah) in smiles:
        #     cv2.rectangle(roi_color,(ax,ay), (ax+aw, ay+ah), (0,0,255) ,2)
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0) ,2)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, img)
        img_counter += 1
    
    tick +=1

    print(tick)

cap.release()
cv2.destroyAllWindows()