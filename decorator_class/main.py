# decorator adalah sebuah function yang dapat menambahkan function lain sebagai parameter
from abc import ABC, abstractmethod


class Button(ABC):
    def __init__(self, set_link):
        self.link = set_link

    @abstractmethod
    def click(self):
        pass

    @property
    @abstractmethod
    def link(self):
        pass


class PushButton(Button):
    # pass
    def click(self):
        print("Go To: {}".format(self.link))

    @Button.link.setter
    def link(self, value):
        self.__link = value

    @link.getter
    def link(self):
        return self.__link


tombol = PushButton("www.imil13.com")
tombol.click()
