class Product:
    def __init__(self, name):
        self.name = name

class PaymentGateway:
    def pay(self):
        print("Payment successful")

class ShoppingCart:
    def __init__(self):
        self.products = [Product("Laptop"), Product("Mouse")]

    def checkout(self, gateway):
        gateway.pay()

cart = ShoppingCart()
print("ShoppingCart HAS-A Products")
print("ShoppingCart USES-A PaymentGateway")
cart.checkout(PaymentGateway())
