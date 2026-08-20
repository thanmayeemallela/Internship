class Laptop:
    def show(self):
        print("Laptop is ready")

class Employee:
    def work(self):
        print("Employee works")

class Developer(Employee):
    def __init__(self):
        self.laptop = Laptop()

developer = Developer()
print("Developer IS-A Employee")
print("Developer HAS-A Laptop")
developer.work()
developer.laptop.show()
