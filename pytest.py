import numpy as np
import cv2
import matplotlib.pyplot as plt
from pynput.mouse import Button, Controller

# Setup the haarcascades for testing gestures
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
right_eye_cascade = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')
left_eye_cascade = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
profile_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
cap = cv2.VideoCapture(0)

# Begin working on the mouse input MVP
mouse = Controller()

# Define default points so that we can move the mouse

prevy = 0
prevx = 0
tick = 0


# Render the cap with bounding boxes around the desired areas
while True:
    # Initialize the stream and settings
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Face detection
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0) ,2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        # print(mouse.position[1])
        diff = x - prevx
        if(tick > 10):
            prevx = x
            if(diff > 10 or diff < -10):
                mouse.move( diff, 0 )
                print(diff)
                tick = 0
        print(diff)
        tick += 1

        smiles = smile_cascade.detectMultiScale(roi_gray)
        for (ax,ay,aw,ah) in smiles:
            cv2.rectangle(roi_color,(ax,ay), (ax+aw, ay+ah), (0,0,255) ,2)
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0) ,2)
    
    # Eye Detection
    # eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    # for (ex,ey,ew,eh) in eyes:
    #     cv2.rectangle(img, (ex,ey), (ex+ew, ey+eh), (0,255,0) ,2)

    # Right Eye Detection
    reyes = right_eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (ex,ey,ew,eh) in reyes:
        mouse.move(5,0)
        cv2.rectangle(img, (ex,ey), (ex+ew, ey+eh), (255,255,0) ,2)

    # Left Eye Detection
    leyes = left_eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (ex,ey,ew,eh) in leyes:
        mouse.move(-5,0)
        cv2.rectangle(img, (ex,ey), (ex+ew, ey+eh), (0,255,255) ,2)
    # smiles = smile_cascade.detectMultiScale(gray, 1.3, 5)
    # for (ax,ay,aw,ah) in smiles:
    #     cv2.rectangle(img,(ax,ay), (ax+aw, ay+ah), (0,0,255) ,2)

    # Profile Detection
    profiles = profile_cascade.detectMultiScale(gray, 1.3, 5)
    for (ex,ey,ew,eh) in profiles:
        cv2.rectangle(img, (ex,ey), (ex+ew, ey+eh), (255,255,0) ,2)
        mouse.click(Button.left, 1)


    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# Capture for single picture
# img = cv2.imread('images.jpg', cv2.IMREAD_GRAYSCALE)

#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# fourcc = cv2.VideoWriter_fourcc(*'XID')
# out = cv2.VideoWriter('ourput.avi', forcc, 20.0, (640,480))

# Capture video
#cap  = cv2.VideoCapture(0)
#while True:
#    ret, frame = cap.read()
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #out.write(frame)
#    cv2.imshow("frame", gray)

#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break

cap.release()
#out.release()
cv2.destroyAllWindows()