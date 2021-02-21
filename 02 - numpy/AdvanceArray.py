import numpy as np
print()

#Matrix dengan Berbagai Tipe
print('Matrix dengan Berbagai Tipe:')
a = np.array(([1,2,3],[3,4,5]), dtype = float)

#Array dengan Menggunaka Function: 0 Dibaca
def kuadrat(baris,kolom):
    return kolom **2

def jumlah(baris,kolom):
    return (kolom + baris)

b= np.fromfunction(kuadrat, (1,10), dtype = int) #(fungsi, ukuran matrix, tipe)
c= np.fromfunction(jumlah, (4,4), dtype = float) #(fungsi, ukuran matrix, tipe)
print(b)
print("-----"*5)
print(c)
print()

#Array dgn Itereable
print('Matrix/Array dgn Itereable:')
iterable = (x*2 for x in range(5))

d = np.fromiter(iterable, dtype = int)
print(d)
print("-----"*5)
print()

#Multitype Array
dtipe = [('nama','S255'),('Tinggi', int)]

data = [('ucup',150),
        ('otong', 160),
        ('mario', 180)
        ]

e = np.array(data, dtype = dtipe)

print(e[0])

print()