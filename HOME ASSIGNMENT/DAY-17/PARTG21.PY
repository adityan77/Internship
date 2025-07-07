# Task 21: Create a Person class with name and age.
# Employee inherits Person and adds salary.
# Teacher and Engineer inherit Employee and add subject/specialization.
# Each class has a display() method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name, "Age:", self.age)

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    def display(self):
        super().display()
        print("Salary:", self.salary)

class Teacher(Employee):
    def __init__(self, name, age, salary, subject):
        super().__init__(name, age, salary)
        self.subject = subject
    def display(self):
        super().display()
        print("Subject:", self.subject)

class Engineer(Employee):
    def __init__(self, name, age, salary, specialization):
        super().__init__(name, age, salary)
        self.specialization = specialization
    def display(self):
        super().display()
        print("Specialization:", self.specialization)

t = Teacher("Anil", 30, 40000, "Math")
e = Engineer("Priya", 28, 60000, "AI")
t.display()
e.display()
