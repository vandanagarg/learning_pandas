# Pandas (v 1.0)

#### Intro
* Pandas is the heart of Python Data Science.
1. NumPy
2. SciPy
3. TensorFlow
4. Scikit learn
5. Stats Models
6. Matplotlib seaborn

* NaN - Not a number or missing values.
* Object datatype - For string or text data or Mixed data types.
* Pandas is a class.

#### We have 3 main classes/data types in pandas.
1. **Pandas Dataframe:** An object in python terms and is an instance of class pandas.
    `pandas.core.frame.DataFrame`
2. **Pandas Series:** It shows only one column/row. It is a one dimensional labelled array.
   It is called labelled since it contains rows/columns data along with the indexes of the data frame.
    `pandas.core.series.Series`
3. **Index Object:** It includes either the row or column index object information.
    `pandas.core.indexes.base.Index`
    `pandas.core.indexes.range.RangeIndex`

#### Position based indexing

* Selecting/Slicing a particular element/row/column is called position based indexing using iloc[].
* Zero based indexing and negative indexing are two concepts limited to python.
* Zero based indexing is that the indexes will start from "0" and is valid for data frames as well.
* Negative indexing is that the indexes from the last element will start from "-1" and is valid for data frames as well.

#### Label based indexing

* Data frame indexes are not like primary keys, the duplicate values are allowed in data frame indexes.
* In real world it's more safe to search for values using label based indexing as positions are always prone to changes.
* Using label indexing we can even fetch multiple occurrences of the same label/value.
* Here while passing the values the boundaries are inclusive.
* If we try to slice data using a non-unique index it gives error as it can't determine to which occurrence it is referring to.
* There is no such errors in slicing with unique labeled indexes.

#### Indexing and Slicing with reindex()

* In case of missing or undefined label names use reindex() method.
* Reindex is frequently used with time series data where we have date time index.
* One advantage of reindex is that we can pass row and column labels to reindex that are not in the data frame. This doesn't work with loc[] and returns error.
* But it doesn't work with non-unique index labels, so in order to use reindex() method the index labels have to be unique.
* Syntax: reindex(index=["PASS ROW INDEXES"], columns=["PASS COLUMN NAMES"])
* We need to always pass values for index and columns as a list even if it's a single parameter.

##### *We can always chain various indexing operations but it is advised to use single indexing operation to fetch details at once.*
