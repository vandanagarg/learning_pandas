""" Numpy Array (element-wise operations / vectorization) """
import numpy as np


print(np.arange(1, 11))  # create numeric ndarray from 1(incl.) to 11(excl.)
print(np.arange(1, 11, 2))  # only every second number is created

l1 = [1, 2, 3, 4]
print(l1 * 2)  # this is not an element-wise operation

l2 = []  # element-wise operations with lists require a bunch of code
for i in l1:
    l2.append(i*2)
print(l2)

# l1 + 2  # this is not an element-wise operation and does not work at all

# element-wise (vectorized) operations are pretty simple with ndarrays
print("\n element-wise (vectorized) operations:")
print("\n 1. int ndarray")
a = np.arange(1, 5)  # create ndarray from 1 to 4 (both including)
print(a)
print(type(a))  # <class 'numpy.ndarray'>
print(type(a[0]))  # <class 'numpy.int64'>
print(a * 2)  # multiplication
print(a + 2)  # addition
print(a**2)  # all elements squared
print(2**a)  # can serve as exponent as well
print(np.sqrt(a))  # square root of all elements
print(np.exp(a))  # exponentiation with e
print(np.log(a))  # natural logarithm
print(a.sum())  # sum of all elements (ndarray method)
print(np.sum(a))  # sum of all elements
print(sum(a))
print(a.size)  # number of elements in ndarray (ndarray attribute)
print(len(a))

print("\n 2. float ndarray")
b = np.array([-2, -1, -0.5, 0, 1, 2, 3.5])
print(b)
print(type(b))  # <class 'numpy.ndarray'>
print(type(b[0]))  # <class 'numpy.float64'>
print(np.abs(b))  # absolute values of all elements

c = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
print(c)
print(np.ceil(c))  # element-wise rounding up
print(np.floor(c))  # element-wise rounding down

# evenly round all elements to the given number of decimals.
print(np.around([-3.23, -0.76, 1.44, 2.65, ], decimals=0))
print(np.around([-3.23, -0.76, 1.44, 2.65, ], decimals=1))
