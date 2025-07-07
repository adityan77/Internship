# Task 6–9:
# Create class Animal with method sound().
# Dog inherits Animal and overrides sound().
# Puppy inherits Dog and overrides sound() again.

class Animal:
    def sound(self):
        return "Generic Animal Sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Puppy(Dog):
    def sound(self):
        return "Yip"

a = Animal()
d = Dog()
p = Puppy()
print(a.sound())
print(d.sound())
print(p.sound())
