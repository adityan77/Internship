n=int(input("Enter Numerator:-"))
d=int(input("Enter Denominator:-"))

try:
    c=n/d
    print(f"Division Is:-{c}")
except ZeroDivisionError:
    print("Cannot Divide By Zero")

