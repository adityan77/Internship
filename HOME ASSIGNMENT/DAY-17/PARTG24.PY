# Task 24: Create custom exceptions: BankError, InsufficientBalanceError, InvalidAmountError.
# Simulate a withdrawal function that raises these when needed.

class BankError(Exception):
    pass

class InsufficientBalanceError(BankError):
    pass

class InvalidAmountError(BankError):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Amount must be greater than zero")
    if amount > balance:
        raise InsufficientBalanceError("Not enough balance")
    return balance - amount

try:
    print(withdraw(500, 600))
except BankError as e:
    print("Error:", e)
