# #Part B: If-Elif-Else
# o	90–100: Grade A
# o	75–89: Grade B
# o	50–74: Grade C
# o	Below 50: Fail
marks=int(input("Enter Your Marks (0-100):-"))
if marks>=90 and marks<=100:
    print("A Grade..!!")
elif marks>=75 and marks<=89:
    print("B Grade..!!")
elif marks>=50 and marks<=74:
    print("C Grade..!!")
else:
    print("Fail..!!")