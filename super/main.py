# super adalah keyword yang digunakan untuk mengambil method dari class induk atau parent class
# kelebihan super adalah bisa mengambil method dari class induk atau parent class dan juga bisa meng-override methodnya
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def info(self):
        print("{} health {}".format(self.name, self.health))


class intelectHero(Hero):
    def __init__(self, name):
        # penggunaan super() untuk mengambil method dari class induk
        super().__init__(name, 100)
        super().info()
        # penggunaan cara method init dari class induk
        # Hero.__init__(self, name, 100)


class strengthHero(Hero):
    def __init__(self, name):
        Hero.__init__(self, name, 200)
        super().info()


free_fire = intelectHero("Free Fire")
pubg = strengthHero("PUBG")

# print(free_fire.name, " ", free_fire.health)
# print(pubg.name, " ", pubg.health)
