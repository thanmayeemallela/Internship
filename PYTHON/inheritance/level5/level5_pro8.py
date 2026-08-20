class Teacher:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name):
        self.name = name

class NotificationService:
    def send(self):
        print("Notification sent")

class School:
    def __init__(self):
        self.teachers = [Teacher("Latha")]
        self.students = [Student("Rupa"), Student("Mahi")]

    def notify(self, service):
        service.send()

school = School()
print("School HAS-A Teachers and Students")
print("School USES-A NotificationService")
school.notify(NotificationService())
