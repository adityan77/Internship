bill_amount = float(input("Enter your bill amount: "))
total = float(input("Enter your total bill amount: "))


if bill_amount < 500:
    discount = 0
elif bill_amount <= 1000:
    discount = 0.05 * total
else:
    discount = 0.10 * total

final_amount = bill_amount - discount

print(f"Final amount : {final_amount}")