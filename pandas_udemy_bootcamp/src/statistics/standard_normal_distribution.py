''' The Standard Normal Distribution and Z-Scores '''
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


mu = 100
sigma = 2
size = 1000000

np.random.seed(123)
pop = np.random.normal(loc=mu, scale=sigma, size=size)
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


''' Probabilities and Z-Scores with scipy.stats '''

print("\n probabilities and Z-Scores")
# probability of having observations -1 sigma away from the mean
print(stats.norm.cdf(-1, loc=0, scale=1))
# opposite of probability of having observations -1 sigma away from the mean
print(1 - stats.norm.cdf(-1))
# probability of having observations 1 sigma away from the mean
print(stats.norm.cdf(1))
# opposite of probability of having observations 1 sigma away from the mean
print(1 - stats.norm.cdf(1))
# probability of having observations within  range (-1 sigma , 1 sigma)
print(stats.norm.cdf(1) - stats.norm.cdf(-1))
# probability of having observations -2 sigma away from the mean
print(stats.norm.cdf(-2))
# opposite of probability of having observations 2 sigma away from the mean
print(1 - stats.norm.cdf(2))
# probability of having observations within  range (-2 sigma , 2 sigma)
print(stats.norm.cdf(2) - stats.norm.cdf(-2))
# probability of having observations at the mean
print(stats.norm.cdf(0))  # 50%

print(pop)

minus_two_sigma = pop.mean() - 2 * pop.std()
print(minus_two_sigma)

print((pop < minus_two_sigma))  # boolean array
print((pop < minus_two_sigma).mean())  # approx 0, it's relative frequency
# also this value is equal to the theoretical value from `stats.norm.cdf(-2)`

# if we change the size to 105mm, calculating probability without z score
print(stats.norm.cdf(x=105, loc=pop.mean(), scale=pop.std()))
# probability of getting a screw of 105mm or more is less than 99.3%
# thus, probability of getting a screw of 105mm or more is 0.6%:
print(1 - stats.norm.cdf(x=105, loc=pop.mean(), scale=pop.std()))

# using z score
z = (105-pop.mean()) / pop.std()
print(z)  # the observation 105 is +2.49 sigma away from the mean

# calculating probability:
print(stats.norm.cdf(z))
# probability of getting a screw of 105mm or more is less than 99.37%

''' getting z values or observation scores from the given probabilites
ppf is inverse of cdf '''

# 50% probability will be equal to mid point
print(stats.norm.ppf(0.5, loc=0, scale=1))
# .5% probability/observations will -1.64std/sigma away from the mean
print(stats.norm.ppf(0.05))
# 95% probability/observations will 1.64std/sigma away from the mean
print(stats.norm.ppf(0.95))

# to find the screw length
# 5% of the observations will have a screw length of 96mm or less
print(stats.norm.ppf(loc=pop.mean(), scale=pop.std(), q=0.05))
# 5% of the observations will have a screw length of 103mm or more
print(stats.norm.ppf(loc=pop.mean(), scale=pop.std(), q=0.95))
