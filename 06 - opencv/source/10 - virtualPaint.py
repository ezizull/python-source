import cv2
import numpy as np

cap = cv2.VideoCapture(1) # webcam
cap.set(10,60)

def ubah_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

myColor = [[92,109,104,255,156,255],
           [0,176,133,255,141,255],
           []]

def find_color(img):
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHsv, lower,upper)
    cv2.imshow(mask)

while True:
    success, img = cap.read()
    frame75 = ubah_frame(img, percent=75)
    cv2.imshow("video", frame75)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
