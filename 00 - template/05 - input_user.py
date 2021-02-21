# input user

# data pasti STRING
data = input("masukan data: ")
print("data = ",data,",type = ",type(data))

# mengubah ke INTEGER
angka = float(input("masukan angka berkoma: "))
print("data = ",angka,",type = ",type(angka))
angka = int(input("masukan angka tanpa koma: "))
print("data = ",angka,",type = ",type(angka))

# kalo BOOLEAN
biner = bool(str(input("ketikkan / kosongkan: ")))
print("data = ",biner,",type = ",type(biner))