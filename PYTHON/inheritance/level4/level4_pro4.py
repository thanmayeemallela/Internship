class Employee:
    def work(self):
        print("Employee works")

class Manager(Employee):
    pass

print("Manager IS-A Employee")
Manager().work()
