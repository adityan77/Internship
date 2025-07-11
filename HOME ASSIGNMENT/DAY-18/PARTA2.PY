# Problem 2: Create Student class with private name and age.
# Use get/set methods. Validate age to be positive.

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age if age > 0 else 0

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")
