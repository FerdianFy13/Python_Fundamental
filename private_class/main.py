class Hero:
    def __init__(self, name, level, attack):
        # penggunan public variable
        self.name = name
        self.__level = level

        #  cara membuat privatet variable dalam python dengan menggunakan tanda underscore dua kali didepan variabel
        self.__attack = attack

        # cara membuat protected variable dalam python dengan menggunda tanda underscore satu kali didepan variabel
        self._enemy = "enemy"

    # encapsulation adalah cara untuk menghindari akses ke private variable dalam class
    # getter untuk mengambil nilai dari private variable
    # setter untuk mengubah nilai dari private variable
    def getAttack(self):
        return self.__attack

    def getLevel(self):
        return self.__level

    def setAttack(self, power):
        self.__level -= power


ferdi = Hero("Ferdian", 100, 25)
print(ferdi.__dict__)
print(ferdi.name)
print(ferdi.getAttack())
ferdi.setAttack(60)
print(ferdi.getLevel())


# perbedaan antara private dan protected
# private: hanya bisa diakses di dalam class
# protected: hanya bisa diakses di dalam class dan kelas turunan
