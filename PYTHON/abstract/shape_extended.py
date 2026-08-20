from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    r = Rectangle(4, 5)
    c = Circle(3)
    print(f"Rectangle area: {r.area()}, perimeter: {r.perimeter()}")
    print(f"Circle area: {c.area():.2f}, perimeter: {c.perimeter():.2f}")
