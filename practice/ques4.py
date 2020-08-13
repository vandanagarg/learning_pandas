import pandas as pd


url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"  # noqa: E501
chipo = pd.read_csv(url, sep='\t', header=0)
print(chipo.head())

chipo.item_price = chipo.item_price.str.replace("$", "").astype("float")
print(chipo.item_price.dtype)

item_price_df = chipo[["item_name", "item_price"]]
# print(item_price_df)
print(item_price_df.sort_values(by="item_name"))

print(item_price_df.sort_values(by="item_price", ascending=False))
print(item_price_df.sort_values(by="item_price").item_price.value_counts())
print(max(item_price_df.item_price))
print(min(item_price_df.item_price))

print(chipo.loc[chipo.item_price == 44.25])
print(chipo.loc[chipo.item_price == max(chipo.item_price)])
# print(chipo.loc[chipo.item_price == 17.50])


# print(chipo.loc[chipo.item_name == "Veggie Salad Bowl"].count())

c = chipo.groupby("item_name")
c = c.quantity.sum()
# print(c)
print(c.loc["Veggie Salad Bowl"])

print(chipo[(chipo.item_name == "Canned Soda") & (chipo.quantity > 1)].count())
print(chipo[(chipo.item_name == "Canned Soda") & (chipo.quantity > 1)].shape)
print(len(chipo[(chipo.item_name == "Canned Soda") & (chipo.quantity > 1)]))
