# Ask the user to enter a number
number = int(input("Enter a number between 100 and 500: "))

if number >= 100 and number <= 500:
    print("The number is within the valid range (100–500).")
else:
    print("Invalid input. The number is not between 100 and 500.")
