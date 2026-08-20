class PaymentService:
    def pay(self):
        print("Payment completed")

class Order:
    def place_order(self, service):
        service.pay()

print("Order USES-A PaymentService")
Order().place_order(PaymentService())
