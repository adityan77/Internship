# •	Create a dictionary where keys are roll numbers and values are student names.
# •	Ask user for a roll number and print the corresponding name.

stud={1:"Aditya",36:"Prasad",31:"Piyush"}
roll=int(input("Enter Roll Number:-"))
for key in stud.keys():
    if key==roll:
        print(stud[key])
        break
    elif key!=roll:
        print("Roll No Not Found")
        break    
    