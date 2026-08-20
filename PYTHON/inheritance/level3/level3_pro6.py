class EmailService:
    def send(self, message):
        print("Email:", message)

class Order:
    def confirm(self, email):
        email.send("Your order is confirmed")

Order().confirm(EmailService())
