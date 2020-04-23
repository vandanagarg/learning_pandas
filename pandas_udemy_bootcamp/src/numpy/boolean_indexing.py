""" Boolean Indexing """
import numpy as np


a = np.arange(1, 11)  # array from 1 to 10
print(a)

mask1 = a > 5  # element-wise check if greater than 5
print(mask1)

mask2 = a < 8  # element-wise check if smaller than 8
print(mask2)

# element-wise check if greater 5 and smaller 8 (logical and)
mask3 = (a > 5) & (a < 8)
print(mask3)

# element-wise check if greater 5 or smaller 8 (logical or)
mask4 = (a > 5) | (a < 8)
print(mask4)

mask5 = ~((a > 5) & (a < 8))  # the opposite of mask3
print(mask5)
# mask5 = not((a > 5) & (a < 8))
# here in vector form we can't use keyword not;
# we have to use ~ symbol for any not operation

# slicing all elements that are greater 5 (fulfill condition of mask1)
print(a[a > 5])
print(a[mask1])  # slicing all elements that fulfill condition of mask1
print(a[mask2])  # slicing all elements that fulfill condition of mask2
print(a[mask3])  # slicing all elements that fulfill condition of mask3
print(a[mask4])  # slicing all elements that fulfill condition of mask4
print(a[mask5])  # slicing all elements that fulfill condition of mask5
