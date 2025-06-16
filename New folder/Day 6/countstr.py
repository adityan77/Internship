count = 0 

def string():
    global count
    str = "Piyush Dinesh More"
    for i in str:
        if i == 's':
            count += 1
    print(count)
    
string()