class Course:
    def __init__(self, name):
        self.name = name

class Person:
    def show(self):
        print("Person")

class Student(Person):
    def __init__(self):
        self.course = Course("Python")

student = Student()
print("Student IS-A Person")
print("Student HAS-A Course")
student.show()
print("Course:", student.course.name)
