# Inspecting Arrays
# Create a sample array of float64
# Find the shape, size, and dtype of an array.
# Change the dtype of an array from float64 to int32.
 # Find the number of dimensions (ndim) of an array.

import numpy as np

s_array = np.array([1.3,3.7,5.9,3.9],dtype=np.float64)
print(s_array)

s_array2d = np.array([[1.3 , 2.5], [5.7 , 7.9]],dtype=np.float64)
print(s_array2d)

print("Shapes of the array: ",s_array.shape)
print("Size of array: ",s_array.size)

s_arrayint = s_array.astype(np.int32)
print(s_arrayint.dtype)
print(s_arrayint)