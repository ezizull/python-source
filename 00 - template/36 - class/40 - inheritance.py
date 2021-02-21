class Ojek():
    
    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def cek_id_ojek(self):
        print('nama:',self.nama,'\nmotor:',self.transmisi,'\ndaerah:',self.daerah)

class Nojek(Ojek): # inheritance menggunakan semua dari "(Ojek)"
    pass
    def cek_id_ojek(self):
        print('nama:',self.nama,'\nmotor:',self.transmisi,'\ncek aplikasi Nojek!')

ojek1 = Ojek('mario','manual','pantai barat')
ojek2 = Nojek('omjack','metic','orang gunung')

print("")

# ojek1.cek_id_ojek()
ojek2.cek_id_ojek()

print("")