class Person:
    def show_name(self):
        print("Name: Rupa")

class Student(Person):
    def study(self):
        print("Rupa is studying")

student = Student()
student.show_name()
student.study()
