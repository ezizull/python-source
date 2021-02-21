import numpy as np

print()

a = np.arange(10)**2

print(a)
print()

#Index: 0 Dibaca [6 = 7]
print('elemen ke 1 dari a adalah', a[0])
print('elemen ke 7 dari a adalah', a[6])
print('elemen ke akhir dari a adalah', a[-1])
print()

#Slicing: 0 !!Dibaca [5 = 5]
print('elemen dari 1 - 6 adalah', a[0:6]) #(Start,End)
print('elemen dari 4 - akhir adalah', a[3:])
print('elemen dari awal - 5 adalah', a[:5])
print()

#Iterasi
for i in a:
    print('value =',i)

print()