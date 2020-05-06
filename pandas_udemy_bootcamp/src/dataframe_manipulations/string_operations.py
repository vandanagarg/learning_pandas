''' String Operations in Pandas '''
import config_file  # noqa: F401
from utilities.dataframe_utilities import DataframeUtilities as dfu


summer = dfu.get_dataframe("summer.csv")
hello = "Hello World"
print(hello)

print(type("Hello World"))
print(len(hello))
print(hello.lower())
print(hello.upper())
print(hello.title())
print(hello.split(" "))
print(hello.replace("Hello", "Hi"))

print("\n string operations on dataframes:")
names = summer.loc[:9, "Athlete"].copy()  # creating a copy
print(names)
print(names.dtypes)  # object datatype
print(names[0])  # 1st element
print(type(names[0]))  # str type

print("\n vectorized string operations using .str :")
# print(names.lower())  # gives error
# we must use .str to perform any string operations on dataframes/series
print(names.str.lower())
print(names.str.title())

# n parameter for number of splits, by default for all occurrences
# n=1 denotes to splits only at the first whitespace/occurrence
print(summer.Event.str.split(" ", n=1))
# n=2 denotes to splits at the first two whitespaces/occurrences
# expand parameter False by default and gives o/p as list
# if expand=True, then it splits the values in separate columns
print(summer.Event.str.split(" ", n=2, expand=True))

# checks for "100M" values at any point in the string
print(summer.Event.str.contains("100M"))  # boolean series
print(summer[summer.Event.str.contains("100M")])
