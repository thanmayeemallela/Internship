class Product:
    def __init__(self, name):
        self.name = name

class PaymentService:
    def pay(self):
        print("Payment done")

class DeliveryService:
    def deliver(self):
        print("Order delivered")

class OnlineOrder:
    def __init__(self):
        self.products = [Product("Book"), Product("Pen")]

    def place_order(self, payment, delivery):
        payment.pay()
        delivery.deliver()

order = OnlineOrder()
print("OnlineOrder HAS-A Products")
print("OnlineOrder USES-A Payment and Delivery Services")
order.place_order(PaymentService(), DeliveryService())
