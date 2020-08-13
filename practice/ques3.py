import pandas as pd
from file_utilities import FILE_PATH


file_name = FILE_PATH + "dataset_food.tsv"

food = pd.read_csv(file_name, sep='\t', header=0, low_memory=False)
print(food.head())
print(food.shape[0])
print(food.shape[1])
print(food.columns)
print(food.columns[104])
print(food["-glucose_100g"].dtype)
print(food.index)

print(food.product_name.iloc[18])
food.values[18][7]
