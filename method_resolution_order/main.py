# method resolution order adalah urutan method yang akan dijalankan ketika menggunakan keyword super() dalam penggunaan multiple inheritance
class A:
    def show(self):
        print("laravel")


class B:
    def show(self):
        print("codeigniter")


class C(A, B):
    def show(self):
        print("flutter")


mil = C()
mil.show()
help(mil)
