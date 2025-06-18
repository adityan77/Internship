prices={"apple":10,"banana":5}
try:
    fruit=input("Enter Fruit Name:-")
    price=prices[fruit]
    filee=input("Enter A File Name:-")
    with open(filee,"r") as file:
        content=file.read()
        print(f"The Price:-{price}")
       
except(KeyError,FileNotFoundError) as e:
    # print("File Not Found!!!")
    # print("Key Not Found!!!")
    print(e)
    