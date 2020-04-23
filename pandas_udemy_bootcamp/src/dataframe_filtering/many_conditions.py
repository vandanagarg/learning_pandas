""" Filtering Dataframes with multiple conditions (AND/ OR) """
import config_file  # noqa: F401
from utilities import DataframeUtilities as dfu


titanic_df = dfu.get_dataframe("titanic.csv")
print(titanic_df.sex.head(10))
print(titanic_df.sex == "male")

male_series = (titanic_df.sex == "male")
print(male_series.head())

age_series = titanic_df.age > 14
print(age_series.head())

# combining both series/conditions
print("\n AND condition: ")
print((male_series & age_series).head())

male_survived = titanic_df.loc[male_series & age_series, [
    "survived", "pclass", "sex", "age"]]
print(male_survived.head())
male_survived.info()
print(male_survived.describe())
print(titanic_df.describe())
# it infers that w.r.t. total mean 38% only 17% adult male passengers survived

print("\n OR condition: ")

female_series = (titanic_df.sex == "female")
print(female_series.head())

female_child_age_series = titanic_df.age < 14
print(female_child_age_series.head())

print((female_series | female_child_age_series).head())
print(titanic_df.loc[female_series & female_child_age_series].head())
print(titanic_df.loc[female_series | female_child_age_series])

female_child_survived = titanic_df.loc[
    female_series | female_child_age_series,
    ["survived", "pclass", "sex", "age"]]
print(female_child_survived.head())
female_child_survived.info()
print(female_child_survived.describe())
print(titanic_df.describe())
# it infers that w.r.t. total mean 38%; 72% female/child survived
# Hence the hypothesis was the probability of survival of a female
# or child is more than that of a male and is true from results

print("\n Combining logical operations: ")
survival = (titanic_df["survived"] == 1)
print(survival.head())
psg_survived = titanic_df.loc[
    (female_series | female_child_age_series) & (survival),
    ["survived", "pclass", "sex", "age"]]
print(psg_survived.head())
