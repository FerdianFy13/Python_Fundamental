# diamond problem adalah kasus multiple inheritance yang memiliki turunan yang sama
# yang dapat diselesaikan dengan menggunakan keyword super()


class A:
    def show(self):
        print("this is a query A")


class B(A):
    def show(self):
        print("this is a query B")


class C(A):
    def show(self):
        print("this is a query C")


class D(B, C):
    pass
    # def show(self):
    #     print("this is a query D")


mal = D()
mal.show()
help(mal)
