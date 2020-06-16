''' split, apply, combine operations on dataframes
using groupby method '''
import matplotlib.pyplot as plt
from create_dataframes import summer
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


print(summer.head())
summer.info()

# We are interseted in details of top winning countries with
# highest medals in Olympic games
medals_per_country = summer.groupby("Country").Medal.count()
print(medals_per_country)

# most successfull 20 countries
medals_per_country = summer.groupby("Country").Medal.count().nlargest(n=20)
print(medals_per_country)

# creating a bar chart to visualize the results
plt.style.use("seaborn")

medals_per_country.plot(kind="bar", figsize=(14, 8), fontsize=14)
plt.xlabel("Country", fontsize=13)
plt.ylabel("No. of Labels", fontsize=13)
plt.title("Summer Olympic Games (Total Medals per Country)", fontsize=16)
plt.show()

# Titanic Dataset
titanic = dfu.get_dataframe("titanic.csv")
titanic.info()

# to check the total average fare and average fare for each passenger class
print(titanic.describe())
print(titanic.fare.mean())
print(titanic.groupby("pclass").fare.mean())

# to check the survival rate of passengers
print("\n survival:")
# tells no. of total passengers survived
print(titanic.survived.sum())
# tells rate of survival of passengers
print(titanic.survived.mean())

# rate of survival by sex, pclass
print(titanic.groupby("sex").survived.mean())
print(titanic.groupby("pclass").survived.mean())

# creating new column to segregate adults & child and check their survival rate
titanic["ad_chi"] = "adult"
titanic.loc[titanic.age < 18, "ad_chi"] = "child"
print(titanic.ad_chi.value_counts())
print(titanic.groupby("ad_chi").survived.mean())
# adding more keys
print(titanic.groupby(["sex", "ad_chi"]).survived.mean())
print(titanic.groupby(["sex", "ad_chi"]).survived.count())
# sorting
print(titanic.groupby(["sex", "ad_chi"]).survived.mean(
                     ).sort_values(ascending=False))

# visualizing results
w_and_c_first = titanic.groupby(["sex", "ad_chi"]).survived.mean(
                     ).sort_values(ascending=False)
w_and_c_first.plot(kind="bar", figsize=(14, 8), fontsize=14)
# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)
plt.xlabel("Groups", fontsize=13)
plt.ylabel("Survival rate", fontsize=13)
plt.title("Titanic Survival Rate by Sex/Age Groups", fontsize=16)
plt.show()

# performing a series of operations
print(titanic.groupby("sex")[["survived", "pclass", "age", "fare"]
                             ].agg(["sum", "mean"]))
