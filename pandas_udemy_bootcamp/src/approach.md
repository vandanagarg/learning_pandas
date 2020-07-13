# Steps to approach a solution

* Import all libraries
* Import all data sets
* Inspect data sets:- head/tail/info/describe
* Filter rows for any missing values
``` df[df.isna().any(axis=1)] ```
* Drop missing values
``` df.dropna(inplace=True) ```
* Check for the same column names and same structure in all the dataframes/ input data we have as it will easy to compare results later and do one by one.
1. Updating values of an existing column:
``` python
dataframe- df
column - NOC
39            Puerto Rico (PUR)
40               Thailand (THA)
41             Totals (41 NOCs)
Name: NOC, dtype: object

df.NOC.str.split("(", expand= True).iloc[:, 1].str.replace(")", "").str.replace("*", "")

o/p:
39        PUR
40        THA
```

2. Saving the o/p as a new column.
```python
df["Country"] = df.NOC.str.split("(", expand= True).iloc[:, 1].str.replace(")", "").str.replace("*", "")
```

3. Drop unwanted columns and set required index column.
```python
df = df.drop(columns =["Rank", "NOC", "Total"]).set_index("Country")
```

4. Transform all dataframes similar to the result's structure. So as it is easy to compare our results.

* Now aggregating actual dataframe for total medals/ to get result.

* The aim is to count total number of medals for each country, in the case of single medals or medals less than 5 it is fine but if its a team even then we need to keep just one medal and treat others as duplicate and remove those entries. 

* For this first identify gender of events(male, female or mixed events) for each row. Google and identify what the hints and extra information means and look for those hints in the existing dataframe in all possible columns or any combination.

* Second we must identify all unique Events and count the amount of medals in each Event (new column Event_Medals). In this we are only considering unique events on bases of Columns "Year", "Sport", "Discipline", "Event", "Event_Gender". We are not considering medal type here. Event_Medals will give the total medals for that unique event. It will help us to identify those events which got more than 5 medals in total.

* Third we must separate the team events so as we can then remove the duplicate entries for the team events.
Here first we should mark if a particular entry is for a team even or not. Then separate single and team event dataframe. Then remove duplicates from team events dataframe and then combine both dataframes again.

* In the end we perform our final groupby to see total number of medals for each country. We can then get data for required year and see if it matches to the given sample results.

* For validations of results : To see the difference and divergence in results we can sub the values of both dataframes and if the sum of those equals 0 means the results are completely same and there is no divergence.


### Tips:
1. Creating a new column from an existing column.
```python
 df["new_column_name"] = df.existing_column
```

2. Creating a new column with some default value.
```python
# string column
 df["new_column_name"] = "abc"
# numeric column
 df["new_column_name"] = 0
```

3. Checking for a string value in a column and ignoring caps.
```python
 df.column_name.str.lower().str.contains("string_to_search").sum()
```

4. Combining two conditions: search for a string and comparing an integer value.
```python
  ((df.column_name.str.lower().str.contains("string_to_search")) & (df.column_name < 1988)).sum()
```

5. Override the existing values in a column if a condition is satisfied.
```python
  # conditions - store the results as pandas series(true or false)
  mask1 = df.column_name.str.lower().str.contains("string_to_search")
  mask2 = ((df.column_name.str.lower().str.contains("string_to_search")) & (df.column_name < 1988))
  
  # if any one of the condition is True from mask1 or mask2, replace the existing value of Event_Gender column with the new value X
  df.loc[mask1 | mask2 , "Event_Gender"] = "X"
```

6. In the case we have a list of indexes/ index labels for which we need to replace an existing value for a column let's say Event_Gender column.
```python
# list of indexes for which existing value needs to be replaced
list_of_indexes = [21773, 21782, 21776,21785, 21770, 21779,23703]

# for df dataframe using loc operator replacing existing value for Event_Gender column with value X
df.loc[list_of_indexes, "Event_Gender"] = "X"
```

7. To check for distinct values and its count in a column.
```python
df.column_name.value_counts()
```

8. To perform groupby operation on a dataframe and perform an aggregation on a specific column lets say(Medal) and then create a new column and store the results into it.
```python
df["Event_Medals"] = df.groupby(["Year", "Sport", "Discipline", "Event", "Event_Gender"]).Medal.transform("count")
```

9. To display distinct values and its count for a column and sort it in ascending order.
```python
df.column_name.value_counts().sort_index()
```

10. To see all the rows for particular column value use loc operator as:
```python
# to search in a column for value 5 in dataframe df
df.loc[df.column_name == 5]
```

11. To compare a value in a column(Event_Medals) and if it satisfies the condition then assign some value("Yes") else assign some default value("No") using numpy where function and also creating a new column("Team") to store the results.
```python
df["Team"] = pd.Series(np.where(df.Event_Medals > 5, "Yes", "No"))
```

12. To remove duplicate rows from a dataframe. Let's say we have to remove duplicate rows from summer dataframe for duplicated medal rows in column Team == Yes or means for Team Events.

* First point to remember is we should always save our original indexes by using reset_index() method so as we can get back to original indexes whenever required.
```python
summer.reset_index(inplace=True)
```

* Second we must split the original dataframe into single and team events and then combine them back after removing duplicate rows.
```python
singles = summer.loc[summer.Team == "No"].copy()
team = summer.loc[summer.Team == "Yes"].copy()

# drop/remove duplicates on the bases of columns "Year", "Sport", "Discipline", "Country", "Event", "Event_Gender", "Medal".(Keep only first occurrence)
team.drop_duplicates(subset = ["Year", "Sport", "Discipline", "Country", "Event", "Event_Gender", "Medal"], inplace = True)

# to concat two dataframes again and save it in a new dataframe
summer_new = pd.concat([singles, team])

# check shape of concatenated dataframe
pd.concat([singles, team]).shape

# to set the original indexes again
summer_new.set_index("index", inplace= True)

# now summer_new dataframe contains are the rows without duplicate medals data for team events
```

13. Grouping the data for total medals for each country for all editions and rearranging the columns.
```python
# groupby on summer_new dataframe and storing results in medal_tables dataframe
medal_tables = summer_new.groupby(["Year", "Country", "Medal"]).Medal.count().unstack(fill_value = 0)[["Gold", "Silver", "Bronze"]]
```

14. Comparing with sample results Medal Tables.
```python
# fetching the results for a particular edition and sorting columns in descending order also saving the results.
agg_1976 = medal_tables.loc[1976].sort_values(["Gold", "Silver", "Bronze"], ascending = False).copy()

# To check the divergence in two dataframes, use sub()/subtract method and drop missing values
div_76 = agg_1976.sub(wik_1976).abs().dropna()
# If all values = 0 means no divergence or both the dataframes are equal/have same values

# we can also check the overall sum of the dataframe to get an idea instead checking each row
score_76 = div_76.sum().sum()
# if sum = 0 means no divergence and results are completely same

# However, it might be just a coincidence that we might get a perfect result as in real scenarios we might get lot of divergence or extreme conditions for some years/cases.
```
