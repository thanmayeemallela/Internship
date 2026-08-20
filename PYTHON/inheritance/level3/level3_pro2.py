class PaymentService:
    def pay(self, amount):
        print("Payment done:", amount)

class BankAccount:
    def make_payment(self, service):
        service.pay(1000)

account = BankAccount()
account.make_payment(PaymentService())
