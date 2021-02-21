class Hero:
    # class variable
    jumlah = 0


    def __init__(self, name, health, power, armor):
        # instance variable
        self.name = name # = hero.name = "sniper"
        self.health = health # = hero.health = "sniper"
        self.power = power # = hero.power = 100
        self.armor = armor # = hero.armor = 100
        Hero.jumlah += 1
        print("membuat hero bernama " + name)



hero1 = Hero("sniper",100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("mirana",100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("ucup",1000, 100, 0)
print(Hero.jumlah)


'''

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
print("\n",Hero.__dict__)

'''