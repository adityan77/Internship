# Tasks on Inheritance

# Task: 
# Create a parent class Animal with:

# An attribute name.

# A method speak() that returns: "The animal makes a sound."

# Create a child class Dog that inherits from Animal and:

# Overrides the speak() method to return: "The dog barks."

# Test it:
# Create an object of Dog and call its speak() method.
class Animal():
    def __init__(self,name):
        self.name=name
    def speak():
        print("The Animal Makes A Sound")
class Dog(Animal):
    def speak(self):
        print("The Dog Barks")
dog=Dog("Rocky")
dog.name
dog.speak()
