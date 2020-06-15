''' Splitting with many keys '''
from create_dataframes import summer


summer.info()
print(summer.Country.nunique())
# this grouping for 147 countries can either be done by using
# loc operator (complex and time taking) or by groupby (easier way)

# using groupy operation
print("\n grouping on 1 key:")
split1 = summer.groupby("Country")
l_c = list(split1)
# print(l_c)
print(len(l_c))  # 147
print(l_c[100])
print(l_c[100][1])

print("\n grouping on 2 keys:")
split2 = summer.groupby(["Country", "Gender"])
l2 = list(split2)
# print(l2)
# should be approx double since male/female 2 group to division in ideal case
print(len(l2))  # 236
print(l2[100: 102])
print(type(l2[100]))  # <class 'tuple'>
print(l2[100][0])  # ('IOP', 'Men')
print(type(l2[100][0]))  # <class 'tuple'>
print(l2[100][1])
print(type(l2[100][1]))  # <class 'pandas.core.frame.DataFrame'>

print("\n grouping on 3 keys:")
split3 = summer.groupby(["Country", "Gender", "Year"])
l3 = list(split3)
# print(l3)
print(len(l3))  # 1702
print(l3[100: 102])
print(type(l3[100]))  # <class 'tuple'>
print(l3[100][0])  # ('AUT', 'Men', 1980)
print(type(l3[100][0]))  # <class 'tuple'>
print(l3[100][1])
print(type(l3[100][1]))  # <class 'pandas.core.frame.DataFrame'>
