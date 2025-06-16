a=int(input("Enter 1st Number:-"))
b=int(input("Enter 2nd Number:-"))
operator=input("Enter A operator To Perform Operations(+,-,/,*):-")
if operator=='+':
    print(f"Additon Of {a} And {b} Is:-{a+b}")
elif operator=='-':
    print(f"Substraction Of {a} And {b} Is:-{a-b}")
elif operator=='*':
    print(f"Multiplication Of {a} And {b} Is:-{a*b}")
elif operator=='/':
    print(f"Division Of {a} And {b} Is:-{a/b}")
else:
    print("Enter A Valid Operator!!!")
