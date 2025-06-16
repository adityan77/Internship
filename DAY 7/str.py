count=0
def str(name):
    global count
    for i in name :
        if i=="A" or i=="a":
            count=count+1
    print(count)
n=input("Enter A string:-")
str(n)