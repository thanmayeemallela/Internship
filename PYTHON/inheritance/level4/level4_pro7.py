class Keyboard:
    def type(self):
        print("Typing")

class Laptop:
    def __init__(self):
        self.keyboard = Keyboard()

print("Laptop HAS-A Keyboard")
Laptop().keyboard.type()
