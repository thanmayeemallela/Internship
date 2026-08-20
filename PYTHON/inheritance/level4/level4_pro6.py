class PaymentGateway:
    def pay(self):
        print("Payment successful")

class ShoppingCart:
    def checkout(self, gateway):
        gateway.pay()

print("ShoppingCart USES-A PaymentGateway")
ShoppingCart().checkout(PaymentGateway())
