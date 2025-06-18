student={"Name":"Alice","Age":20,"Course":"Python"}
#Accesssing The Value
print(student["Name"])

#Modifying The Age
student["Age"]=21
print(student)

student["city"]="Mumbai"
print(f"Modified Dictionary:-{student}")
del(student["Course"])
print(f"Dictionary After Deletion:-{student}")

# PART:-B
print("Looping Through Dictinoary:-")
for key,value in student.items():
    print(f"{key}:{value}")

#2
if "Name" in student:
    print("Name Key Exist")

#3
grade=student.get("grade","Not Assigned")
print(f"Grade",grade)
