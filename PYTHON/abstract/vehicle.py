from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self) -> str:
        pass


class Car(Vehicle):
    def start(self) -> str:
        return "Car engine started"


class Bike(Vehicle):
    def start(self) -> str:
        return "Bike engine started"


if __name__ == "__main__":
    print(Car().start())
    print(Bike().start())
