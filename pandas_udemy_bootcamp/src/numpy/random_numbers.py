""" Random Numbers """
import numpy as np


# creating 10 random integers between 1 (incl.) and 101 (excl.)
a = np.random.randint(1, 101, 10)
print(a)

np.random.seed(123)  # setting a seed enables reproducibility
a = np.random.randint(1, 101, 10)
print(a)

# creating 10 normal distributed numbers with mean 5 and std 2
print(np.random.normal(5, 2, 10))

print("\n creating array \n")
b = np.arange(1, 101)  # creating array b from 1 to 100
print(b)

print("\n random shuffle array \n")
np.random.shuffle(b)  # randomly shuffle ndarray b
print(b)
print("\n sorting array \n")
b.sort()  # sorting ndarray b again
print(b)
# sort() method doesn't give an option to sort in reverse order; to do so use:
print(b[::-1])  # sorting in reverse order

print("\n creating a random sample from given array \n")
print(b)
np.random.seed(123)
# randomly creating a 100 elements sample of ndarray b with/without replacement
b1 = np.random.choice(b, 100, replace=True)
print(b1)
# replace=True means we can choose the same element again else it chooses an
# element only once

b1.sort()  # sorting b1
print(b1)

print(np.unique(b1))  # unique elements of b1
print(np.array(list(set(b1))))  # same
print(np.unique(b1).size)  # how many unique elements?
print(np.unique(b1, return_index=True, return_counts=True))
# .unique()-method is quite informative,
# return_index gives the index of the first occurrence of the element

# if we pass replace=False, no element is repeated and we get all unique
# elements as b
b2 = np.random.choice(b, 100, replace=False)
print(b2)
print(np.unique(b2).size)  # how many unique elements?
