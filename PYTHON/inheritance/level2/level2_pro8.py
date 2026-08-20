class Department:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self):
        self.departments = [
            Department("IT"),
            Department("HR"),
            Department("Sales")
        ]

    def show_departments(self):
        for department in self.departments:
            print(department.name)

Company().show_departments()
