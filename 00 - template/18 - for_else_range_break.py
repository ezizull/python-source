# for i in range (10,40,5): # 10 sampai 40 klipatan 5
#     print(i)

# for i in range (0,40): # 0 sampai 40
#     print(i)

# print(range(10,40,5)) # bukan range 
'''
    menemukan angka
'''

number = 5;

for i in range (0,10):
    print(i)
    if i == number:
         print('angka ditemukan',i)

print('--------------------')

for i in range (0,10):
    print(i)
    if i == number:
        print('angka ditemukan',i)
        break # keluar dari proses looping

print('--------------------')

'''
    else kurang tepat
'''
for i in range (0,10):
    print(i)
    if i == number:
        print('angka ditemukan',i)
        break # keluar dari proses looping
    else:
        print('angka tidak ditemukan')

print('--------------------')

'''
    else yang tepat
'''
for i in range (0,10):
    print(i)
    if i == number:
        print('angka ditemukan',i)
        break # keluar dari proses looping
else:
    print('angka tidak ditemukan')

print('--------------------')
    
for i in range (0,1):
    print(i)
else:
    print('hallo')

print("space diluar")

print('--------------------')

'''
    break mumutus/meniadakan operasi
'''
for i in range (0,10):
    print(i)
    break
    if i == number:
        print('angka ditemukan',i)
        break # keluar dari proses looping
else:
    print('angka tidak ditemukan')
