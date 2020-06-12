''' Comparing two DataFrames / Identify Differences
5 ways how to identify / highlight differences between
two versions of the same Dataset over time '''
import pandas as pd
import numpy as np
from create_dataframes import sales


# updating NA value in sales
sales.iloc[0, 3] = 9
print(sales)
# Sales Dataframe (two elements are changed from Day1 to Day2)
sales2 = sales.copy()
# changing 2 elements in sales2
sales2.iloc[0, 1] = 100
sales2.iloc[3, 2] = 200
print(sales2)

# solution 1:
print(sales == sales2)  # prints false for changed elements

# solution 2:
# prints old values for changed elements/ NaN for unchanged elements
print(sales.where(~(sales == sales2)))

# solution 3:
# prints new values for changed elements/ NaN for unchanged elements
print(sales2.where(~(sales == sales2)))

# solution 4:
# concat both dataframes
sales_comp = pd.concat([sales, sales2], axis=1, keys=["Day1", "Day2"])
print(sales_comp)


# Highlighting differences
def highlight_diff(data, color='yellow'):
    attr = 'background-color: {}'.format(color)
    other = data.xs('Day1', axis='columns', level=-2)
    return pd.DataFrame(np.where(data.ne(other, level=1), attr, ''),
                        index=data.index, columns=data.columns)


df = sales_comp.style.apply(highlight_diff, axis=None)
print(df)


# solution 5:
# showing changes side to side
def diff_pd(df1, df2):
    """Identify differences between two pandas DataFrames"""
    assert (df1.columns == df2.columns).all(), \
        "DataFrame column names are different"
    if any(df1.dtypes != df2.dtypes):
        "Data Types are different, trying to convert"
        df2 = df2.astype(df1.dtypes)
    if df1.equals(df2):
        return None
    else:
        # need to account for np.nan != np.nan returning True
        diff_mask = (df1 != df2) & ~(df1.isnull() & df2.isnull())
        ne_stacked = diff_mask.stack()
        changed = ne_stacked[ne_stacked]
        changed.index.names = ['id', 'col']
        difference_locations = np.where(diff_mask)
        changed_from = df1.values[difference_locations]
        changed_to = df2.values[difference_locations]
        return pd.DataFrame({'from': changed_from, 'to': changed_to},
                            index=changed.index)


print(diff_pd(sales, sales2))
