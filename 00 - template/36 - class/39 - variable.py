class mahasiswa():

    jumlah_mahasiswa = 0

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim = input_nim
        
        mahasiswa.jumlah_mahasiswa += 1
            
# main program

otong = mahasiswa("otong surotong", 123456789)
ucup = mahasiswa("michael surotong", 987654321)
cassandra = mahasiswa("cassandra", 1029384756)

print(mahasiswa.jumlah_mahasiswa)

# otong.kegemaran = "menari"
# mahasiswa.jurusan = "ekonomi"
otong.jurusan = "ekonomi mikro"

# print(mahasiswa.jurusan)
print(otong.nama,otong.jurusan)
# print(otong.kegemaran)
# print(ucup.jurusan)

# print(mahasiswa.__dict__)
# print(otong.__dict__)