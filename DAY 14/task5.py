# Math Operations
# Perform element-wise addition, subtraction, multiplication, and division between two arrays.
# Perform power and square root operations.
# Use np.sum(), np.mean(), np.min(), np.max(), and np.std().

import numpy as np
arr = np.array([11,22,33,44,55])
arr2 = np.array([66,77,88,99,100])

add = arr + arr2
print("Element wise Addition of array: ",add)

sub = arr - arr2
print("Element wise Substraction of array: ",sub)

mul = arr * arr2
print("Element wise multiplication: ",mul)

div = arr / arr2
print("Element wise division: ",div)

power = arr**2
print("Power of array 1 elements: ",power)

power2 = arr2**2
print("Power of array 2 elements: ",power2)

sq = np.sqrt(arr)
print("Square root  of array 1 elements: ",sq)

sq2 = np.sqrt(arr2)
print("Square root  of array 2 elements: ",sq2)

sum = np.sum(arr)
print("Sum of array 1 elements: ",sum)

sum2 = np.sum(arr2)
print("Sum of array 2 elements: ",sum2)

min = np.min(arr)
print("Minimum element of array 1",min)

min2 = np.min(arr2)
print("Minimum element of array 2",min2)

max = np.max(arr)
print("Maximum element of array 1",max)

max2 = np.max(arr2)
print("Maximum element of array 2",max2)

mean  = np.mean(arr)
print("Mean : ",mean)

std = np.std(arr)
print(std)