# Task: Simple Polymorphism with Inheritance
# Create a parent class Animal:

# Method: sound() → returns "Some sound..."

# Create child classes:

# Dog → overrides sound() with "Bark"

# Cat → overrides sound() with "Meow"

# Test by looping over a list of Animal instances and calling .sound().
class Animal():
    def sound(self):
        return "Some Sound...."
class Dog(Animal):
    def sound(self):
        return "Bhav bhav"
class Cat(Animal):
    def sound(self):
        return "Meow"
animals=[Dog(),Cat(),Animal(),Dog(),Cat()]
for animal in animals:
    print(animal.sound())