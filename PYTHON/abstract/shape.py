from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


if __name__ == "__main__":
    c = Circle(3)
    r = Rectangle(4, 5)
    print(f"Circle area: {c.area():.2f}")
    print(f"Rectangle area: {r.area():.2f}")
