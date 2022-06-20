# override method adalah method yang meng-override method dari class induk atau parent class
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def info(self):
        print("Information pada superclass")
        print("{} health {}".format(self.name, self.health))


class intelectHero(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
        super().info()

    # override method
    # override dilakukan ketika memiliki argument yang sama dengan method yang lain
    def info(self):
        print("\nInformation pada subclass")
        print("{} \n\tTipe: intellegent \n\thealth {}".format(self.name, self.health))


class strengthHero(Hero):
    def __init__(self, name):
        super().__init__(name, 200)
        super().info()


free_fire = intelectHero("Free Fire")
pubg = strengthHero("PUBG")

free_fire.info()
