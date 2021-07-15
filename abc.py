from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        return 0


class Square(Shape):
    side = 4
    def area(self):
        print("Area of square",self.side * self.side)

class Rectangle(Shape):
    width = 5
    length = 10
    def area(self):
        print("Area of rectange: ",self.width * self.length)

square = Square()
rectange = Rectangle()
square.area()
rectange.area()
shape = Shape()
