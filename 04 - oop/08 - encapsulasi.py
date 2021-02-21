class Hero:

    def __init__(self, name, health, attack):
        self.__name = name
        self.__health  = health
        self.__attack = attack

    # getter
    def getname(self):
        return self.__name

    def gethealth(self):
        return self.__health
    
    def getattack(self):
        return self.__attack

    # setter
    def diserang(self,terserang):
        self.__health -= terserang

    def plusAttack(self, tambahan):
        self.__attack += tambahan



shaker = Hero("Shaker", 50, 5)

print(shaker.__dict__)

# game berjalan

print()

print()
print(shaker.getname())
print(shaker.gethealth())
print()
shaker.diserang(7)
print(shaker.gethealth())
print()
shaker.plusAttack(10)
print(shaker.getattack())

print()