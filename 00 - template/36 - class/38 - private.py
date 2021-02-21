class mahasiswa():

    jurusan = "teknik tata boga"
    __nilai = 0 # private

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama  # public
        self.nim = input_nim    # public

    def uts(self,input_nilai):
        self.__nilai += input_nilai

    def uas(self,input_nilai):
        self.__nilai += input_nilai

    def status(self):
        if self.__nilai <= 50:
            print(self.nama,'tidak lulus')
        else:
            print(self.nama,'lulus')

otong   = mahasiswa("otong surotong",123456789)
ucup    = mahasiswa("michael ucup",123456789)

otong.uts(10)
otong.uas(50)
otong.status()

ucup.uts(90)
ucup.uas(40)
ucup.status()

# print(otong.__nilai)
