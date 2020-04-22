''' Descriptive Statistics
Population vs. Sample (Price Returns for S&P 500 Companies in 2017)

The __S&P 500__, or just the S&P, is a __stock market index__ that
measures the stock performance of __500 large companies__ listed on
stock exchanges in the United States. It is one of the most commonly
followed equity indices, and many consider it to be one of the best
representations of the U.S. stock market.
The S&P 500 is a __capitalization-weighted index__ and the performance
of the __10 largest companies__ in the index account for __21.8% of the
performance__ of the index. '''
import numpy as np
from create_numpy_array import pop, sample


# What is the equally weighted return in 2017?
# Population: 2017 Price Return for all 500 Companies
print(pop)
print(pop.size)

# Sample: 2017 Price Return for 50 Companies (randomly selected)
print(sample)
print(sample.size)

# to check if each sample is in population data as well
for i in sample:
    print(i in pop)

print(np.isin(sample, pop))
