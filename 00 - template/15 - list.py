data = [1,4,9,16,25,36,49,64]

# mengakses List
subdata1 = data[3]
subdata2 = data[-3]

# memotong list
subdata3 = data[0:4] # 0 samapai sebelum 4
subdata4 = data[-2:] # mengambil semua yg Kekanan setelah [-2]
subdata4 = data[:4] # mengambil semua yg Kekiri setelah [4]

data2 = [100,200,300,400,500,600,700,800]

# menambah list
data3 = data + data2

print(data)
print("-----"*6)
'''
    BAHAYA !! data bisa berubah | mengCopy list ke variabel
'''

a = data # SALAH = "a" menjadi "data" & "data" menjadi a
a = data[:] # harus BEGINI = "a" menCOPY semua yg ada di "data" 
a[4] = 87 

print("before :")
print(data)
print("after  :")
print(a)
print("-----"*6)

# mengubah list dgn slicing
data[3:5] = [11,12] #[3:5] = 3 sampai 5
print(data)
print("-----"*6)

# list dalam list
x = [data,data2]
print(x)
print("-----"*6)

# akses list dalam multidimensional list
y = x[0][3] # [0] = kotak ke 1 dari "x" | [3] urutan ke 3 di kotak tsb
print(y)
print("-----"*6)

# methods untuk list
data.append(data2) # menambah member yg diinginkan "(data2)"
print(data)
print("-----"*6)

# function untuk list
panjang_list = len(data)
print(panjang_list)
print("-----"*6)