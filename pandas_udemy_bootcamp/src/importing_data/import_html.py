''' Importing data from the web with pd.read_html() '''
import pandas as pd


url = "https://en.wikipedia.org/wiki/1976_Summer_Olympics_medal_table"
print(url)

df_url = pd.read_html(url)  # list of 2 dataframes
print(df_url)
print(type(df_url))  # <class 'list'>
print(len(df_url))  # 3
print(df_url[0])
print(df_url[1])
print(df_url[2])

wik_1976 = df_url[0]
print(wik_1976.head())
print(wik_1976.tail())
wik_1976.info()
