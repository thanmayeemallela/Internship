class Student:
    college_name = "ABC College"

    def __init__(self, name: str):
        self.name = name


class Employee:
    company_name = "XYZ Corp"

    def __init__(self, name: str):
        self.name = name


class Car:
    number_of_wheels = 4

    def __init__(self, brand: str):
        self.brand = brand


class BankAccount:
    bank_name = "National Bank"

    def __init__(self, holder: str, acc_no: str):
        self.holder = holder
        self.acc_no = acc_no


class Product:
    category = "General"

    def __init__(self, name: str):
        self.name = name


if __name__ == "__main__":
    # College name
    s1 = Student('A')
    s2 = Student('B')
    s3 = Student('C')
    print('College:', Student.college_name)

    # Company name
    print('Company:', Employee.company_name)

    # Wheels
    print('Wheels:', Car.number_of_wheels)

    # Bank
    a1 = BankAccount('Alice', '0001')
    a2 = BankAccount('Bob', '0002')
    print('Bank name:', BankAccount.bank_name)

    # Product category
    print('Category:', Product.category)
