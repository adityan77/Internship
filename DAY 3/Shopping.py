# print("\tEnter Deatils About Your Shopping")
t=int(input("Enter Total Number Of Items"))
for i in range(t) : 
 item_name=input("Enter The Item Name:-")
quantity=int(input("Enter The Quantity Of Item:-"))
price=int(input("Enter Price Of Per Item:-"))
print("\tSHOPPING BILL")
print("Item Name:-",item_name)
print("Quantity",quantity)
print("Price Per Item:-",price)
total=price*quantity
print("Toatal Bill:-",total)
