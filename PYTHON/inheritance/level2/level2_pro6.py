class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self):
        self.employees = [Employee("Rupa"), Employee("Sweety")]

    def show_employees(self):
        for employee in self.employees:
            print(employee.name)

Department().show_employees()
