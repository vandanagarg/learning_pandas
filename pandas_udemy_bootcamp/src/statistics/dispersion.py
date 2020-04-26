''' Variability around the Central Tendency / Dispersion/ variance
Range, Minimum and Maximum '''
import numpy as np
from create_numpy_array import pop, sample


np.set_printoptions(precision=4, suppress=True)

print("\n population:")
print(pop.size)
print(pop.max())
print(pop.min())

# calculate range with method ptp()
range = pop.ptp()
print(range)

# another way to calculate range value
print(pop.max() - pop.min())

print("\n sample:")
print(sample.size)
print(np.max(sample))  # best stock return values 132%
print(np.min(sample))  # worst stock return values -12%
print(sample.ptp())  # calculate range


''' Variance and Standard Deviation '''
# __Population Variance__

print("\n Population Variance")
print(pop.var())
print(np.var(pop))

# __Sample Variance__

print("\n Sample Variance")
print(np.var(sample))
# This result is not close enough to pop var, which in ideal case
# sample var , pop var should be close enough
print(np.var(sample, ddof=1))
# another parameter ddof is use in order to get more reliable results,
# for population observations ddof=0 and for sample data ddof=1 always
print(sample.var(ddof=1))

# __Standard Deviation__

print("\n Population Standard Deviation")
print(np.sqrt(pop.var()))
print(pop.std())

print("\n Sample Standard Deviation")
print(np.sqrt(np.var(sample, ddof=1)))
print(np.sqrt(sample.var(ddof=1)))
print(sample.std(ddof=1))

# unit here for all is % so like mean is approx 20% and std is approx 30%
