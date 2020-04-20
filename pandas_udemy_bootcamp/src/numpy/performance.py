""" Performance issues """
import numpy as np
import timeit


size = 3  # number of elements

a = np.arange(size)  # ndarray 
print(len(a))

l1 = list(range(size))  # list
print(len(l1))

b = a + 2
print(timeit.timeit(b, number=1))

# print(get_ipython().run_line_magic('timeit', 'a+2'))
# ndarray: measuring time for element-wise addition'

# get_ipython().run_line_magic('timeit', '[i+2 for i in l]')  # list: measuring time for element-wise addition')

# get_ipython().run_line_magic('timeit', 'a*2  # multiplication')

# get_ipython().run_line_magic('timeit', '[i*2 for i in l]  # multiplication')

# get_ipython().run_line_magic('timeit', 'a**2  # square')

# get_ipython().run_line_magic('timeit', '[i**2 for i in l]  # square')

# get_ipython().run_line_magic('timeit', 'np.sqrt(a)  # square root')

# get_ipython().run_line_magic('timeit', '[i**0.5 for i in l]  # square root') [markdown]

# size = 1000000  # number of elements

# a = np.arange(size)  # ndarray 
# print(len(a))

# l1 = list(range(size))  # list
# print(len(l1))

# get_ipython().run_line_magic('timeit', 'a+2  # ndarray: measuring time for element-wise addition')

# get_ipython().run_line_magic('timeit', '[i+2 for i in l]  # list: measuring time for element-wise addition')

# get_ipython().run_line_magic('timeit', 'a*2  # multiplication')

# get_ipython().run_line_magic('timeit', '[i*2 for i in l]  # multiplication')

# get_ipython().run_line_magic('timeit', 'a**2  # square')

# get_ipython().run_line_magic('timeit', '[i**2 for i in l]  # square')

# get_ipython().run_line_magic('timeit', 'np.sqrt(a)  # square root')

# get_ipython().run_line_magic('timeit', '[i**0.5 for i in l]  # square root') [markdown]

