class Hero:
    def __init__(self, name, health, armor):
        self.__name = name
        self.__health = health
        self.__armor = armor

    # penggunaan property
    # property ini akan menjalankan method getter dan setter1
    @property
    def information(self):
        return "name: {}, health: {}".format(self.__name, self.__health)

    @property
    def armor(self):
        return self.__armor

    # getter digunakan untuk mengambil nilai dari property
    @armor.getter
    def armor(self):
        return self.__armor

    # setter digunakan untuk mengubah nilai property
    @armor.setter
    def armor(self, input):
        self.__armor = input

    # deleter digunakan untuk menghapus property
    @armor.deleter
    def armor(self):
        print("armor has been deleted")
        self.__armor = None


aka47 = Hero("AK-47", 100, 20)
print(aka47.information)
print(aka47.armor)
print(aka47.__dict__)
aka47.armor = 30
print(aka47.armor)
print(aka47.__dict__)
del aka47.armor
print(aka47.__dict__)
