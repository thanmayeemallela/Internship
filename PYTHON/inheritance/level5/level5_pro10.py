class EducationalInstitution:
    def show(self):
        print("Educational institution")

class Department:
    def __init__(self, name):
        self.name = name

class ExaminationService:
    def conduct(self):
        print("Exam conducted")

class University(EducationalInstitution):
    def __init__(self):
        self.departments = [Department("CSE"), Department("ECE")]

    def conduct_exam(self, exam):
        exam.conduct()

university = University()
print("University IS-A EducationalInstitution")
print("University HAS-A Departments")
print("University USES-A ExaminationService")
university.show()
university.conduct_exam(ExaminationService())
