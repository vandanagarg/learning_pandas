""" Numpy Array (Indexing and Slicing multi-dimensional arrays) """
import numpy as np


# creating matrix with 3 rows and 4 columns
a = np.arange(1, 13)
a = a.reshape(3, 4, order="F")  # order="F" orders elements vertically
print(a)

a = np.arange(1, 13)
a = a.reshape(3, 4, order="C")  # "C" orders elements horizontally (default)
print(a)

print(a[0])  # first row (index position 0)
print(a[1])  # second row (index position 1)
print(a[2])  # third row (index position 2)
print(a[-1])  # last row (index position -1)

print(a[1][1])  # second row, second column
print(a[1, 1])  # more convenient in one square bracket
print(a[2, -1])  # third row, last column

print(a[:, 0])  # all rows, first column
print(a[:, 1])  # all rows, second column
print(a[:, -1])  # all rows, last column
print("\n Slicing:")
print(a[:2, 1: 3])  # first two rows, column two and three

print("\n Transpose matrix:")
print("a: \n {}".format(a))
print(a.T)  # Transpose: switching axes (attribute)
print(a.transpose())  # same (method)

print("\n a: \n {}".format(a))
a[:, -1] = a[:, -1]/4  # changing slice inplace
print("\n after division: \n {}".format(a))
print("\n")

a = np.arange(1, 13).reshape(3, 4)  # creating a 3x4 matrix
print(a)
print(a.sum())  # sum over all elements in matrix
print(a.sum(axis=0))  # sum of each column/ along rows
print(a.sum(axis=1))  # sum of each row/ along columns

print("\n Cumulative sum")
print(a.cumsum())  # cumulative sum of all elements
print(a.cumsum(axis=0))  # cumulative sum for each column
print(a.cumsum(axis=1))  # cumulative sum for each row

print("\n Product")
print(a)
print(a.prod())  # product over all elements
print(a.prod(axis=0))  # product over all elements in each column
print(a.prod(axis=1))  # product over all elements in each row [markdown]
