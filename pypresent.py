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

# Previous position holder
prevx = 0
prevy = 0
diffx = 0
diffy = 0
# def capture_voice():
#     while True:
#         with mic as source:
#             audio = r.listen(source)
#         try:
#             if r.recognize_sphinx(audio) == 'twenty':
#                 mouse.click(Button.left, 1)
        
#         except LookupError:
#             print("Could not understand audio")

while True:
    # Initialize the stream and settings
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Begin new thread
    # if i > 150:
    #     thread.start_new_thread( capture_voice, ( ))
    #     i = 0
    # i += 1
    # print(i)
    # Eye Detection
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (ex,ey,ew,eh) in eyes:
        # print(prevx)
        # print(prevy)
        diffx = prevx - ex
        diffy = prevy - ey 
        prevx = ex
        prevy = ey

        if diffx > 5 and diffx < 50:
            # print(diffx)
            mouse.move(diffx , 0)
        if diffx < -5 and diffx > -50:
            # print(diffx)
            mouse.move(diffx , 0)
        if diffy > 5  and diffy < 50:   
            # print(diffy)
            mouse.move(0 , diffy)
        if diffy < -5  and diffy > -50:   
            # print(diffy)
            mouse.move(0 , diffy)
        else:
            print(diffy)
        cv2.rectangle(img, (ex,ey), (ex+ew, ey+eh), (0,255,0) ,2)
    
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