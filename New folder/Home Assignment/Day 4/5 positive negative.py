num = float(input("Enter a number: "))

if num > 0:
    print("Number is positive")
    if num > 100:
        print("and greater than 100")
    else:
        print("and not greater than 100")
elif num < 0:
    print("Number is negative")
else:
    print("Number is zero")
