# Final Mini Project
# Perform the following in one script:
# Create a 5x5 array of random integers between 1–100.
# Find the min, max, mean, and sum of the array.
# Replace all numbers > 50 with -1.
# Save the array to a .npy file.
# Load it back and print the contents.

import numpy as np
r_integers = np.random.randint(1, 101, size=(5,5))
print(r_integers)

mean = np.mean(r_integers)
print("mean: ",mean)
min = np.min(r_integers)
print("Min: ",min)
max = np.max(r_integers)
print("max: ",max)
sum = np.sum(r_integers)
print("sum: ",sum)

r_integers[r_integers > 50] = -1
print(r_integers)
