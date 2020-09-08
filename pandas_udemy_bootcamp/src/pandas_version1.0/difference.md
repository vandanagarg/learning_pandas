# What's new in Pandas Version 1.0

#### 1. Display Options:
Older: By default 60 rows (first 30 and last 30)

```python
pd.options.display.max_rows
60
pd.options.display.min_rows
None
```

New:
By default 10 rows (first 5 and last 5)

For more than 60 rows min_rows option prevails
```python
pd.options.display.max_rows
60
pd.options.display.min_rows
10
```

#### 2. Info method:
Gives meta information on data frames: index, columns, missing values in columns, data types of columns, memory usage etc.

New version has headers and there is consecutive labelling of the columns.

#### 3. New nullable dtypes:
This is still experimental
Till now for strings and in case of any missing value columns are marked as "object" data type.
Also in case of integer values if there is a single missing value the column changes into float dtype.
convert_dtypes() method helps covert the df into most suitable data types.
It also gives select_dtypes() method more flexibility to select any particular column dtype directly.

#### 4. pd.NA value for missing values
Older: 
* Originally nan comes from numpy package np.nan
* Till now we had different indicators for missing values for different datatypes

New: 
* New version explicitly has a NAN missing type pd.NA
* Now pd.NA will be a missing value indicator consistent across all dataypes.

```python
pd.NA
<NA>
type(pd.NA)
<class 'pandas._libs.missing.NAType'>
```

#### 5. Addition of the ignore_index parameter
ignore_index parameter is an alternative for reset_index method.
It can be used to re arrange the indexes in sort_values and drop_duplicates() methods.

#### 6. Removal of prior version deprecations
* Separate label and position based indexing.
* reindex method for handling missing keys.
* No direct ptp.() method to find range for a column.
