class Student:
    def __init__(self, name: str, age: int, course: str):
        self.name = name
        self.age = age
        self.course = course


class Employee:
    def __init__(self, name: str, department: str, salary: float):
        self.name = name
        self.department = department
        self.salary = salary


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self) -> float:
        return self.price * self.quantity


class Car:
    def __init__(self, brand: str, model: str, year: int, price: float):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price


class Person:
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city


if __name__ == "__main__":
    # Students
    s1 = Student('A', 20, 'Math')
    s2 = Student('B', 21, 'CS')
    s3 = Student('C', 19, 'Physics')
    for s in (s1, s2, s3):
        print('Student:', s.name, s.age, s.course)

    # Employees (5)
    emps = [
        Employee(f'Emp{i}', 'Dept', 3000 + i * 100) for i in range(1, 6)
    ]
    for emp in emps:
        print('Employee:', emp.name, emp.department, emp.salary)

    # Products
    p = Product('Pen', 10.0, 5)
    print('Product total:', p.total_price())

    # Cars
    cars = [
        Car('Toyota', 'Y', 2015, 500000),
        Car('Hyundai', 'Z', 2019, 600000),
        Car('Kia', 'S', 2021, 700000),
    ]
    for car in cars:
        print('Car:', car.brand, car.model, car.year, car.price)

    # Persons
    p1 = Person('X', 30, 'Delhi')
    p2 = Person('Y', 25, 'Mumbai')
    print('Person1:', p1.name, p1.age, p1.city)
    print('Person2:', p2.name, p2.age, p2.city)
