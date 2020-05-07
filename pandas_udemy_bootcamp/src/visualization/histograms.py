''' Histograms - to visualize frequency distributions in numerical columns '''
import config_file  # noqa: F401
from utilities.dataframe_utilities import DataframeUtilities as dfu
import matplotlib.pyplot as plt


titanic = dfu.get_dataframe("titanic.csv")
plt.style.use("seaborn")

# for checking frequency distributions, we can even set bins/intervals
print(titanic.age.value_counts())
print(titanic.age.value_counts(bins=10))

titanic.age.plot(kind="line", figsize=(12, 8), fontsize=15)  # line plot
plt.show()

titanic.age.plot(kind="hist", figsize=(12, 8), fontsize=15)  # default 10 bins
plt.show()

# for absolute quantities
titanic.age.plot(kind="hist", figsize=(12, 8), fontsize=15, bins=80)
plt.show()

# for relative quantities set density=True
titanic.age.plot(kind="hist", figsize=(12, 8), fontsize=15, bins=80,
                 density=True)
# by default density & bins parameter is not visible but we can use them
plt.show()
''' here in plot function we can see parameters mostly related to line plots
and rest parameters can be applied but are not visible;
hence it is better to use some other methods to plot histograms, which has
all other useful/needed parameters '''

# using hist() method
titanic.age.hist(figsize=(12, 8), bins=80, xlabelsize=15, ylabelsize=15)
plt.show()

titanic.age.hist(figsize=(12, 8), bins=80, xlabelsize=15, ylabelsize=15,
                 cumulative=True)  # absolute cumulative frequencies/histogram
plt.show()

''' here applying hist() function directly can't handle missing values and
gives error so we must drop missing values first to plot the graph; also;
plot() method directly can handle missing values and no need to explicitly drop
them but for all missing values we get breaks in our graphs be it any graph '''
plt.figure(figsize=(12, 8))
# plots relative & cumulative histogram values add up 1 (normalized quantities)
plt.hist(titanic.age.dropna(), bins=80, density=True, cumulative=True)
plt.show()
