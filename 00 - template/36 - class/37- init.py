class mahasiswa():

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim = input_nim

    def belajar(self,kondisi):
        print(self.nama,'sedang belajar', kondisi)

    def tidur(self):
        print(self.nama,'tidur dalam kelas')


otong = mahasiswa("otong surotong",123456789)

print(otong.nama)
print(otong.nim)

otong.belajar("dengan giat")

# ucup = mahasiswa()

# otong.nama = "otong surotong"
# ucup.nama = "maichel ucup"

# print(ucup.nama)

# ucup.tidur()