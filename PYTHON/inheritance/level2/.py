class Student:
    def __init__(self, name):
        self.name = name

class College:
    def __init__(self):
        self.students = [Student("Rupa"), Student("Mahi"), Student("Sri")]

    def show_students(self):
        for student in self.students:
            print(student.name)

College().show_students()
