''' Data Visualization with Matplotlib
The plot() method '''
import config_file  # noqa: F401
from utilities.dataframe_utilities import DataframeUtilities as dfu
import matplotlib.pyplot as plt


titanic = dfu.get_dataframe("titanic.csv")
print(titanic.head())
titanic.info()
# to plot all numerical columns of titanic dataframe
titanic.plot()  # by default line plots
titanic.plot(subplots=True, figsize=(15, 12))  # larger figure size
# separate x- axis scale, seems more meaningful here
titanic.plot(subplots=True, figsize=(15, 12), sharex=False)
# separate x & y axis scale, seems less readable in this case
titanic.plot(subplots=True, figsize=(12, 8), sharex=False, sharey=True)
plt.show()

titanic.age.plot(figsize=(12, 8))
plt.show()

#  Customization of plots
titanic.age.plot(figsize=(12, 8), fontsize=13, c="r", linestyle="-")
# c for color, "r or red" for red color, linestyle can be --, : , -
plt.show()

print(plt.style.available)  # check the available styles
plt.style.use("classic")  # select classic style

# set the range
xticks = [x for x in range(0, 901, 50)]
print(xticks)

yticks = [y for y in range(0, 81, 5)]
print(yticks)

# set parameters
titanic.age.plot(figsize=(12, 8), fontsize=13, c="r", linestyle="-",
                 xlim=(0, 900), ylim=(0, 80), xticks=xticks, yticks=yticks,
                 rot=45)  # rot is to rotate xticks at a particular angle
# if we give values for xticks and yticks, we can omit xlim/ylim params
plt.title("Titanic - Ages", fontsize=15)
plt.legend(loc="best", fontsize=15)  # chooses best place for legend
plt.xlabel("Passenger No", fontsize=13)
plt.ylabel("Age", fontsize=13)
plt.grid()
plt.show()
