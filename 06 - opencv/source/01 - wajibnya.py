import cv2
print("Package Imported")

'''
# photo
img = cv2.imread("bahan/julia.jpg")

cv2.imshow("output",img)
cv2.waitKey(0)
'''

# video
cap = cv2.VideoCapture(0) # webcam
cap.set(10,60)

def ubah_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

while True:
    success, img = cap.read()
    frame75 = ubah_frame(img, percent=75)
    cv2.imshow("video", frame75)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
