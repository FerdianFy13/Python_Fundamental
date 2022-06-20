class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health


# cara melakukan inheritance dari class Hero
class intelectHero(Hero):
    pass


class strengthHero(Hero):
    pass


free_fire = Hero("Free Fire", 100)
pubg = intelectHero("PUBG", 200)
fifa = strengthHero("FIFA", 300)
print(free_fire.name)
print(pubg.__dict__)
print(fifa.__dict__)
print(help(intelectHero))
print(help(strengthHero))
