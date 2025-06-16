sub1 = int(input("Enter The Marks of Subject 1 : "))
sub2 = int(input("Enter The Marks of Subject 2 : "))
sub3 = int(input("Enter The Marks of Subject 3 : "))

total = sub1+sub2+sub3
avg = total / 3
print("-----RESULT-----")
print(f"Subject 1 = {sub1}")
print(f"Subject 2 = {sub2}")
print(f"Subject 3 = {sub3}")
print(f"Total Marks Of Subject is = {total}")
print(f"Percentage is = {avg:.2f}")
if avg >= 80 and avg <= 100:
    print("A grade")
elif avg >=60 and avg<= 79:
    print("B grade")
elif avg >=40 and avg <= 59:
    print("C grade")
else :
    print("fail")

