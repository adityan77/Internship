def menu(arth,a,b):
    if arth == '+':
        print(a+b)
    if arth == '-':
        print(a-b)
    if arth == '*':
        print(a*b)
    if arth == '/':
        print(a/b)
st=input("Enter The Operator To Perform Operation(+,-,/,*):-")
m=int(input("Enter 1st Number:-"))
n=int(input("Enter 2nd Number:-"))
menu(st,m,n)
