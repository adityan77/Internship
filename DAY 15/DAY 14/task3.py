# Indexing and Slicing
# Extract the first 5 elements of an array.
# Extract the last 3 elements.
# Change every second element of an array.
# Extract an element from a 2D array.
# Slice a 2D array to get its first 2 rows and first 2 columns

import numpy as np

arr1 =  np.array([10,15,20,25,30,35,40,45,50])
print(arr1)

print("first five elements: ",arr1[:5])

# print("every second elements: ",arr1[::2])

print("last three elements: ",arr1[-3:])

arr1 [1::2] = 0
print("Changing every second element of array: ",arr1)

arr2d = np.array([[11,21,31], [41,51,61]])
# element = arr2d[11, 21]
# print(element)

slice_2d = arr2d[:2, :2]
print(slice_2d)
