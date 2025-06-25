# Create a BankAccount Class
# Attributes:

# account_holder, balance.

# Methods:

# deposit(amount) — Adds money.

# withdraw(amount) — Subtracts money if available.

# display_balance() — Shows the balance.

# Test it: Create an account, deposit money, withdraw money, and display the balance.
class Bankacc:
    def __init__(self):
        self.acc_holder=input("Enter Name Of Account  Holder:-")
        self.bal=float(input("Enter Balance:-"))
    def deposit(self,amount):
        self.bal+=amount
    def withdraw(self,amount):
       self.bal-=amount
    def display(self):
        print(f"Availabel Balance:-{self.bal}")
b=Bankacc()
a=float(input("Enter Amount:-"))
b.deposit(a)
b.display()
s=input("Do You Want To Withdraw:-")
# s.lower
if s=='yes':
    a=int(input("Enter A Amount To Withdraw:-"))
    b.withdraw(a)
    b.display()
