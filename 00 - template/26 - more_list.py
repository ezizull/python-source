print("")

barang = ['ember','jaket','mobil']
print(barang,'\n---------------------------------------')


print("\n\tmethod menambah list :\n")

barang.append('sepeda')
print(barang)

barang.extend('dompet')
print(barang)

barang.insert(3,'sepeda')
print(barang,'\n---------------------------------------')

print("\n\tmethod menghitung list :\n")

jumlahsepeda = barang.count('sepeda')
print("jumlah sepeda adalah: ",jumlahsepeda,'\n---------------------------------------')

print("\n\tmethod meremove list :\n")

barang.remove('sepeda')
print(barang,'\n---------------------------------------')

print("\n\tmethod mereverse list :\n")

barang.reverse()
print(barang,'\n---------------------------------------')

print("\n\tmethod mengcopy list :\n")

stuff = barang.copy() # tanpa .copy barang ikut berubah jika stuff dirubah
stuff.append('gelas')
print(stuff)
print(barang)

print("")