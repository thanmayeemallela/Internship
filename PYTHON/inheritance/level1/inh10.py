class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def code(self):
        print("Rupa is writing code")

class Tester(Employee):
    def test(self):
        print("Sweety is testing the program")

class Manager(Employee):
    def manage(self):
        print("Latha is managing the team")

Developer().code()
Tester().test()
Manager().manage()
