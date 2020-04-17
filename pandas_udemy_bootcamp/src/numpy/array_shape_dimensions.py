""" Numpy Array (Shape and multiple dimensions) """
import numpy as np


a = np.arange(1, 13)  # creating array from 1 to 12
print(type(a))
print(a.shape)  # one-dimensional array, 12 elements in one dimension (vector)
# shape = row size/length * column size/length

a = a.reshape(2, 6)  # reshaping a: 2 rows / 6 columns
print(a)
print(a.shape)  # two-dimensional array: 2 rows / 6 columns (matrix)

a = a.reshape(6, 2)  # two-dimensional array: 6 rows / 2 columns
print(a)
print(a.shape)
print(a + 100)  # element-wise operations still work

print(a.reshape(3, 4))  # two-dimensional array: 3 rows / 4 columns (matrix)
# print(a.reshape(3, 5))  # not possible with 12 elements

a = a.reshape(2, 2, 3)  # creating a three-dimensional array
print(a)
print(a.shape)

a = a.reshape(3, 4, 1)  # creating a three-dimensional array
print(a)
print(a.shape)

# creating 2-dim ndarray with one line of code
b = np.arange(1, 101).reshape(25, 4)
print(b)
