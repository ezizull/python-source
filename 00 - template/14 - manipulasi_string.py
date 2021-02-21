# operasi & manipulasi string

'''
    1. menyambung STRING (concatenate)
'''
nama_pertama = 'Saya'
nama_tengah = "D"
nama_akhir = "Man"

nama_lengkap = nama_pertama +" "+ nama_tengah +"."+ nama_akhir
print(nama_lengkap)

'''
    2. menghitung panjang STRING
'''
panjang = len(nama_lengkap)
print("panjang dari " +"'"+ nama_lengkap +"'"+ " = " + str(panjang))


'''
    3. operator untuk STRING
'''
d = "d"
status = d in nama_lengkap
print("Apakah " + d + " ada di " +"'"+ nama_lengkap +"'"+ " = " + str(status))

d = "D"
status = d in nama_lengkap
print("Apakah " + d + " ada di " +"'"+ nama_lengkap +"'"+ " = " + str(status))

d = "d"
status = d not in nama_lengkap
print("Apakah " + d + " Tidak ada di " +"'"+ nama_lengkap +"'"+ " = " + str(status))

'''
    4. mengulang STRING
'''
print("ha"*5) # hahahahaha
print(5*"ha") # hahahahaha

'''
    5. Indexing
'''
print("index ke 0 = " + nama_lengkap[0])
print("index ke 6 = " + nama_lengkap[6])
print("index ke -1 = " + nama_lengkap[-1])
print("index ke -2 = " + nama_lengkap[-2])
print("index ke -2 = " + nama_lengkap[-2])
print("index ke 0 : 3 = " + nama_lengkap[0:3]) # = 0 sampai SEBELUM 3
print("index ke 3 : 8 = " + nama_lengkap[3:8]) # = 3 sampai SEBELUM 8
print("index ke 0,2,4,6,8,10 = " + nama_lengkap[0:10:2]) # = 0 - 10 LONCAT 2

'''
    6. item paling KECIL & BESAR
'''
# semua ditentukan Besar - Kecilnya ASCII code
print("paling kecil : " + min(nama_lengkap))
print("paling besar : " + max(nama_lengkap)) 
ascii_code = ord(" ")
print("ASCII code untuk 'spasi' = " + str(ascii_code))
data = 117
print("ASCII code untuk '117' = " + chr(data))

'''
    7. operator METHOD
'''
data = "uvu veve osas"
jumlah = data.count("v")
print("jumlah v pada " +"'"+ data +"'"+ " = " + str(jumlah))