''' Importing and Exporting Stock price data
from Yahoo Finance and Initial Inspection and
Visualization '''
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from create_dataframe import stocks_file


ticker = ["AAPL", "BA", "KO", "IBM", "DIS", "MSFT"]
# print(yf.download("AAPL", start="2010-01-01", end="2019-02-06"))
stocks_df = yf.download(ticker, start="2010-01-01", end="2019-02-06")
# multi level indexes
print(stocks_df.head())
print(stocks_df.tail())
stocks_df.info()
# stocks_df.to_csv("stocks.csv")

# importing multiindex df, also setting datetime index
stocks = pd.read_csv(stocks_file, header=[0, 1], index_col=[0],
                     parse_dates=[0])
print(stocks.head())

# to avoid confusions with multi index we can flatten the index
stocks.columns = stocks.columns.to_flat_index()
print(stocks.head())  # Now we have tuple indexes insted of multi levels

# to revert back to multi indexes instead of tuples
stocks.columns = pd.MultiIndex.from_tuples(stocks.columns)
print(stocks.head())  # Back to multi level indexes

# to swap and sort the index levels
print(stocks.swaplevel(axis=1).sort_index(axis=1))

# initial analysis
stocks.info()
print(stocks.describe())

# we will only need close column for calculations
close = stocks.loc[:, "Close"].copy()
print(close.head())  # daily closing prices

# good to visualize time series data
plt.style.use("seaborn")

close.plot(figsize=(15, 8), fontsize=13)
plt.legend(fontsize=13)
plt.show()
