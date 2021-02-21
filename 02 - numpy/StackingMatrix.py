import numpy as np
print()

a = np.array([1,2,3])
b = np.array([4,5,6])

aMat = np.zeros((2,3))
bMat = np.ones((2,3))

#Stacking Matrix: Menyatukan 2 Array/List

c = np.hstack((a,b))
d = np.vstack((a,b))

cMat = np.hstack((aMat,bMat)) #jumlah Baris Harus Sama
dMat = np.vstack((aMat,bMat)) #jumlah Kolom Harus Sama

print(dMat)

print()