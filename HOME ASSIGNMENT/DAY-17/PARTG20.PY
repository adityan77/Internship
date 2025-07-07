# Task 20: Create a parent class Shape with a method draw().
# Create child classes Square, Rectangle, Circle with their own draw() method.
# Store objects in a list and call draw() on each.

class Shape:
    def draw(self):
        print("Drawing shape")

class Square(Shape):
    def draw(self):
        print("Drawing square")

class Rectangle(Shape):
    def draw(self):
        print("Drawing rectangle")

class Circle(Shape):
    def draw(self):
        print("Drawing circle")

shapes = [Square(), Rectangle(), Circle()]
for s in shapes:
    s.draw()
