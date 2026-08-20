from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self) -> str:
        pass

    @abstractmethod
    def stop(self) -> str:
        pass


class Car(Vehicle):
    def start(self) -> str:
        return "Car started"

    def stop(self) -> str:
        return "Car stopped"


class Bike(Vehicle):
    def start(self) -> str:
        return "Bike started"

    def stop(self) -> str:
        return "Bike stopped"


if __name__ == "__main__":
    print(Car().start())
    print(Car().stop())
    print(Bike().start())
    print(Bike().stop())
