class NotificationService:
    def send(self, name):
        print("Notification sent to", name)

class Student:
    def notify(self, service):
        service.send("Rupa")

Student().notify(NotificationService())
