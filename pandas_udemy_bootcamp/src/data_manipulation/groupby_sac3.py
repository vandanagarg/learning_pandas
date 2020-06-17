''' Generalizing split-apply-combine with apply()
Many a time if we want to find out some specific information as in this case
we need to find eldest m/f passengers onboard; we do this using a user
defined function and this can be used using apply() method.
So here we see how to use user defined functions using apply method
and find some specific information '''
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


# Titanic Dataset
titanic = dfu.get_dataframe("titanic.csv")
titanic = titanic[["survived", "pclass", "sex", "age", "fare"]]
titanic.info()

# using direct methods
print(titanic.groupby("sex").mean())
female_group = list(titanic.groupby("sex"))[0][1]
print(female_group)

print(female_group.mean())
print(female_group.mean().astype("float"))


# using user defined functions
def group_mean(group):
    return group.mean()


# gives the same results
print(group_mean(female_group))

print(titanic.groupby("sex").apply(group_mean))

# finding oldest passengers for both groups using apply() and
# user defined function five_oldest_survived()
print(titanic.nlargest(5, "age"))
# to find largest 5 records w.r.t. age column values


def five_oldest_survived(group):
    return group[group.survived == 1].nlargest(5, "age")


print(titanic.groupby("sex").apply(five_oldest_survived))
# new combined dataframe of oldest passangers who survived
