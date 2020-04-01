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
* Pandas data frame is a datatype.
* Pandas series is a datatype too - it shows only one column/row. It is a one dimensional labelled array.
* It is called labelled since it contains rows/columns data along with the indexes of the data frame.

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
