""" Case Study Numpy vs. Python Standard Library """
import numpy as np
import random


# using vectorization and method-chaining
np.random.seed(122)
print((np.random.randint(1, 11, 100) == 1).sum().mean())

np.random.seed(122)
print((
    np.random.randint(1, 11, 1000000).reshape(10000, 100) == 1
    ).sum(axis=1).mean())

# get_ipython().run_line_magic('timeit', '(np.random.randint(1,11,100*10000
# ).reshape(10000,100) == 1).sum(axis = 1).mean()')

# using nested loops, if statements and lists


def simulation():
    results = []
    for _ in range(10000):
        l1 = []
        for _ in range(100):
            if random.randint(1, 10) == 1:
                l1.append(True)
            else:
                l1.append(False)
        results.append(sum(l1))
    return (sum(results) / len(results))


print(simulation())

# get_ipython().run_line_magic('timeit', 'simulation()')
