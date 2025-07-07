# Task 15:
# If input is a list → return total of all numbers.
# If input is a number → return double of that number.

def add(x):
    if type(x) == list:
        total = 0
        for num in x:
            total += num
        return total
    else:
        return x + x

print(add([1, 2, 3]))  # Output: 6
print(add(5))          # Output: 10
