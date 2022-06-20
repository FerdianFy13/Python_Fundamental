# multiple inheritance adalah inheritance yang lebih dari satu turunan dengan menggunakan keyword super()


class A:
    def queryA(self):
        print("query A")


class B:
    def queryB(self):
        print("query B")


# penggunaan multiple inheritance dengan menggunakan keyword super()
class C(A, B):
    def queryC(self):
        print("query C")


example = C()
example.queryA()
example.queryB()
example.queryC()
