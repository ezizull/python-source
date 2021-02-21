# scope variable : local
print('\nscope : local\n')
namaKucing = 'casandra'

def rubahNamaKucing(namaBaru):
    namaKucing = namaBaru
    print('nama kucing saya',namaKucing)

rubahNamaKucing('ketie')
print('saya rubah namanya menjadi',namaKucing)
print('--------------------\n')

# scope variable : global
print('\nscope : global\n')
namaKucing = 'casandra'
makananKucing = 'wiskas'

def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru
    print('nama kucing saya',namaKucing,'makanannya',makananKucing,'.\n')
    

def kasihMakanKucing(makanan,nama):
    global namaKucing,makananKucing
    namaKucing = nama
    makananKucing = makanan

rubahNamaKucing('maoo')
kasihMakanKucing('teri kring','jhon')
print('saya rubah namanya menjadi',namaKucing,'makanannya diganti',makananKucing)
print('--------------------\n')

