import pandas as pd
import numpy as np


url1 = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv"  # noqa: E501
url2 = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv"  # noqa: E501
cars1 = pd.read_csv(url1, header=0)
cars2 = pd.read_csv(url2, header=0)
# print(cars2)

cars1.dropna(inplace=True, axis=1)
# cars1 = cars1.loc[:, "mpg":"car"]
cars1.info()
cars2.info()

print(cars1.shape[0])
print(cars2.shape[0])

cars = cars1.append(cars2)
print(cars)
print(cars.shape[0])

nr_owners = np.random.randint(15000, high=73001, size=398, dtype='l')
print(nr_owners)

cars['owners'] = nr_owners
print(cars.tail())
