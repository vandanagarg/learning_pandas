import pandas as pd


url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv"  # noqa: E501
drinks = pd.read_csv(url)
# print(drinks[drinks.continent.isna()])

# mean_serving = drinks.beer_servings.mean()
# print(drinks[drinks.beer_servings > mean_serving]
df = drinks.groupby("continent")
print(df.beer_servings.mean())

print(df.wine_servings.describe())

print(df.mean())
print(df.median())

print(df.spirit_servings.describe())
print(df.spirit_servings.agg(["min", "max", "mean"]))
