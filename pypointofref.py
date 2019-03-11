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
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
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


while True:
    # Initialize the stream and settings
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   
    # Eye Detection
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (ex,ey,ew,eh) in eyes:
    
        diffx = prevx - ex
        diffy = prevy - ey 
    
        print("diffx",diffx)
        print("diffy",diffy)
        


        if diffx > 50 and diffx < 100:
            # print(diffx)
            mouse.move(15, 0)
        if diffx < -50 and diffx > -100:
            # print(diffx)
            mouse.move(-15 , 0)
        if diffy > 20  and diffy < 100:   
            print(diffy)
            mouse.move(0 , -10 )
        if diffy < -20  and diffy > -100:   
            print(diffy)
            mouse.move(0 , 10)
        cv2.rectangle(img, (ex,ey), (ex+ew, ey+eh), (0,255,0) ,2)
    # cv2.circle(img, (prevx,prevy), 100, color[, thickness[, lineType[, shift]]])
    cv2.rectangle(img, (prevx -25,prevy - 15), (prevx + 25, prevy + 15), (0,255,0) ,2)
    
    # Right Eye Detection
    # reyes = right_eye_cascade.detectMultiScale(gray, 1.3, 5)
    # for (ex,ey,ew,eh) in reyes:
    #     mouse.move(5,0)
    #     cv2.rectangle(img, (ex,ey), (ex+ew, ey+eh), (255,255,0) ,2)

    # Left Eye Detection
    # leyes = left_eye_cascade.detectMultiScale(gray, 1.3, 5)
    # for (ex,ey,ew,eh) in leyes:
    #     mouse.move(-5,0)
    #     cv2.rectangle(img, (ex,ey), (ex+ew, ey+eh), (0,255,255) ,2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()