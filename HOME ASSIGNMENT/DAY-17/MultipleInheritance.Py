# 🌳 Part B: Multiple Inheritance
# 3.	Create a class Engine:
# o	Method: start() returns Engine started.
# 4.	Create a class MusicSystem:
# o	Method: play() returns Playing music.
# 5.	Create a class Car that inherits from both Engine and MusicSystem:
# o	Method: drive() returns Car is driving.
# o	Test by creating an object of Car and invoking methods from both parent classes.

class Engine():
    def start(self):
        return "Engine Started!!!"
class MusicSystem():
    def play(self):
        return "Playing Music!!!"
class Car(Engine,MusicSystem):
    def drive(self):
        return "Car Is Driving!!!"
C1=Car()
C1.drive()
print(C1.drive())

