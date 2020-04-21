""" Performance issues """
import timeit


print("\n testing performance with 3 elements")
setup = '''
import numpy as np
size = 3  # number of elements

a = np.arange(size)  # ndarray
# print(len(a))

l1 = list(range(size))  # list
# print(len(l1))
'''

print(timeit.timeit('''import numpy as np
size = 3
a = np.arange(size)
a+2''', number=2))

print(timeit.timeit('a+2', setup, number=1))
# ndarray: measuring time for element-wise addition

print(timeit.timeit('[i+2 for i in l1]', setup, number=1))
# list: measuring time for element-wise addition

print(timeit.timeit('a*2', setup, number=1))
# multiplication

print(timeit.timeit('[i*2 for i in l1]', setup, number=1))
# multiplication

print(timeit.timeit('a**2', setup, number=1))
# square

print(timeit.timeit('[i**2 for i in l1]', setup, number=1))
# square

print(timeit.timeit('np.sqrt(a)', setup, number=1))
# square root

print(timeit.timeit('[i**0.5 for i in l1]', setup, number=1))
# square root


print(timeit.timeit('''import numpy as np
size = 3
a = np.arange(size)
a+2''', number=2))

print("\n testing performance with 1000000 elements")

large_setup = '''
import numpy as np
size = 1000000  # number of elements

a = np.arange(size)  # ndarray
# print(len(a))

l1 = list(range(size))  # list
# print(len(l1))
'''

print(timeit.timeit('''import numpy as np
size = 1000000
a = np.arange(size)
a+2''', number=2))

print(timeit.timeit('a+2', large_setup, number=1))
# ndarray: measuring time for element-wise addition

print(timeit.timeit('[i+2 for i in l1]', large_setup, number=1))
# list: measuring time for element-wise addition

print(timeit.timeit('a*2', large_setup, number=1))
# multiplication

print(timeit.timeit('[i*2 for i in l1]', large_setup, number=1))
# multiplication

print(timeit.timeit('a**2', large_setup, number=1))
# square

print(timeit.timeit('[i**2 for i in l1]', large_setup, number=1))
# square

print(timeit.timeit('np.sqrt(a)', large_setup, number=1))
# square root

print(timeit.timeit('[i**0.5 for i in l1]', large_setup, number=1))
# square root
