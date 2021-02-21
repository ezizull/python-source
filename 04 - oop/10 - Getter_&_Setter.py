from typing import NoReturn


class Hero:

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.__info = "name {} : \n\t health: {}".format(self.name,self.__health)

    @property
    def info(self):
        return "name {} : \n\t health: {}".format(self.name,self.__health) # name dapat diupdate
        # return self.__info # tidak dapat update name

    @property
    def armor(self):
        pass
    
    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print("armor di delet")
        self.__armor = None


sniper = Hero('sniper',100,5)
print(sniper.info)

print("\nUbah nama:")
sniper.name = 'dadang'
print(sniper.info)

print("\ngetter untuk armor:")
print(sniper.armor)
print("setter untuk armor:")
sniper.armor = 30
print(sniper.armor)


del sniper.armor
print(sniper.__dict__)