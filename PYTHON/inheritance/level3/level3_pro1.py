class Printer:
    def print_data(self, data):
        print(data)

class Student:
    def __init__(self, name):
        self.name = name

    def print_details(self, printer):
        printer.print_data("Student: " + self.name)

student = Student("Rupa")
printer = Printer()
student.print_details(printer)
