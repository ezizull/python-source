import numpy as np

print()

a = [1,2,3,4,5]
b = [6,7,8,9,10]

anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

#hasil_python = a + b

#print("hasil python:")
#print(hasil_python)

''' 
    ElementWise operation
'''
#Penjumlahan
hasil_numpy = anp + bnp

#Pengurangan
hasil_numpy = anp - bnp

#Pembagian
hasil_numpy = anp / bnp

#Perkalian
hasil_numpy = anp * bnp

#Perpangkatan
hasil_numpy = anp ** bnp

#Multidimensi Array Numpy
c = np.array(([1,2,3],[4,5,6]))
d = np.array(([7,8,9],[-1,-2,-3]))

hasil = c - d

print("hasil:")
print(hasil)

print()