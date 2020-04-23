""" Numpy Basics - Creating ndarray """
import numpy as np


l1 = list(range(1, 11))  # create a list

my_array = np.array(l1)  # transform list into a numpy array (ndarray)
print(my_array)
# ndarray's help perform operations on large datasets in vectorized manner
print(type(my_array))  # <class 'numpy.ndarray'>

# same as lists, ndarrays store multiple elements (is iterable)
for i in my_array:
    print(i)

l2 = [1, 2.5, "Dog", True]  # lists can store different datatypes
for i in l2:
    print(type(i))

""" in ndarrays, all elements must have same datatype; numpy transforms
automatically into the least common datatype: int, float, bool all can be
converted into str and not vice versa for all case. Hence, string is typically
the least common denominator """
a = np.array(l2)
for i in a:
    print(type(i))  # <class 'numpy.str_'>

# while creating a numpy array all elements are automatically
# changed in a single datatype
b_int = np.array([1, 2, 3])
print(b_int.dtype)  # int64

b_float = np.array([1, 2., 3])
print(b_float.dtype)  # float64

b_str = np.array([1., "2", 3])
print(type(b_str))  # <class 'numpy.ndarray'>
print(b_str.dtype)  # <U32 denotes string
# can check single datatype of all elements with attribute .dtype
