class Hero:
    jumlah = 0


    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        Hero.jumlah += 1

    # method = void
    def siapa(self):
        print("namaku adalah " + self.name)
    
    # method dengan argument
    def healthUp(self, up):
        self.health += up
    
    # method dengan return
    def getHealth(self):
        return self.health



hero1 = Hero("Sniper",100, 10, 5)
hero2 = Hero("Mario",90, 5, 10)

hero1.siapa()
hero1.healthUp(210)

print(hero1.getHealth())