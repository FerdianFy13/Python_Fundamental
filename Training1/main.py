class Hero:
    def __init__(self, name, level, attaackPower, armorNumber):
        self.name = name
        self.level = level
        self.attaackPower = attaackPower
        self.armorNumber = armorNumber

    # self adalah sebuah variabel yang akan dibutuhkan untuk mengakses property dari object dan merepresentasikan object yang sedang diakses

    def attack(self, enemy):
        print(self.name + " menyerang " + enemy.name)
        enemy.defence(self, self.attaackPower)

    def defence(self, enemy, power):
        print(self.name + " diserang " + enemy.name)
        powers = power / self.armorNumber
        print("enemy power: " + str(powers))
        self.level -= powers
        print("remainder health: " + str(self.level))


sniper = Hero("Sniper", 1, 10, 5)
aka47 = Hero("AK-47", 2, 20, 10)
ferdi = Hero("Ferdi", 3, 30, 15)

sniper.attack(ferdi)
print("\n")
ferdi.attack(sniper)
