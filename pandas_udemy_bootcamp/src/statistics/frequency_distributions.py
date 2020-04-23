''' Visualizing Frequency Distributions, Relative and Cumulative
Frequencies with plt.hist() '''
import numpy as np
import matplotlib.pyplot as plt
from create_numpy_array import pop, sample


# print(pop)
# print(sample)

# Frequency Distributions with plt.hist()
plt.figure(figsize=(12, 8))
plt.hist(pop, bins=75)
plt.title("Absolute Frequencies - Population", fontsize=20)
plt.xlabel("Stock Returns 2017 (in %)", fontsize=15)
plt.ylabel("Absolute Frequency", fontsize=15)
plt.xticks(np.arange(-100, 401, 25))
plt.show()

plt.figure(figsize=(12, 8))
plt.hist(sample, bins=15)
plt.title("Absolute Frequencies - Sample", fontsize=20)
plt.xlabel("Stock Returns 2017 (in %)", fontsize=15)
plt.ylabel("Absolute Frequency", fontsize=15)
plt.show()


# Relative Frequencies with plt.hist()
np.set_printoptions(precision=4, suppress=True)
print(pop.size)
print(sample.size)

print(np.ones(len(pop)) / len(pop))

# For Relative Frequencies plot we must pass the correct values for
# weights parameter
plt.figure(figsize=(12, 8))
plt.hist(pop, bins=75, weights=np.ones(len(pop)) / len(pop))
plt.title("Relative Frequencies - Population", fontsize=20)
plt.xlabel("Stock Returns 2017 (in %)", fontsize=15)
plt.ylabel("Relative Frequency", fontsize=15)
plt.show()

# This graph doesn't give Relative Frequencies plot by just setting density
# parameter to True as it gives normalized frequency graph
plt.figure(figsize=(12, 8))
plt.hist(pop, bins=50, density=True)
plt.title("INCORRECT-Relative Frequencies - Population", fontsize=20)
plt.xlabel("Stock Returns 2017 (in %)", fontsize=15)
plt.ylabel("Relative Frequency", fontsize=15)
plt.show()


# Cumulative Frequencies with plt.hist()

# For Absolute Cumulative Frequencies plot we must pass correct values:
# density=False and cumulative=True
plt.figure(figsize=(12, 8))
plt.hist(pop, bins=50, density=False, cumulative=True)
plt.title("Cumulative Absolute Frequencies - Population", fontsize=20)
plt.xlabel("Stock Returns 2017 (in %)", fontsize=15)
plt.ylabel("Cumulative Absolute Frequency", fontsize=15)
plt.show()

# For Relative Cumulative Frequencies plot we must pass correct values:
# density=True and cumulative=True
plt.figure(figsize=(12, 8))
plt.hist(pop, bins=50, density=True, cumulative=True)
plt.title("Cumulative Relative Frequencies - Population", fontsize=20)
plt.xlabel("Stock Returns 2017 (in %)", fontsize=15)
plt.ylabel("Cumulative Relative Frequency", fontsize=15)
plt.show()
