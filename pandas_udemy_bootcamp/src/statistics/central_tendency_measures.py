''' Measures of Central Tendency - Mean and Median '''
import numpy as np
from create_numpy_array import pop, sample


np.set_printoptions(precision=4, suppress=True)

# __Population Mean__ arithmetic mean/ average
print(pop)
print("\n Population Mean:")
print(pop.mean())
print(np.mean(pop))

# __Sample Mean__
print("\n")
print(sample)
print("\n Sample Mean:")
print(sample.mean())

# __Median__
print("\n Population Median:")
print(np.median(pop))
print("\n Sample Median:")
print(np.median(sample))
print("Median for even number of observations:")
sample.sort()  # first sort the list and take mean of 2 mid observations
print((sample[24] + sample[25]) / 2)


''' Measures of Central Tendency - Geometric Mean '''
print("\n Geometric Mean:")
# stock prices at the end of year 2015, 16, 17, 18
Price_2015_2018 = np.array([100, 107, 102, 110])

# for years 2015 to 2017 annual returns
''' annual return = current year price/ previous year price - 1 '''
ret = Price_2015_2018[1:] / Price_2015_2018[:-1] - 1
print("annual returns {}".format(ret))

mean = ret.mean()  # arithmetic mean
print("mean: {}".format(mean))

# to calculate price for year 2018 using mean()
print("\n final stock price for 2018 using mean:")
print(100 * (1 + mean)**3)

# find Geometric Mean- compound interest/growth rate
geo_mean = (1 + ret).prod()**(1/ret.size) - 1
print("geo_mean: {}".format(geo_mean))

# to calculate price for year 2018 using geo_mean()
print("\n final stock price for 2018 using geo_mean:")
print(100 * (1 + geo_mean)**3)

# another way to find geo_mean()
''' final price/ initial price to the power of one divided by number
of periods minus one '''
print("\n geo_mean:")
print((110 / 100)**(1/ret.size) - 1)
