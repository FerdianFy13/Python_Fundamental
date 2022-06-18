class Hero:
    __value = 0

    def __init__(self, name):
        self.__name = name
        Hero.__value += 1

    # method ini akan dijalankan ketika object dibuat (static method)
    def getValue(self):
        return Hero.__value

    def getName(self):
        return self.__name

    # method decorator (static method) untuk mengubah method yang ada di dalam class dan dijalankan ketika object dibuat
    @staticmethod
    def getStaticValue():
        return Hero.__value

    # perbedaan static method dan class method
    # static method: method yang tidak berkaitan dengan object dan tidak berkaitan dengan class
    # class method: method yang berkaitan dengan class dan tidak berkaitan dengan object
    @classmethod
    def getClassValue(cls):
        return cls.__value


sniper = Hero("sniper")
print(Hero.getStaticValue())
aka47 = Hero("AK-47")
print(sniper.getClassValue())
# print(sniper.getName())
