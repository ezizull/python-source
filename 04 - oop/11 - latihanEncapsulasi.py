class Hero:

    __jumlah = 0

    def __init__(self, name, health, attack, armor):
        self.__name = name
        self.__firsthealth = health
        self.__firstattack = attack
        self.__firstarmor = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__firsthealth * self.__level
        self.__attack = self.__firstattack * self.__level
        self.__armor = self.__firstarmor * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level {}  : \n\thealth = {}/{} \n\tarmor = {} \n\tatttack = {}".format(self.__name,self.__level,self.__health,self.__healthMax,self.__armor,self.__attack)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, plusExp):
        self.__exp += plusExp
        if (self.__exp >= 100):
            print()
            print(self.__name, 'level up')
            print()
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__firsthealth * self.__level
            self.__attack = self.__firstattack * self.__level
            self.__armor = self.__firstarmor * self.__level

    def menyerang(self, musuh):
        self.gainExp = 50



slardar = Hero('slardar', 100, 5, 10)
axe = Hero('axe', 100, 5, 10)
print(slardar.info) 

slardar.menyerang(axe)
slardar.menyerang(axe)
slardar.menyerang(axe)
print(slardar.info)