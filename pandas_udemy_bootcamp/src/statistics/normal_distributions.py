''' Normal Distribution
Creating a normally distributed Random Variable '''
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


mu = 100
sigma = 2
size = 1000000

np.random.seed(123)
pop = np.random.normal(loc=mu, scale=sigma, size=size)
print(pop)
print(pop.size)
print(pop.mean())
print(pop.std())

plt.figure(figsize=(20, 8))
plt.hist(pop, bins=1000)
plt.title("Normal Distribution", fontsize=20)
plt.xlabel("Screw Length", fontsize=15)
plt.ylabel("Absolute Frequency", fontsize=15)
plt.show()

print(stats.skew(pop))  # approx 0
print(stats.kurtosis(pop))  # excess kurtosis, approx 0
print(stats.kurtosis(pop, fisher=False))  # approx 3
print(stats.describe(pop))


''' Normal Distribution - Probability Density Function (pdf)
with scipy.stats '''

x = np.linspace(90, 110, 1000)
# print(x)

y = stats.norm.pdf(x, loc=mu, scale=sigma)
# print(y)

plt.figure(figsize=(20, 8))
plt.hist(pop, bins=1000, density=True)
plt.plot(x, y, linewidth=3, color="red")
plt.grid()
plt.title("Normal Distribution", fontsize=20)
plt.xlabel("Screw Length", fontsize=15)
plt.ylabel("pdf", fontsize=15)
plt.show()


''' Normal Distribution - Cumulative Distribution Function (cdf)
with scipy.stats '''

x = np.linspace(90, 110, 1000)
y = stats.norm.cdf(x, loc=mu, scale=sigma)

plt.figure(figsize=(20, 8))
plt.hist(pop, bins=1000, density=True, cumulative=True)
plt.plot(x, y, color="red", linewidth=3)
plt.grid()
plt.title("Normal Distribution", fontsize=20)
plt.xlabel("Screw Length", fontsize=15)
plt.ylabel("cdf", fontsize=15)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.show()
