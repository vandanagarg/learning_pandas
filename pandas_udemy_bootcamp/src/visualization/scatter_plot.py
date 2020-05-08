''' Scatterplots - 2D Scatterplots
Are used to detect relationships between 2 numerical features'''
import config_file  # noqa: F401
from utilities.dataframe_utilities import DataframeUtilities as dfu
import matplotlib.pyplot as plt


titanic = dfu.get_dataframe("titanic.csv")
print(titanic.head())
plt.style.use("seaborn")

# here we plot relationship between age and fare column - 2D plot
titanic.plot(kind="scatter", figsize=(15, 8), x="age", y="fare")
plt.show()  # each dot represents passenger

titanic.plot(kind="scatter", figsize=(15, 8), x="age", y="fare",
             c="red", marker="D", s=20)
plt.show()  # can change c= color, marker- shape of dots(o by default) & s=size

''' 3D scatter plot - by passing 3rd column name to parameter c we make 3D plot
where color difference in the scatters indicate the different values for the
scatters and values can be determined from the details given at RHS about the
3rd column, then in order to change color styles we can use colormap parameter
and there are various color styles available to pick from one '''

titanic.plot(kind="scatter", figsize=(15, 8), x="age", y="fare", c="survived",
             marker="x", s=20, colormap="viridis")
plt.show()  # just 2 colors as only 2 values


titanic.plot(kind="scatter", figsize=(15, 8), x="age", y="fare", c="pclass",
             marker="x", s=20, colormap="viridis")
plt.show()  # 3 different colors as only 3 values for column pclass
