# Multiple Except Blocks

# Input: take a number and a file name.

# Divide 100 by the number and open the file.

# Catch both ZeroDivisionError and FileNotFoundError.

try :
    n=int(input("Enter A Number:-"))
    d=100/n
except ZeroDivisionError:
    print("Cannot Divide By Zero!!!")
try:
    f=input("Enter File Name:-")
    file=open(f,"r")    

except FileNotFoundError:
    print("File Not Found!!!")
