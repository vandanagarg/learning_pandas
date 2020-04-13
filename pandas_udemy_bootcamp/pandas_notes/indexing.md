# Types of Indexing in Pandas in order to fetch row and column details

* There are 3 ways to fetch indexed data from a data frame
1. Position based indexing - using numbers/ indexes/ range
2. Label based indexing - using row/ column labels
3. Using reindex() - Using both number/position and label indexes
* Try using following format `dataframe_name.method_name[rows/index/[names], columns/index/[names]]` while indexing and fetching data for a row/column.

#### Position based indexing (iloc[])

* Selecting/Slicing a particular element/row/column is called position based indexing using iloc[].
* Zero based indexing and negative indexing are two concepts limited to python.
* Zero based indexing is that the indexes will start from "0" and is valid for data frames as well.
* Negative indexing is that the indexes from the last element will start from "-1" and is valid for data frames as well.

#### Label based indexing (loc[])

* Data frame indexes are not like primary keys, the duplicate values are allowed in data frame indexes.
* In real world it's more safe to search for values using label based indexing as positions are always prone to changes.
* Using label indexing we can even fetch multiple occurrences of the same label/value.
* Here while passing the values the **boundaries are always inclusive**.
* If we try to slice data using a non-unique index it gives error as it can't determine to which occurrence it is referring to.
* There is no such errors in slicing with unique labeled indexes.

#### Indexing and Slicing with reindex()

* In case of missing or undefined label names use reindex() method.
* Reindex is frequently used with time series data where we have date time index.
* One advantage of reindex is that we can pass row and column labels to reindex that are not in the data frame. This doesn't work with loc[] and returns error.
* But it **doesn't work with non-unique index labels**, so in order to use reindex() method the index labels have to be unique.
* Syntax: reindex(index=["PASS ROW INDEXES"], columns=["PASS COLUMN NAMES"])
* We need to always **pass values as a list** for index and columns even if it's a single parameter.

##### *We can always chain various indexing operations but it is advised to use single indexing operation to fetch details at once.*
