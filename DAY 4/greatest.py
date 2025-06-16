# # #elif statement
# # a=int(input("Enter 1st Number:-"))
# # b=int(input("Enter 2nd Number:-"))
# # c=int(input("Enter 3rd Number:-"))
# # if(a>b and a>c):
# #     print(f"{a} Is Greater!!")
# # elif(b>a and b>c):
# #     print(f"{b} Is Greater!!")
# # else:
# #     print(f"{c} Is Greater!!")

# is_rain=input("Is It Raining:-")
# if(is_rain== "Yes"):
#     print("Take Umbrella")

# else:
#     print("Wear Sunglases")

Sub1=int(input("Enter The Sub1 Marks:-"))
Sub2=int(input("Enter The Sub2 Marks:-"))
Sub3=int(input("Enter The Sub3 Marks:-"))
total=Sub1+Sub2+Sub3
Per=total/3
Per=int(Per)
print("\tRESULT")
print(f"SUBJECT 1:{Sub1}")
print(f"SUBJECT 2:{Sub2}")
print(f"SUBJECT 3:{Sub3}")
print(f"TOTAL:{total}")
print(f"PERCENTAGE:{Per}")
if(Per>=90 and Per<=100):
    print("Grade A+")#print("Congrats You Are In Distinction Class!!!")
elif(Per>=70 and Per<=90):
    print("Grade A")#print("Congrats First Class With Distinction")
elif(Per>=60 and Per<=70):
    print("Grade B")#print("Congrats First Class")
elif(Per>=50 and Per<=60):
    print("Grade C")#print("Second Class")
else:
    print("Fail")

