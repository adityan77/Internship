# Reshaping and Flattening
# Create an array with numbers from 1-12 and reshape it into (3, 4).
# Flatten the array back into a 1D array

import numpy as np

arr = np.arange(1, 13)
print("Original  Array:")
print(arr)

r_arr = arr.reshape(3, 4)
print("\nReshaped 2D Array:")
print(r_arr)


f_arr = r_arr.flatten()
print("\nFlattened 1D Array:")
print(f_arr)
