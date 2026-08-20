class Engine:
    def start(self):
        print("Engine started")

class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        self.move()

car = Car()
print("Car IS-A Vehicle")
print("Car HAS-A Engine")
car.drive()
