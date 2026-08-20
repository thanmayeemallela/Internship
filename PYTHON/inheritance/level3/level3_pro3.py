class PaymentGateway:
    def pay(self, amount):
        print("Payment gateway paid:", amount)

class ShoppingCart:
    def checkout(self, gateway):
        print("Checking out cart")
        gateway.pay(1500)

cart = ShoppingCart()
cart.checkout(PaymentGateway())
