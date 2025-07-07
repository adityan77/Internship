# Task 16–17:
# Create Employee class with name, salary.
# Manager inherits Employee and adds department.
# Override display() and use super().

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("Name:", self.name, "Salary:", self.salary)

class Manager(Employee):
    def __init__(self, name, salary, dept):
        super().__init__(name, salary)
        self.dept = dept
    def display(self):
        super().display()
        print("Department:", self.dept)

m = Manager("Riya", 50000, "HR")
m.display()
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("Name:", self.name, "Salary:", self.salary)

class Manager(Employee):
    def __init__(self, name, salary, dept):
        super().__init__(name, salary)
        self.dept = dept
    def display(self):
        super().display()
        print("Department:", self.dept)

m = Manager("Riya", 50000, "HR")
m.display()

class BankAccount:
    def calculate_interest(self):
        return 100

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return 150

s = SavingsAccount()
print(s.calculate_interest())
