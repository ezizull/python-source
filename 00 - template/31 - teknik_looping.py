# teknik looping

nama_band = ['payung teduh',
             'fourtwnty',
             'dialog dini hari',
             'Mr. sonjaya',
             'parahyene',
             'syahrini']

# iterasi = 0;
# for band in nama_band:
#     print('no:',iterasi,'namaband',band)
#     iterasi+=1

kumpulan_lagu = ['akad',
        'zona nyaman',
        'rumahku',
        'sang filsuf',
        'sindoro',
        'jodohku']

# enumerate = otomatis me return

for index,band in enumerate(nama_band):
    print(index,':',band)


print('='*40)

# zip = menggambungkan list

for band,lagu in zip(nama_band,kumpulan_lagu):
    print(band,'menyayikan lagu yang berjudul:',lagu)

print('='*40)

# playlist

playlist = {'baby baby', 'ada apa dengan cinta', 'cenat cenut', 'jaran goyang','gorgom','kuda','kucing'}

for lagu in sorted(playlist):
    print(lagu)

print('='*40)

# dictionary

playlist2 = {'payung teduh':'akad',
             'fourtwnty':'zona nyaman',
             'dialog dini hari': 'rumahku',
             }

for i in playlist2.items():
    print(i)