def factorial(num):
    fact=1
    i=1
    while i<=num:
        fact=fact*i
        i=i+1
    return fact
n=int(input("Enter a number:-"))
facts=factorial(n)
print(facts)