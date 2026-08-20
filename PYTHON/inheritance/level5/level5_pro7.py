class Department:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, name):
        self.name = name

class PayrollService:
    def pay(self):
        print("Salary processed")

class Company:
    def __init__(self):
        self.departments = [Department("IT")]
        self.employees = [Employee("Rupa"), Employee("Sweety")]

    def process_salary(self, payroll):
        payroll.pay()

company = Company()
print("Company HAS-A Departments and Employees")
print("Company USES-A PayrollService")
company.process_salary(PayrollService())
