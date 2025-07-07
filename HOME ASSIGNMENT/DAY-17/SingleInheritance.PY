# 1.	Create a parent class Person with attributes:
# o	name, age.
# o	Method: display().
# 2.	Create a child class Student that inherits Person:
# o	Add roll_number attribute.
# o	Override the display() method.

class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name:-{self.name}")
        print(f"Age:-{self.age}")
class Student(Person):   
    def display(self,roll):
        self.roll=roll
        print(f"Roll No:-{self.roll}")
s1=Student("Aditya",23)
# print(s1.name())
print(s1.age)
s1.display(23)

        
        
        