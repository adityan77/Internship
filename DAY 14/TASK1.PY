# Create a 1D array of numbers from 1–10.
# Create an array of 10 zeros.
# Create an array of 5 ones.
# Create an array of even numbers from 2–20.
# Create an array with random numbers between 0 and 1.
# Create an array of shape (3, 3) filled with the number 7.
# Create an identity matrix of size 4x4.

import numpy as np

print("1D array of numbers from 1-10")
arr1d = np.array([1, 2, 3, 4, 5,6,7,8,9,10])
print(arr1d)

print("\n Array of 10 zeros")
zeros = np.zeros((10))  
print(zeros)

print("\n Array of 5 ones")
ones = np.ones(5)
print(ones)

print("\narray of even numbers from 2 to 20")
even_no = np.arange(2,21,2)
print(even_no)

print("\n Random numbers between 0 and 1")
random_no = np.random.rand(10)
print(random_no)

print("\n array of shape (3, 3) filled with the number 7")
shape_no = np.full((3,3),7)
print(shape_no)

print("\n Identity matrix")
i_matrix = np.eye(4)
print(i_matrix)