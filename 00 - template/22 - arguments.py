
# fungsi dgn menggunakan argumen sederhana

def siswa(nama):
    print('\nsiswa ini bernama: ',nama)

siswa('mario\n')

# fungsi dengan menggunakan keywords arguments

def guru(nama,pelajaran):
    print('\nguru ini bernama: ',nama)
    print('mengajar pelajaran: ',pelajaran,'\n')

guru(nama='popong',pelajaran='seni rupa')
guru(pelajaran='olah raga',nama='endang',)
guru('olahraga','raihan') # ini contoh yang salah


# fungsi dengan menggunakan default arguments

def penjagaSekolah(nama,shift='siang',galak='tidak'):
    print('\npenjaga sekolah ini bernama: ', nama)
    print('shiftnya: ', shift)
    print('galak?: ', galak,'\n')

penjagaSekolah('entis')
penjagaSekolah('maman',shift='malam')
penjagaSekolah('asep',galak='sangat')



