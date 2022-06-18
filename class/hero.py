class Hero:
    # penggunaan init merupakan sebuah contructor yang akan dipanggil saat object dibuat
    def __init__(self, name, level):
        self.name = name
        self.level = level

    # method adalah sebuah function yang berada di dalam class dan dapat diakses oleh object
    # penggunaan void method atau sebuah method tanpa adanya sebuah return
    def show_hero(self):
        print("Nama Hero: ", self.name)

    # penggunaan method dengan menggunakan sebuah argument didalamnya
    def show_level(self, level):
        print("Level Hero ", level)

    # penggunaan method dengan menggunakan sebuah return
    def show_level_return(self):
        return self.level  # return value dari method


hero1 = Hero("Monkey D. Luffy", 1)
print(hero1.name)
hero1.show_hero()
hero1.show_level(1)
print(hero1.show_level_return())
