class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    pass

print("Dog IS-A Animal")
Dog().eat()
