import numpy as np
import cv2
import matplotlib.pyplot as plt
from pynput.mouse import Button, Controller


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('ourput.avi', fourcc, 20.0, (640,480))


# while True:
#     # Initialize the stream and settings
#     ret, img = cap.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Face detection
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0) ,2)
#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = img[y:y+h, x:x+w]


# Capture video
while True:
   ret, frame = cap.read()
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   out.write(frame)
   cv2.imshow("frame", gray)

   if cv2.waitKey(1) & 0xFF == ord('q'):
       break

cap.release()
out.release()
cv2.destroyAllWindows()