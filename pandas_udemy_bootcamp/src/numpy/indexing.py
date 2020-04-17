""" Numpy Array (Indexing and Slicing) """
import numpy as np


a = np.arange(1, 11)  # array from 1 to 10 (incl.)
print(a[0])  # first element at index position 0 (zero-based indexing!)
print(a[1])  # second element (index position 1)
print(a[-1])  # last element
print(list(enumerate(a)))  # list of index,value tuples
print(a[2:6])  # slicing from index position 2 (incl.) till position 6 (excl.)
print(a[:])  # all elements
print(a[:5])  # all elements until index position 5 (excl.)
print(a[6:])
# all elements from index position 6 (incl.) till the last element (incl.)
print(a[::2])  # every second element, starting from first element
print(a[::3])  # every third element, starting from first element
print(a[2::3])
# every third element, starting from third element (index position 2)
a[0] = 100  # ndarrays are mutable, changing first element to 100
a[-1] = 101  # changing last element to 101
print(a)
# in contrast to lists, ndarrays allow braodcasting, assigning one new value
# to multiple elements
a[2:5] = 50
print(a)
# assigning multiple new values to multiple elements
a[2: 5] = [50, 51, 52]
print(a)

# creating new ndarray b from a
a = np.arange(1, 11)
b = a[2:8]  # making a slice of ndarray a and assign new variable b
print(b)
b[0] = 100  # changing first element of ndarray b
print(b)
print(a)  # respective element of ndarray a has changed as well!!!

l1 = list(range(1, 11))  # lists behave differently
m = l1[2:8]  # here a copy of the slice of l1 is created
print(m)
m[0] = 100  # changing first element of slice m
print(m)
print(l1)  # no effect on l !!!

# creating new ndarray b_copy from a using copy() method
print("\n Using copy() method:")
a = np.arange(1, 11)
b_copy = a[2:8].copy()  # making a slice of ndarray a and assign to b_copy
print(b_copy)
b_copy[0] = 100  # changing first element of ndarray b_copy
print(b_copy)
print(a)  # respective element of ndarray a does not change in this case
