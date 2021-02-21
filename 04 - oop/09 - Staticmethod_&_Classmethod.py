class Hero:

    __jumlah = 0;

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # method untuk object
    def getObject(self):
        return Hero.__jumlah

    # method untuk class
    def getClass():
        return Hero.__jumlah

    # method untul all
    @staticmethod
    def getAll():
        return Hero.__jumlah

    @classmethod
    def getObject(cls):
        return cls.__jumlah


sniper = Hero('sniper')
rikimaru = Hero('rikimaru')
print(Hero.getAll())
print(rikimaru.getObject())
ranger = Hero('ranger')
print(ranger.getAll())
print(Hero.getObject())