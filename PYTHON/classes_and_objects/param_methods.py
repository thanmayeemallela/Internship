class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def sub(self, a: float, b: float) -> float:
        return a - b

    def mul(self, a: float, b: float) -> float:
        return a * b

    def div(self, a: float, b: float) -> float:
        return a / b if b != 0 else float('inf')


class Student:
    def grade(self, marks: float) -> str:
        if marks >= 90:
            return 'A'
        if marks >= 75:
            return 'B'
        if marks >= 60:
            return 'C'
        return 'F'


class Rectangle:
    def area(self, length: float, width: float) -> float:
        return length * width


class BankAccount:
    def __init__(self, holder: str, balance: float = 0.0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount: float) -> float:
        self.balance += amount
        return self.balance


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def total_price(self, quantity: int) -> float:
        return self.price * quantity


if __name__ == "__main__":
    calc = Calculator()
    print('Calc add:', calc.add(5, 3))
    st = Student()
    print('Grade:', st.grade(82))
    rect = Rectangle()
    print('Area:', rect.area(4, 5))
    acc = BankAccount('A')
    print('Deposit:', acc.deposit(500))
    prod = Product('Pen', 10)
    print('Total price:', prod.total_price(4))
