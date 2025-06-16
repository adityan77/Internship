
def arithmetic(arithmetic,a,b,):
    if arithmetic == '+':
        print("Addition is ",a+b)
    elif arithmetic == '-':
        print("Subtraction is ",a-b)
    elif arithmetic == '*':
        print("Multiplition is ",a*b)
    elif arithmetic == '/':
        print("division is ",a/b)
    else :
        print("Sign is Invalid")
    
str = input("Enter The sign between  + - * / ")
c= int(input("Enter The First Number"))
d = int(input("Enter The Second Number"))
arithmetic(str,c,d)