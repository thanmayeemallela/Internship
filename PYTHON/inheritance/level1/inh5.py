class Shape:
    def show(self):
        print("This is a shape")

class Rectangle(Shape):
    def area(self):
        print("Area:", 10 * 5)

rectangle = Rectangle()
rectangle.show()
rectangle.area()
