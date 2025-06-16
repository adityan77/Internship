# 8.	Print the following right-angle triangle pattern using a for loop:
#    *
#   ***
#  *****
# *******
# Take a number n as input and print a triangle with n rows using *.
# Take number of rows as input
n = int(input("Enter the number of rows: "))

# Loop to print the triangle
for i in range(1, n + 1):
    spaces = n - i  # Number of spaces
    stars = 2 * i - 1  # Number of stars
    print(" " * spaces + "*" * stars)

    
    
