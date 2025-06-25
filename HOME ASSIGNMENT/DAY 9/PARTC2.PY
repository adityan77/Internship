# o	Create a dictionary inventory where keys are product names ("pen", "notebook", "eraser") and values are quantities.
# o	Write a function update_stock(item, quantity) to increase stock.
# o	If item is not in inventory, add it.
# Create a dictionary with initial inventory

# Function to update stock
def update_stock(item, quantity,inventory):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"Updated inventory: {item} = {inventory[item]}")



inventory = {
    "pen": 10,
    "notebook": 5,
    "eraser": 8
}


i=input("Enter Item Name To Be Uodated:-")
q=int(input("Enter The Quantity Of Item:-"))
update_stock(i, q,inventory)        
print("Final Inventory:", inventory)
