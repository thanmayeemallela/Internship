class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.products = [
            Product("Book", 200),
            Product("Pen", 20)
        ]

    def show_cart(self):
        for product in self.products:
            print(product.name, product.price)

ShoppingCart().show_cart()
