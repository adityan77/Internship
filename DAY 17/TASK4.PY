# Task:
# Create a parent class Number.

# Create SumNumber and ProductNumber classes that inherit from Number.

# Create a final class FinalCalculator that inherits from both.

# Call parent methods directly:

# SumNumber.sum(self, a, b).

# ProductNumber.product(self, a, b).

# Test:

# FinalCalculator().sum(5, 10) → 15

# FinalCalculator().product(3, 4) → 12

class Number:
    
     pass
class Sumnumber(Number):
    def sum(a,b):
        # self.a=a
        # self.b=b
        print(a+b)
class ProductNumber(Number):
    def Pro(a,b):
        # self.a=a
        # self.b=b

        print(a*b)        
class Final(Sumnumber,ProductNumber):
    def __init__(self):
        Sumnumber(self.a,self.b)
        ProductNumber(self.a,self.b)

Sumnumber.sum(2,3)
Final.sum(5,3)
Final.Pro(3,4)
