class Team:
    def setTeam(self, team):
        self.team = team

    def showTeam(self):
        print(self.team)


class Type:
    def setType(self, type):
        self.type = type

    def showType(self):
        print(self.type)


class Hero(Team, Type):
    def __init__(self, name, health):
        self.name = name
        self.health = health


mil = Hero("imil", 100)
mil.setTeam("mil mel mal")
mil.setType("human")
mil.showTeam()
mil.showType()
print(mil.name, mil.health)
