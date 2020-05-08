''' Confidence Intervals
The ABC Company produces screws. The length of the screws follows
a Normal Distribution with mean = 100(millimeters) and standard deviation
2 (millimeters). Determine the Confidence Interval around the mean where
90% of all observations can be found'''
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


conf = 0.90

tails = (1-conf) / 2
print(tails)  # 5% leftover tails

left = stats.norm.ppf(tails)
print(left)  # left boundary

right = stats.norm.ppf(1-tails)
print(right)  # right boundary

print(stats.norm.interval(conf))  # confidence range
# o/p is a tuple
left, right = stats.norm.interval(conf)  # unpacking tuple
print(left)
print(right)

x = np.linspace(-5, 5, 1000)

y = stats.norm.pdf(x)

plt.figure(figsize=(20, 8))
plt.plot(x, y, color="black", linewidth=2)
plt.fill_between(x, y, where=((x > right) | (x < left)),
                 color="blue", alpha=0.2)
plt.fill_between(x, y, where=((x < right) & (x > left)),
                 color="red", alpha=0.2)
plt.grid()
plt.annotate("5%", xy=(1.75, 0.01), fontsize=20)
plt.annotate("5%", xy=(-2.25, 0.01), fontsize=20)
plt.annotate("90%", xy=(-0.6, 0.2), fontsize=40)
plt.annotate("-1.645σ", xy=(-1.645, -0.015), fontsize=10)
plt.annotate("1.645σ", xy=(1.645, -0.015), fontsize=10)
plt.xticks(np.arange(-4, 5, 1),
           labels=["-4σ=-4", "-3σ=-3", "-2σ=-2", "-1σ=-1", "mu=0",
                   "1σ=1", "2σ=2", "3σ=3", "4σ=4"],
           fontsize=10)
plt.title("Standard Normal Distribution", fontsize=20)
plt.ylabel("pdf", fontsize=15)
plt.show()

x = np.linspace(-5, 5, 1000)

y = stats.norm.cdf(x)

plt.figure(figsize=(12, 8))
plt.margins(x=0, y=0)
plt.plot(x, y, color="black", linewidth=2)
plt.vlines(x=[left, right], ymin=0, ymax=[
              stats.norm.cdf(left), stats.norm.cdf(right)], linestyle="--")
plt.hlines(y=[stats.norm.cdf(left), stats.norm.cdf(right)], xmin=-5, xmax=[
              left, right], linestyle="--")
plt.grid()
plt.xticks(np.arange(-4, 5, 1),
           labels=["-4σ=-4", "-3σ=-3", "-2σ=-2", "-1σ=-1", "mu=0", "1σ=1",
                   "2σ=2", "3σ=3", "4σ=4"],
           fontsize=15)
plt.yticks(np.arange(0, 1.1, 0.05), fontsize=10)
plt.annotate("-1.645σ", xy=(-1.60, 0.015), fontsize=10)
plt.annotate("1.645σ", xy=(1.7, 0.015), fontsize=10)
plt.title("Standard Normal Distribution", fontsize=20)
plt.ylabel("cdf", fontsize=15)
plt.show()

# values in mm(millimeters) - 90% of screws have a length between this interval
print(stats.norm.interval(conf, loc=100, scale=2))

mu = 100
sigma = 2
size = 1000000

np.random.seed(123)
pop = np.random.normal(loc=mu, scale=sigma, size=size)
print(pop)

# actual values using percentile method to find 5th% and 95th%
left, right = np.percentile(pop, [5, 95])
print(left)
print(right)
# o/p results are similar to stats.norm.interval(conf, loc=100, scale=2)
# hence we have a normally distributed population with mean 100 and std 2
