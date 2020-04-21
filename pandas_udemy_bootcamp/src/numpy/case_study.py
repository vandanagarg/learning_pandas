""" Case Study Numpy vs. Python Standard Library """
import numpy as np
import random
import timeit


# using vectorization and method-chaining
np.random.seed(122)
print((np.random.randint(1, 11, 100) == 1).sum().mean())

np.random.seed(122)
print((
    np.random.randint(1, 11, 1000000).reshape(10000, 100) == 1
    ).sum(axis=1).mean())

print("\n testing performance for vectorization and method-chaining: ")

print(timeit.timeit('''
import numpy as np
import random
(np.random.randint(1,11,100*10000
).reshape(10000,100) == 1).sum(axis = 1).mean()
''', number=1))


# using nested loops, if statements and lists

print("\n testing performance for nested loops, if statements and lists: ")


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


print("\n simulation result is: " + str(simulation()))

print(timeit.timeit('simulation()', setup="from __main__ import simulation",
      number=1))
