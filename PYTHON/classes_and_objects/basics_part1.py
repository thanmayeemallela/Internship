class Student:
    def __init__(self, name: str = "Alice"):
        self.name = name

class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year


class Employee:
    def __init__(self, name: str, emp_id: int, dept: str):
        self.name = name
        self.emp_id = emp_id
        self.dept = dept


class Mobile:
    def __init__(self, brand: str, model: str, price: float):
        self.brand = brand
        self.model = model
        self.price = price


class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price


if __name__ == "__main__":
    # 1. Student and one object
    s = Student('Rahul')
    print('Student:', s.name)

    # 2. Car - three objects
    c1 = Car('Toyota', 'Corolla', 2018)
    c2 = Car('Honda', 'Civic', 2020)
    c3 = Car('Ford', 'Focus', 2017)
    for i, c in enumerate((c1, c2, c3), 1):
        print(f'Car{i}:', c.brand, c.model, c.year)

    # 3. Employee object
    e = Employee('Kavya', 101, 'HR')
    print('Employee:', e.name, e.emp_id, e.dept)

    # 4. Mobile
    m = Mobile('Samsung', 'A12', 10999.0)
    print('Mobile:', m.brand, m.model, m.price)

    # 5. Books - two objects
    b1 = Book('Python 101', 'John Doe', 299.0)
    b2 = Book('Data Science', 'Jane Roe', 399.0)
    for b in (b1, b2):
        print('Book:', b.title, b.author, b.price)
