# Task 23: Create a base Animal class with methods sound() and move().
# Create Lion, Snake, Parrot classes with specific behaviors.
# Store them in a list and call their methods.

class Animal:
    def sound(self):
        return "Some sound"
    def move(self):
        return "Some movement"

class Lion(Animal):
    def sound(self):
        return "Roar"

class Snake(Animal):
    def move(self):
        return "Slither"

class Parrot(Animal):
    def sound(self):
        return "Talk"

animals = [Lion(), Snake(), Parrot()]
for a in animals:
    print("Sound:", a.sound())
    print("Move:", a.move())
