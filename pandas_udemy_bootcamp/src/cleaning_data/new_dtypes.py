''' Pandas Version 1.0: NEW Dtypes and pd.NA
Pandas is getting more pythonic with new datatypes and a new
placeholder for missing values pd.NA over time new datatypes
will be considered as standard in pandas
Earlier we had a combined object datatype for strings, text or
mixed datatypes but now this has been improvised to represent
string datatype and so on, also missing values are represented as
<NA> instead of NaN values '''
from create_dataframes import titanic
import pandas as pd

print(titanic.head())
#   Survived  Class  Gender   Age  SipSp  ParCh      Fare Emb Deck
# 0        0      3    male  22.0      1      0     $7.25   S  NaN
titanic.info()
'''
Data columns (total 9 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   Survived  894 non-null    object
 1   Class     894 non-null    int64
 2   Gender    894 non-null    object
 3   Age       758 non-null    object
 4   SipSp     894 non-null    int64
 5   ParCh     894 non-null    int64
 6   Fare      894 non-null    object
 7   Emb       892 non-null    object
 8   Deck      203 non-null    object
dtypes: int64(3), object(6)
memory usage: 63.0+ KB
'''

# we need to convert older datatypes to new one using convert_dtypes()
titanic = titanic.convert_dtypes()
print(titanic.head())
#   Survived  Class  Gender   Age  SipSp  ParCh      Fare Emb  Deck
# 0        0      3    male  22.0      1      0     $7.25   S  <NA>

titanic.info()
'''
#   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   Survived  894 non-null    string
 1   Class     894 non-null    Int64
 2   Gender    894 non-null    string
 3   Age       758 non-null    string
 4   SipSp     894 non-null    Int64
 5   ParCh     894 non-null    Int64
 6   Fare      894 non-null    string
 7   Emb       892 non-null    string
 8   Deck      203 non-null    string
dtypes: Int64(3), string(6)
memory usage: 65.6 KB
'''
print(titanic.iloc[0, -1])  # <NA>
print(type(titanic.iloc[0, -1]))
# <class 'pandas._libs.missing.NAType'>
print(pd.NA)  # <NA>
