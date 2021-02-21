class Hero:
    
    def __init__(self, name, health, power, armor):
        self.name = name # = hero.name = "sniper"
        self.health = health # = hero.health = "sniper"
        self.power = power # = hero.power = 100
        self.armor = armor # = hero.armor = 100



hero1 = Hero("sniper",100, 10, 4)
hero2 = Hero("mirana",100, 15, 1)
hero3 = Hero("ucup",1000, 100, 0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)