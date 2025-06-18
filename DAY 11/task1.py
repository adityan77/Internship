# file = open("Notes.txt","w")
# file.write("This Is File Handling.....")#writing content in file
# file.write("Hello World")#appending content in File 
# print(file.tell())
# file.close()
# #print(file.read())

with open ("Notes.txt","r+") as file:
    file.write("File Handling Example!!")
    file.write("""\nName:-Aditya Suresh Nigale
    I am an Diploma Student
    Studying Computer technology Course""")
    file.seek(0) 
    #print(file.readlines())
    count=0
    for i in file.readlines():
        count+=1
    print(count)
    file.seek(0)
    result=file.read()
    print(result)
    d=result.split() # Split To Find Total Number Of Words
    # print(d)
    print("Total Number Of Words In File",len(d))#Total Number Of Words In File
    print("Total Number Of Character In Files Content",len(result))#Total Number Of Character In Files Content