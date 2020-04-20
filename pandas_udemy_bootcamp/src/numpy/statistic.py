""" Summary Statistics """
import numpy as np


np.random.seed(123)
a = np.random.randint(1, 101, 11)
# creating an array with 11 random integers between 1 and 100

a.sort()
print(a)
print(a.max())  # maximum
print(np.max(a))  # maximum
print(max(a))  # maximum

print(a.min())  # minimum

print(np.mean(a))  # mean
print(a.mean())  # mean

print(np.median(a))  # median

print(np.std(a))  # standard deviation

print(np.var(a))  # variance

print(np.percentile(a, 10))  # 10th percentile
# It means 10% elements are lower to this point and rest are higher
print(np.percentile(a, 90))  # 90th percentile
# It means 90% elements are lower to this point and rest are higher

np.random.seed(123)
a = np.random.randint(1, 101, 11)
# creating an array with 11 random integers between 1 and 100
print(a)

np.random.seed(111)  # different seed!!!
b = np.random.randint(1, 101, 11)
# creating an array with 11 random integers between 1 and 100
print(b)

print(np.cov(a, b))  # covariance matrix
print(np.corrcoef(a, b))  # correlation matrix
