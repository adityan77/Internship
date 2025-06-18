# Task 3: List Access and Conversion
# Instructions:

# Create a list: data = [10, 20, 30]

# Ask the user for an index.

# Access that index and convert it to a float.

# Catch both IndexError and ValueError.
data=[10,20,30,"Adi"]
try:
    ind=int(input("Enter A Index:-"))
    value= float(data[ind])
    
# except IndexError:
#     print("Index Is Out Of Range!!!")
# except ValueError:
#     print("Value Cannot be Converted")
except(IndexError,ValueError) as e:
    print("Index Is Out Of Range!!!")
    print("Value Cannot be Converted")