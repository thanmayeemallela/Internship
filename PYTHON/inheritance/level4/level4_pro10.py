class Employee:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self):
        self.employees = [Employee("Rupa"), Employee("Sweety")]

print("Company HAS-A Employees")
for employee in Company().employees:
    print(employee.name)
