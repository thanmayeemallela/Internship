from abc import ABC , abstractmethod
class vehical(ABC):
    def start(self):
        pass;
class bike (vehical):
    def start(self):
        print("bike starts")
class car (vehical):
    def start(self):
        print("car starts")
b=bike()
c=car()
b.start()
c.start()