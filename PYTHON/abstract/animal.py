from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self) -> str:
        pass


class Dog(Animal):
    def sound(self) -> str:
        return "Woof"


class Cat(Animal):
    def sound(self) -> str:
        return "Meow"


if __name__ == "__main__":
    for a in (Dog(), Cat()):
        print(f"{a.__class__.__name__} -> {a.sound()}")
