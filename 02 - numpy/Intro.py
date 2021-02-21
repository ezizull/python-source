import numpy as np

print()

#Membuat Vector
a = np.array([1, 2, 3, 4, 5])
b = np.array([1.5, 2.5, 5, 6, 7])

#Membuat Vector dengan Range
c = np.arange(1, 10, 2)

#Membuat Linspace
d = np.linspace(1, 10, 4)

#Array Multidimensi / Matrix
e = np.array( [(1,2,3) , (4,5,6)] )

#Matrix dengan Nilai 0
f = np.zeros((3,5))

#Matrix dengan Nilai 1
g = np.ones(5)

#Matrix Identitas
h1 = np.identity(5)
h2 = np.eye(5)

#Display
print(h2)

print()