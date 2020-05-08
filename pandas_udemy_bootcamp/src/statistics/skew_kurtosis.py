''' Higher Central Moments
How to calculate Skew & Kurtosis with scipy.stats '''
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from create_numpy_array import pop


np.set_printoptions(precision=4, suppress=True)

plt.figure(figsize=(12, 8))
plt.hist(pop, bins=75)
plt.title("Absolute Frequencies - Population", fontsize=20)
plt.xlabel("Stock Returns 2017 (in %)", fontsize=15)
plt.ylabel("Absolute Frequency", fontsize=15)
plt.xticks(np.arange(-100, 401, 25))
plt.show()

# __Skew__
# For a normally distributed data skewness should be zero
print(stats.skew(pop))
# Here positive value indicates that we have right skewness and fat
# tails to the right

# __Kurtosis__
# 2 types Fisher and Pearson
print(stats.kurtosis(pop, fisher=True))
print(stats.kurtosis(pop, fisher=False))

# difference in Fisher and Pearson kurtosis is 3
# Fisher < Pearson
# The positive values here determine that we do have fat tails on
# the positive side
