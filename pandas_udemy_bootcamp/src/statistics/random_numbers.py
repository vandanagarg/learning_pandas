''' Common Probability Distributions and Confidence Intervals
Generating Random Numbers with Numpy using module random'''
import numpy as np


# generate random integers in the range 1 to 10
print(np.random.randint(low=1, high=11, size=10))

# returns random floats in half open interval[0.0, 1.0)
# continuos uniform in nature
print(np.random.random(size=10))

# uniform numbers in a specific range, excludes high
print(np.random.uniform(low=1, high=10, size=10))

# generate random samples from a normal distribution
print(np.random.normal(size=10))
# default mean, std 0 - so here the mean and std of the samples is 0
# loc = mean, scale = std of the normal distribution
print(np.random.normal(loc=100, scale=10, size=10))
# here the mean is 100 and std of the samples is 10


# Reproducibility with np.random.seed()
print("\n reproducibility with np.random.seed() \n")
print(np.random.randint(low=1, high=11, size=10))
print(np.random.randint(low=1, high=11, size=10))
print(np.random.randint(low=1, high=11, size=10))

np.random.seed(123)
print(np.random.randint(low=1, high=11, size=10))

np.random.seed(123)
print(np.random.randint(low=1, high=11, size=10))

np.random.seed(5)
print(np.random.randint(low=1, high=11, size=10))

np.random.seed(5)
print(np.random.randint(low=1, high=11, size=10))
