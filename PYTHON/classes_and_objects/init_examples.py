class Student:
    def __init__(self, name: str, age: int, course: str, marks: float):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks


class Employee:
    def __init__(self, emp_id: int, name: str, department: str, salary: float):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary


class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price

    def display(self) -> str:
        return f"{self.title} by {self.author} - {self.price}" 


class Car:
    def __init__(self, brand: str, model: str, year: int, price: float):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def start(self) -> str:
        return "Started"

    def stop(self) -> str:
        return "Stopped"

    def display(self) -> str:
        return f"{self.brand} {self.model} ({self.year}) - {self.price}"


class BankAccount:
    def __init__(self, holder: str, acc_no: str, balance: float):
        self.holder = holder
        self.acc_no = acc_no
        self.balance = balance


if __name__ == "__main__":
    s = Student('A', 20, 'CS', 85.5)
    print(s.name, s.marks)
    e = Employee(1, 'B', 'IT', 40000)
    print(e.emp_id, e.name, e.salary)
    b = Book('Learn', 'C', 250)
    print(b.display())
    car = Car('Ford', 'Figo', 2016, 300000)
    print(car.start(), car.display(), car.stop())
    acc = BankAccount('D', '0001', 1000)
    print(acc.holder, acc.balance)
