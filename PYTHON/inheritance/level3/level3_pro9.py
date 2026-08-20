class DeliveryService:
    def deliver(self, address):
        print("Food delivered to", address)

class FoodOrder:
    def send_order(self, delivery):
        delivery.deliver("Rupa's house")

FoodOrder().send_order(DeliveryService())
