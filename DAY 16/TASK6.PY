# Calculator Class with Static Methods
# Create a Calculator class:

# add(a, b) — Static method

# multiply(a, b) — Static method

# is_even(number) — Static method

# Test it: Call these methods without creating an object, like:

# Calculator.add(5, 3)  # Returns 8 
class Calculator:
    @staticmethod
    def add(a,b):
        print(f"Addition:-{a+b}")
    @staticmethod
    def mul(a,b):
        print(f"Multiplication:-{a*b}")
    @staticmethod
    def is_even(num):
        if num%2==0:
            print("Even Number!!")
        else:
            print("Odd Number!!")
C=Calculator()
no1=int(input("Enter 1st Number:-"))
no2=int(input("Enter 2nd Number:-"))
n=int(input("Enter A Number To Check Even Or Odd:-"))
C.add(no1,no2)
C.mul(no1,no2)
C.is_even(n)
