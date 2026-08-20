class Teacher:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name):
        self.name = name

class School:
    def __init__(self):
        self.teacher = Teacher("Latha")
        self.student = Student("Rupa")

    def show(self):
        print("Teacher:", self.teacher.name)
        print("Student:", self.student.name)

School().show()
