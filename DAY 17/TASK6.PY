# Task: Polymorphism with Similar Methods (Duck Typing)
# Create classes:

# Car with method move() → returns "Car is driving..."

# Boat with method move() → returns "Boat is sailing..."

# Plane with method move() → returns "Plane is flying..."

# Create a function:

# def test_move(vehicle):
#     print(vehicle.move())

# Test by passing instances of Car, Boat, and Plane.
class car():
   def move():
    return "Car is driving..."
class Boat():
  def move():
    return "Boat is sailing..."
class Palne():
  def move():
    return "Plane Is Flying"
def test_move(vehicle):
     print(vehicle.move())
     
vehicle=input("Enter Vehicle Name(Car,Boat,Plane!):-")
test_move(vehicle)