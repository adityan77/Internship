# Task 13–14:
# Create Bird, Fish, Dog classes with move() method.
# Use test_move() to call move() polymorphically.

class Bird:
    def move(self):
        return "Flies"

class Fish:
    def move(self):
        return "Swims"

class Dog:
    def move(self):
        return "Walks"

def test_move(obj):
    print(obj.move())

test_move(Bird())
test_move(Fish())
test_move(Dog())
