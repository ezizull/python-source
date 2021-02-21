import cv2
import numpy as np

faseCascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

path = "bahan/muka.jpg"
img = cv2.imread(path)
imgResize = cv2.resize(img,(320,400))

imgGray = cv2.cvtColor(imgResize,cv2.COLOR_BGR2GRAY)

faces = faseCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(imgResize,(x,y),(x+w,y+h),(255,100,0),2)

cv2.imshow("img",imgResize)

cv2.waitKey(0)