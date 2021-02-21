import cv2
import numpy as np

img = np.zeros((400,600,3),np.uint8)
# print(img)
# img[:]= 255,0,0

# line & shape
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(200,225,25),5)
cv2.rectangle(img,(50,350),(200,200),(10,80,225),50)
cv2.circle(img,(470,130),100,(225,100,10),25)

# text
cv2.putText(img," Opencv",(150,70),cv2.FONT_HERSHEY_COMPLEX,1.5,(30,30,200),5)

cv2.imshow("image",img)

cv2.waitKey(0)