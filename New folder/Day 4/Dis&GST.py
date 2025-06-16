item_name = input("Enter The Name of Item ")
quantity = int(input("Enter The Quantity os Item "))
price = int(input("Enter The Price per item "))

calculate = quantity * price
discount = calculate * 0.1 
dis = calculate - discount

gst =  dis * 0.18
total = gst + dis

print("\t-------SHOPPING BILL-------")
print(f"\tThe Name of Item is {item_name}")
print(f"\tThe Quantity of Item is {quantity}")
print(f"\tThe Price of Item is {price}")
print(f"\tThe Final Bill is {calculate}")

print(f"\t10% Discount on {calculate}  {dis}")
print(f"\tTotal Bill with GST : {total}")
