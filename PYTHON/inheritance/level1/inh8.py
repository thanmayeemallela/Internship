class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def study(self):
        print(self.name, "is a student")

class Teacher(Person):
    def teach(self):
        print(self.name, "is a teacher")

Student("Rupa", 17).study()
Teacher("Latha", 35).teach()
