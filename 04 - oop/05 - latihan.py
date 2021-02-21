class Hero:

    def __init__(self, nama, darah, attack, armor):
        self.nama = nama
        self.darah  = darah
        self.attack = attack
        self.armor = armor

    def serang(self, lawan):
        print(self.nama + " menyerang " + lawan.nama)
        lawan.diserang(self, self.attack)
    
    def diserang(self, lawan, attack_lawan):
        print(self.nama + " diserang " + lawan.nama)
        attack_terasa = attack_lawan / self.armor
        print('attack terasa : ' + str(attack_terasa))
        self.darah -= attack_terasa
        print('darah ' + self.nama + ' tersisa ' + str(self.darah))


sniper = Hero('sniper',100,10,5)
rikimaru = Hero('rikimaru',100,20,10)

print()
sniper.serang(rikimaru)
print()
rikimaru.serang(sniper)
print()