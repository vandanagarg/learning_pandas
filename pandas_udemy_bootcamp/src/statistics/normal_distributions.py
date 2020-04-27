''' Creating a normally distributed Random Variable '''
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


''' The Standard Normal Distribution and Z-Scores '''

mu = pop.mean()
sigma = pop.std()

print(mu)
print(sigma)
print(pop[0])
print((pop[0] - mu))  # absolute distance
print((pop[0] - mu) / sigma)
print(pop[1])
print((pop[1] - mu) / sigma)

print("\n z values:")
print((pop - mu) / sigma)  # z values - deviation from mean
z = stats.zscore(pop)
print(z)

print(round(z.mean(), 4))  # mean should be zero
print(z.std())  # std should be one
print(stats.skew(z))  # skew should be zero
print(stats.kurtosis(z))  # excess kurtosis should be zero

x = np.linspace(-4, 4, 1000)

y = stats.norm.pdf(x, loc=0, scale=1)

plt.figure(figsize=(20, 8))
plt.hist(z, bins=1000, density=True)
plt.grid()
plt.plot(x, y, linewidth=3, color="red")
plt.xticks(np.arange(-4, 5, 1),
           labels=["-4σ=-4", "-3σ=-3", "-2σ=-2", "-1σ=-1", "mu=0", "1σ=1",
           "2σ=2", "3σ=3", "4σ=4"],
           fontsize=15)
plt.title("Standard Normal Distribution", fontsize=20)
plt.ylabel("pdf", fontsize=15)
plt.show()

y = stats.norm.cdf(x)

plt.figure(figsize=(20, 8))
plt.hist(z, bins=1000, density=True, cumulative=True)
plt.plot(x, y, color="red", linewidth=3)
plt.grid()
plt.xticks(np.arange(-4, 5, 1),
           labels=["-4σ=-4", "-3σ=-3", "-2σ=-2", "-1σ=-1", "mu=0", "1σ=1",
           "2σ=2", "3σ=3", "4σ=4"],
           fontsize=15)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.title("Standard Normal Distribution", fontsize=20)
plt.ylabel("cdf", fontsize=15)
plt.show()
