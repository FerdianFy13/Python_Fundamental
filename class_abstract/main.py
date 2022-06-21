# abstract class adalah class yang tidak dapat diinstansiasi
from abc import ABC, abstractmethod


class Button(ABC):
    # def click(self):
    #     print("Button clicked")
    @abstractmethod
    def click(self):
        pass


class PushButton(Button):
    # pass
    def click(self):
        print("Push button clicked")


class RadioButton(Button):
    # pass
    def click(self):
        print("Radio button clicked")


tombol = PushButton()
tombol2 = RadioButton()

tombol.click()
tombol2.click()
help(tombol)
