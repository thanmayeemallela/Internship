from abc import ABC , abstractmethod
class animal(ABC):
    def sound(self):
        pass;
class dog (animal):
    def sound(self):
        print("dog barks")
class cat (animal):
    def sound(self):
        print("cat meows")
d=dog()
c=cat()
d.sound()
c.sound()