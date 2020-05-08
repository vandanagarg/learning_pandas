''' Discrete Uniform Distributions and Continuous Uniform Distributions '''
import numpy as np
import matplotlib.pyplot as plt


print(np.random.randint(low=1, high=7, size=10))

print("\n Discrete Uniform Distributions")
np.random.seed(123)
a = np.random.randint(low=1, high=7, size=100000)
print(a)
print(a.mean())
print(a.std())
print(100000/6)

plt.figure(figsize=(12, 8))
plt.hist(a, bins=6, ec="black")
plt.title("Discrete Uniform Distribution", fontsize=20)
plt.ylabel("Absolute Frequency", fontsize=15)
plt.show()

plt.figure(figsize=(12, 8))
plt.hist(a, bins=6, weights=np.ones(len(a)) / len(a), ec="black")
plt.title("Discrete Uniform Distribution", fontsize=20)
plt.ylabel("Relative Frequency", fontsize=15)
plt.show()

# doesn't plot relative frequency - plots probability density
# the area under the curve is one ans y axis is normalized .200 * 5 = 1
plt.figure(figsize=(12, 8))
plt.hist(a, bins=6, density=True, ec="black")
plt.title("Discrete Uniform Distribution", fontsize=20)
plt.show()

plt.figure(figsize=(12, 8))
plt.hist(a, bins=6, density=True, cumulative=True, ec="black")
plt.title("Discrete Uniform Distribution", fontsize=20)
plt.ylabel("Cumulative Relative Frequency", fontsize=15)
plt.show()

print("\n Continuous Uniform Distributions")
np.random.seed(123)
b = np.random.uniform(low=0, high=10, size=10000000)
print(b)
print(b.mean())
print(b.std())

# probability density function
# since we have a continuous random variable hence density=True
plt.figure(figsize=(12, 8))
plt.hist(b, bins=1000, density=True)
plt.title("Continuous Uniform Distribution", fontsize=20)
plt.ylabel("pdf", fontsize=15)
plt.show()
''' Here the y axis is normalized in a way that area under the curve is one
10 * .10 = 1, Also probability at a particular point/ single outcome is zero
as area = 0 but within a range/interval eg point 0 to 2 probability is area
under the curve 2 * .10 = .20 or 20%
'''

# cumulative distribution function for Continuous Uniform random variable
''' cdf is integral over the pdf, it shows the area under the curve of pdf '''
plt.figure(figsize=(12, 8))
plt.hist(b, bins=1000, density=True, cumulative=True)
plt.grid()
plt.title("Continuous Uniform Distribution", fontsize=20)
plt.ylabel("cdf", fontsize=15)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.show()
