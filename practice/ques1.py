''' question1 '''
import pandas as pd
import numpy as np
from file_utilities import FILE_PATH


chipo = pd.read_csv(FILE_PATH + "dataset_chipotle.tsv",
                    delimiter="\t", header=0)
print(chipo.head(10))
print(chipo.shape[0])
chipo.info()
print(chipo.count())

print(chipo.shape[1])
print(chipo.columns)

print(chipo.index)

print(chipo.item_name.value_counts().nlargest(1))
c = chipo.groupby("item_name")
print(c.sum())
print(c.quantity.sum().sort_values(ascending=False).nlargest(1))

print(chipo.choice_description.value_counts().nlargest(1))
d = chipo.groupby("choice_description")
print(d.quantity.sum().sort_values(ascending=False).nlargest(1))

print(chipo.quantity.sum())

print(chipo.item_price.dtype)
# print(chipo.item_price[0])
# print(round(chipo.item_price.str.replace("$", "").astype("float").
#             describe(), 2).sum())
# dollarizer = lambda x: float(x[1:])
chipo.item_price = chipo.item_price.apply(lambda x: float(x[1:]))
print(chipo.item_price.dtype)

revenue = (chipo['quantity'] * chipo['item_price']).sum()
print('Revenue was: $' + str(np.round(revenue, 2)))

print(chipo.order_id.value_counts().count())
t_orders = chipo.order_id.nunique()

print(revenue/t_orders)

chipo['revenue'] = chipo['quantity'] * chipo['item_price']
order_grouped = chipo.groupby(by=['order_id']).sum()
# print(order_grouped.mean())
print(order_grouped.mean()['revenue'])

print(chipo.item_name.nunique())
