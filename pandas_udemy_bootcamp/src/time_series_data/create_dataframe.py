''' Time Series dataframes '''
import pandas as pd
import config_file  # noqa: F401
from utilities.file_utilities import FileUtilities


PATH = FileUtilities.get_abs_path("../../Course_Materials_Part5/Video_Lecture_NBs/")  # noqa: E501
temp_file = PATH + "temp.csv"
stocks_file = PATH + "stocks.csv"

temp = pd.read_csv(temp_file)
# print(temp)

stocks = pd.read_csv(stocks_file)
stocks = pd.read_csv(stocks_file, header=[0, 1], index_col=[0],
                     parse_dates=[0])
# print(stocks)

# daily closing prices
close = stocks.loc[:, "Close"].copy()
# print(close.head())
