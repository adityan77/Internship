username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin":
    if password == "1111":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")

       