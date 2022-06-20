# method resolution order adalah urutan method yang akan dijalankan ketika menggunakan keyword super() dalam penggunaan multiple inheritance
class A:
    def show(self):
        print("A")


class B:
    def show(self):
        print("B")


class C(A, B):
    def show(self):
        print("C")


mil = C()
mil.show()
help(mil)
