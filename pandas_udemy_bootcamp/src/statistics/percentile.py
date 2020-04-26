''' Percentiles '''
import numpy as np
from create_numpy_array import pop


np.set_printoptions(precision=4, suppress=True)

''' percentile is a point where a part of observations is less and
other part is above a certain percentile value, for eg: median is a special
case of 50th% where half values are below & rest are above that point '''
print(np.percentile(pop, 50))
print(np.median(pop))

print(np.percentile(pop, 5))
# it means 5% in our population are below -14.450332744976718 (14%)
print(np.percentile(pop, 95))
# means in year 2017 5% of companies showed a return of more that 65%

# Passing multiple values, getting a range
print(np.percentile(pop, [25, 75]))
# Here 50% of the companies returns are between 4% and 35%
print(np.percentile(pop, [5, 95]))
print(np.percentile(pop, [2.5, 97.5]))
