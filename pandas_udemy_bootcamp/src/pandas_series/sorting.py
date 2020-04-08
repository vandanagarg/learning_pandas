""" sorting pandas series, one way is using sort_values() method,
the other way is using indexes"""
import pandas as pd


dic = {1: 10, 3: 25, 2: 76, 4: 6, 5: 36, 6: 0, 7: None}
print(dic)

sales = pd.Series(dic)
print(sales)

print(sales.sort_index())  # ascending True by default
print(sales.sort_index(ascending=False))
sales.sort_index(inplace=True)
print(sales)
# Now this is not appending actual sales series and is not
# a in memory operation, to do so set inplace parameter True

print(sales.sort_values())  # sorts values ascending not indexes
print(sales)
sales.sort_values(inplace=True)  # ascending True by default
print(sales)

# changing default parameters
print(sales.sort_values(ascending=False, na_position="last", inplace=False))
print(sales)
print("Check ignore_index")
sales.sort_values(ascending=False, na_position="first", inplace=True)
print(sales)
sales.sort_values(
    ascending=False, na_position="first", inplace=True, ignore_index=True
    )  # It ignores  original indexes and replaces them with new serial indexes
print(sales)

""" Thus numerical indexes are sorted high to low and object/string
indexes are sorted alphabetically"""
