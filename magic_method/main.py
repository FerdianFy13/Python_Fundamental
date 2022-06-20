# # penggunaan reverse method
# list = [5, 10, 15, 25]
# print(list[::-2])

# magic method adalah method yang tidak didefinisikan secara eksplisit
class Mango:
    def __init__(self, name, total):
        self.name = name
        self.total = total

    # __repr__ adalah method yang akan dijalankan ketika mengambil nilai dari objek
    def __repr__(self):
        return "Debug Buah {} dengan total {}".format(self.name, self.total)

    # __str__ adalah sebuah method yang dijalankan ketika mengambil nilai dari objek ketika program diproduksi
    # perbedaan __str__ dan __repr__ adalah __str__ akan menampilkan nilai dari objek ketika program diproduksi sedangkan __repr__ akan menampilkan nilai dari objek ketika program dijalankan
    def __str__(self):
        return "Buah {} dengan total {}".format(self.name, self.total)

    # __add__ adalah method yang akan dijalankan ketika menjumlahkan objek
    def __add__(self, other):
        return self.total + other.total


fruit = Mango("Apple", 10)
melon = Mango("Melon", 20)
# print(fruit.__dict__)
# cara mengakses method __repr__
# print(repr(fruit))
# cara mengakses method __str__
print(melon)
print(fruit + melon)
