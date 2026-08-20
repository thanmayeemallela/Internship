from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def prepare(self) -> str:
        pass


class Pizza(Food):
    def prepare(self) -> str:
        return "Preparing pizza with cheese and toppings"


class Burger(Food):
    def prepare(self) -> str:
        return "Preparing burger with patty and lettuce"


if __name__ == "__main__":
    print(Pizza().prepare())
    print(Burger().prepare())
