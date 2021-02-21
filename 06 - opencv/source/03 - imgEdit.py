import cv2
import numpy as np

img = cv2.imread("bahan/sepi.jpg")
print(img.shape)

imgResize = cv2.resize(img, (320, 223)) # width, hight
print(imgResize.shape)

imgCropped = img[0:200, 200:500] # hight, width

cv2.imshow("image", img)
cv2.imshow("Resize image", imgResize)
cv2.imshow("Cropped image", imgCropped)

cv2.waitKey(0)