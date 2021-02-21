'''
# mendefinisikan fungsi

def fungsi():
    print('ini adalah fungsi ')

# memanggil fungsi
fungsi()
fungsi()
'''

# membuat fungsi sederhana

print("")

def suaraayam():
    print('kukuruyuk!!!')

def hargaayam():
    suaraayam()
    print('harga ayam per 1 kg adalah Rp. 20.000')

# membuat fungsi dengan input argumen
def hargatotalayam(kg):
    suaraayam()
    harga = 20000
    hargaTotal = kg*harga
    print('harga ',kg,'kg ayam adalah',hargaTotal)

hargaayam()
hargatotalayam(int(input('pesan brp kg : ')))

print("")