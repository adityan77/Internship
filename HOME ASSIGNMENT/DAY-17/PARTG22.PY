# Task 22: Create a base class Polygon.
# Create child classes Square, Rectangle, Triangle with area methods.
# Use polymorphism to call area() from a list of shapes.

class Polygon:
    def area(self):
        return "Not defined"

class Square(Polygon):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

class Rectangle(Polygon):
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

shapes = [Square(4), Rectangle(5, 3), Triangle(6, 4)]
for shape in shapes:
    print(shape.area())
