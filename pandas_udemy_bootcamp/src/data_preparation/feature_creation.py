''' Data preparation and Feature creation '''
from create_dataframes import titanic, sales


titanic.info()
titanic.age.fillna(titanic.age.mean(), inplace=True)
print(titanic.head(10))

''' Creating new data/ additional features using existing
columns of our dataframe and using arithmetic operations like
Add/Sub/Mul/Div on columns '''

# addition of columns: to check for any relatives onboard
# 1. element wise operation
print(titanic.sibsp + titanic.parch)

# 2. method add() # better performance, recommended way
print(titanic.sibsp.add(titanic.parch))
titanic["no_relative"] = titanic.sibsp.add(titanic.parch)
print(titanic.head())

# sales dataset
print(sales)
# lets add sales of monday and thursday
# + operator
print(sales.Mon + sales.Thu)  # NaN value is a problem

# add() method  # advantage handles missing values
print(sales.Mon.add(sales.Thu))  # NaN value can be handled
print(sales.Mon.add(sales.Thu, fill_value=0))  # parameter fill_value

# multiplication of columns:
# create a new column
sales["perc_bonus"] = [0.12, 0.15, 0.10, 0.20]
print(sales)

# to calculate thursday's bonus amount(15% on 87, 10% on 8)
# 1. * operator
print(sales.Thu * sales.perc_bonus)  # NaN value is a problem

# 2. mul() method  # advantage handles missing values
print(sales.Thu.mul(sales.perc_bonus, fill_value=0))

# find weekly bonus for all salesman
# sum() pandas method handles missing values no need to specify again
print(sales.iloc[:, :-1].sum(axis=1).mul(sales.perc_bonus))

sales["Weekly_Bonus"] = sales.iloc[:, :-1].sum(axis=1).mul(sales.perc_bonus)
print(sales)

''' Add/Sub/Mul/Div on columns with Scaler Value '''
# to calculate birth year of passengars, 1912(titanic disaster year)
# 1. using - operator
print(1912 - titanic.age)

# 2. using sub() method  # missing values are handled
titanic["YOB"] = titanic.age.sub(1912).mul(-1)
print(titanic.head())

# change the US dollar fare column to euro's fare
fx_rate = 1.1
titanic["EUR_fare"] = titanic.fare.div(fx_rate)
print(titanic.head())

# dropping unwanted columns
titanic.drop(columns=["sibsp", "parch", "deck", "YOB", "EUR_fare"
                      ], inplace=True)
print(titanic.head())

# sales dataset
# calculating actual daily sale by substracting the fixed_cost
fixed_cost = 5
print(sales.iloc[:, :-2].sub(fixed_cost, fill_value=0))

# to check for daily bonus of salesmans
perc_bonus = 0.1
print(sales.iloc[:, :-2].mul(perc_bonus, fill_value=0))

''' To perform a more complex calculation: to find bonus
on the basis of lot_size on each 10 size the bonus percentage
increases to 1.25, thus to perform such calculations we use
floordiv() method followed by chaining other methods '''
lot_size = 10
bonus_per_lot = 1.25

# find total lot sizes and then multiply with the bonus amount
print(sales.iloc[:, :-2].floordiv(lot_size, fill_value=0).mul(bonus_per_lot))

# to find total weekly bonus sum up all salesman's bonus
print(sales.iloc[:, :-2].floordiv(lot_size, fill_value=0
                                  ).mul(bonus_per_lot).sum(axis=1))
