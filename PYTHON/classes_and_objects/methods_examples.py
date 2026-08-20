import math


class Student:
    def __init__(self, name: str, age: int, course: str):
        self.name = name
        self.age = age
        self.course = course

    def display(self) -> str:
        return f"Student: {self.name}, {self.age}, {self.course}"


class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def display_salary(self) -> str:
        return f"{self.name} salary: {self.salary:.2f}"


class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b if b != 0 else float('inf')


class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def circumference(self) -> float:
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    st = Student('A', 20, 'CS')
    print(st.display())
    emp = Employee('B', 5000)
    print(emp.display_salary())
    calc = Calculator()
    print('Add:', calc.add(2, 3))
    rect = Rectangle(4, 5)
    print('Rect area/perim:', rect.area(), rect.perimeter())
    cir = Circle(3)
    print('Circle area/circumf:', round(cir.area(), 2), round(cir.circumference(), 2))
