class mahasiswa():
    # nama = 'nama'

    def __init__(self, input_name, input_nim):
        self.nama = input_name
        self.nim = input_nim

    def belajar(self, kondisi):
        print(self.nama,'sedang belajar', kondisi)

    def tidur(self):
        print(self.nama,'tidur dalam kelas')

otong = mahasiswa("otong surotong", 123456789)
ucup = mahasiswa("maichel ucup", 1029384756)

# otong.nama = "otong surotong"
# ucup.nama = "maichel ucup"


print(otong.nama)
print(ucup.nama)

otong.belajar("dengan giat")
ucup.tidur()