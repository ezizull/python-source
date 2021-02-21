class Hero:

    jumlah = 0
    __jumlah = 0

    def __init__(self, nama, darah):
        self.nama =  nama
        self.darah = darah

        # variable Private
        self.__private = "private"
        # variable Protected
        self._protected = "protected"


lina = Hero("Lina",100)

print()
print(lina.__dict__)
print()
print(Hero.__dict__)
print(Hero.__jumlah)
print()