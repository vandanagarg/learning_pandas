''' Explanatory Data Analysis
How additional features influence /Which factors influence house prices?
'''
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimp
import seaborn as sns
from data_cleaning import housing_df
from create_dataframe import PATH


# till now we have cleaned the data and made new features,
# now we must check how this effects house prices and best way to
# observe it is making diffrent plots
housing_df.median_house_value.hist(bins=100, figsize=(12, 8))
plt.show()

# to find correlation of median_house_value with other factors, towards
# +1 we have positive correlation and at 0 almost no influence and -1
# indicates a negative correlation
print(housing_df.corr().median_house_value.sort_values(ascending=False))

# for median income column
housing_df.median_income.hist(bins=100, figsize=(12, 8))
plt.show()

# regression plot - o/p is a positive linear relationship
sns.set(font_scale=1.5)
sns.jointplot(data=housing_df, x="median_income", y="median_house_value",
              kind="reg", height=10)
plt.show()

# kernel density plot - o/p is a positive linear relationship
sns.jointplot(data=housing_df, x="median_income", y="median_house_value",
              kind="kde", height=10)
plt.show()

# scatter plot, using color map for median_house_value column
housing_df.plot(kind="scatter", x="longitude", y="latitude",
                s=housing_df.population/100, label="Population",
                figsize=(15, 10), c="median_house_value",
                cmap="coolwarm", colorbar=True,
                alpha=0.4, fontsize=15, sharex=False)
plt.ylabel("Latitude", fontsize=14)
plt.xlabel("Longitude", fontsize=14)
plt.legend(fontsize=16)
plt.show()
# each dot represents a district and darker the dot(red) represents
# higher prices and lighter the dot color its cheaper prices and the plot
# looks like the shape of california state

# To see the california map as a image beneath the plot
image_name = PATH + "california.png"
california_img = mpimp.imread(image_name)
print(california_img)  # reads file into an array
# image represented as a matrix with numbers

# to plot the image
plt.figure(figsize=(15, 10))
plt.imshow(california_img)
plt.show()

# but this image doesn't contain/show any longitude/latitude's
# change the axis labels using extent to include longitude/latitude
plt.imshow(california_img, extent=[-124.55, -113.80, 32.45, 42.05])
plt.show()

# combining map and datapoints
housing_df.plot(kind="scatter", x="longitude", y="latitude",
                s=housing_df.population/100, label="Population",
                figsize=(15, 10), c="median_house_value",
                cmap="coolwarm", colorbar=True,
                alpha=0.4, fontsize=15, sharex=False)

plt.imshow(california_img, extent=[-124.55, -113.80, 32.45, 42.05],
           alpha=0.5, cmap=plt.get_cmap("jet"))

plt.ylabel("Latitude", fontsize=14)
plt.xlabel("Longitude", fontsize=14)
plt.legend(fontsize=16)
plt.show()

# categorical column "ocean_proximity"
prox = housing_df.ocean_proximity.unique()
print(prox)

# to filter for each category and plot on the same graph individually

# 1. plot for "INLAND"
df_loc = housing_df[housing_df.ocean_proximity == prox[3]].copy()
df_loc.plot(kind="scatter", x="longitude", y="latitude",
            s=df_loc.population/100, label="Population",
            figsize=(15, 10), c="median_house_value",
            cmap="coolwarm", colorbar=True,
            alpha=0.4, fontsize=15, sharex=False)

plt.imshow(california_img, extent=[-124.55, -113.80, 32.45, 42.05],
           alpha=0.5, cmap=plt.get_cmap("jet"))

plt.ylabel("Latitude", fontsize=14)
plt.xlabel("Longitude", fontsize=14)
plt.legend(fontsize=16)
plt.show()

# 2. plot for "<1H OCEAN"
df_loc2 = housing_df[housing_df.ocean_proximity == prox[2]].copy()
df_loc2.plot(kind="scatter", x="longitude", y="latitude",
             s=df_loc2.population/100, label="Population",
             figsize=(15, 10), c="median_house_value",
             cmap="coolwarm", colorbar=True,
             alpha=0.4, fontsize=15, sharex=False)

plt.imshow(california_img, extent=[-124.55, -113.80, 32.45, 42.05],
           alpha=0.5, cmap=plt.get_cmap("jet"))

plt.ylabel("Latitude", fontsize=14)
plt.xlabel("Longitude", fontsize=14)
plt.legend(fontsize=16)
plt.show()
# hence these graph shows location does matter for house prices

''' For latitude and longitude we clearly don't have a linear relationship
since the prices are not constant and vary a lot, but with the non linear
ML models like random forest regressor we should be able to find relationship
between location and house prices '''

# next income should be the most important feature to forecast house prices
housing_df.median_income.hist(bins=50, figsize=(15, 10))
plt.title("Median Income")
plt.show()

# Here we can convert numerical column into categorical column by
# converting/dividing it into 5 groups/bins - binning
print(pd.qcut(housing_df.median_income, q=[0, 0.25, 0.5, 0.75, 0.95, 1]))

housing_df["income_cat"] = pd.qcut(housing_df.median_income, q=[
                            0, 0.25, 0.5, 0.75, 0.95, 1],
                            labels=["Low", "Below_Average",
                                    "Above_Average", "High", "Very High"])
print(housing_df.income_cat)

# relative counts
print(housing_df.income_cat.value_counts(normalize=True))

# Seaborne bar plots
plt.figure(figsize=(12, 8))

# median income and ocean proximity
sns.set(font_scale=1.5, palette="viridis")
sns.countplot(data=housing_df, x="income_cat", hue="ocean_proximity")
plt.legend(loc=1)
plt.show()

# income_cat and median_house_value, so lesser the income lesser
# the house's value and vice versa
sns.set(font_scale=1.5)
sns.barplot(data=housing_df, x='income_cat',
            y='median_house_value', dodge=True)
plt.show()

# ocean_proximity and median_house_value
sns.barplot(data=housing_df, x="ocean_proximity",
            y="median_house_value", dodge=True)
plt.show()

# grouping data
matrix = housing_df.groupby(["income_cat", "ocean_proximity"]
                            ).median_house_value.mean().unstack(
                            ).drop(columns=["ISLAND"])
matrix.astype("int")

# create a heat map
sns.set(font_scale=1.4)
sns.heatmap(matrix.astype("int"), cmap="Reds", annot=True, fmt="d",
            vmin=90000, vmax=470000)
plt.show()
''' So here we have clear idea that for high incomes, the house value
is more and is near to ocean while for low incomes the value of house
is less and is away from ocean i.e. is in inland '''
