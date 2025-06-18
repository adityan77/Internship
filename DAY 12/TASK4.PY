try :
    n=int(input("Enter A Number:-"))
    d=100/n
    f=input("Enter File Name:-")
    file=open(f,"r")    

except ZeroDivisionError:
    print("Cannot Divide By Zero!!!")
except FileNotFoundError:
    print("File Does Not Exist!!!")
else:
    print(f"Division Is{d}")
    print(f"File Open Sucessfully!!")
    