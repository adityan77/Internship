# Task: 
# Create a parent class Vehicle with:

# An attribute brand.

# A method describe() that returns: "This is a vehicle."

# Create a child class Car that inherits from Vehicle and:

# Adds an attribute model.

# Overrides the describe() method to return: "This is a [brand] [model]."

# Test it:
# Create an object of Car and call its describe() method.
class Vehicle():
    def __init__(self,brand):
        self.brand=brand
        # self.model=model
    def describe():
        return "This Is Vehicle"
class Car(Vehicle):
    def describe(self,brand,model):
        print(f"This Is A {brand} {model}")
c=Car("BMW")
c.describe("BMW","M4")
