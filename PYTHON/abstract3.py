from abc import ABC , abstractmethod
class shape(ABC):
    def area(self):
        pass;
class circle (shape):
    def area(self):
        print("arear of a circle is pir2")
class rectangle (shape):
    def area(self):
        print("area of a rectangle length*breath")
c=circle();
r=rectangle();
c.area();
r.area();