class Hero:
    __jumlah = 0

    def __init__(self, name, health, attackPower, armor):
        self.__name = name
        self.__healthStandart = health
        self.__attackPowerStandart = attackPower
        self.__armorStandart = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandart * self.__level
        self.__attackPowerMax = self.__attackPowerStandart * self.__level
        self.__armor = self.__armorStandart * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level {} : \n\thealth = {}/{}\n\tattack = {} \n\tarmor = {}".format(
            self.__name,
            self.__level,
            self.__health,
            self.__healthMax,
            self.__attackPowerMax,
            self.__armor,
        )

    @property
    def getExp(self):
        pass

    @getExp.setter
    def getExp(self, add):
        self.__exp += add
        if self.__exp >= 100:
            print(self.__name, "level up")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandart * self.__level
            self.__attackPowerMax = self.__attackPowerStandart * self.__level
            self.__armor = self.__armorStandart * self.__level

    def attack(self, musuh):
        self.getExp = 50


ferdian = Hero("Monkey D-Luffy", 100, 15, 10)
axe = Hero("Axe", 100, 15, 10)
print(ferdian.info)

ferdian.attack(axe)
ferdian.attack(axe)
ferdian.attack(axe)
print(ferdian.info)
