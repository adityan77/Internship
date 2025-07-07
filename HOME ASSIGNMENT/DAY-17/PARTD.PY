# Task 10–12:
# Create base class Shape with method area().
# Rectangle, Circle, Triangle inherit from Shape and implement area().

import math

class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        return "Not implemented"

class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__("Rectangle")
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

r = Rectangle(4, 5)
c = Circle(3)
t = Triangle(6, 4)
print(r.area())
print(c.area())
print(t.area())
