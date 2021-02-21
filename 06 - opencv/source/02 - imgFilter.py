import cv2
import numpy as np

img = cv2.imread("bahan/sepi.jpg")

# resize image
scale_persent = 75

width = int(img.shape[1]*scale_persent / 100)
height = int(img.shape[0]*scale_persent / 100)
dsize = (width,height)

resize_img = cv2.resize(img,dsize)

# make layers image
karnel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(resize_img,150,200)
imgDialation = cv2.dilate(imgCanny,karnel,iterations=1)
imgEroded = cv2.erode(imgDialation,karnel,iterations=1)

cv2.imshow("Gray image", imgGray)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dialation image", imgDialation)
cv2.imshow("Eroded image", imgEroded)
cv2.waitKey(0)