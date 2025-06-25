# Random Numbers
# Create an array of 5 random numbers between 1-100.
# Create a 3x3 array with random floats between 0-1.
# Create a 4x4 array of random integers between 10-50

import numpy as np

print("array of 5 random numbers between 1-100")
r_num = np.random.randint(1,101 , size=5)
print(r_num)

print("\n 3x3 array with random floats between 0-1")
r_floats = np.random.rand(3,3)
print(r_floats)

print("\n 4x4 array of random integers between 10-50")
r_integers = np.random.randint(10, 51, size=(4,4))
print(r_integers)
                               