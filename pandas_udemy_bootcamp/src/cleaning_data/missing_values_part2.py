''' Removing missing values with dropna() '''
from missing_values_part1 import titanic, summer


''' There are generally 3 ways to deal with missing values:
1. do nothing with missing values and just keep them as it is
2. Ignore/drop all rows/columns with missing values
3. replace missing values with some other value
but it is not certain which needs to be followed '''

# Titanic dataset
titanic.info()
print(titanic[titanic.Emb.isna()])
''' here in this case we just have 2 NA values but we can't remove these
although emb column doesn't greatly effects the interpertation of data but for
other columns we will loose imp values so here we let these values be NA '''

''' For age column as well since we have a lot of NA values we can't afford to
drop them and thus we leave them as it is, since pandas is capable of
handling missing values and even if we need to apply any method on age column
it will not give any error as it will just ignore missing values '''
print(titanic.Age.value_counts(dropna=False))
print(titanic.Age.mean(skipna=True))
print(titanic.Age.mean(skipna=False))  # nan

# original shape of dataframe before dropping missing values
print(titanic.shape)
# shape of dataframe after dropping missing values
print(titanic.dropna().shape)
''' dropna() with default parametres axis=0, how="any" drops all rows with
at-least 1 missing value, hence we are left with only 182 rows'''

# drop rows with atleast 1 missing value
print(titanic.dropna(axis=0, how="any").shape)
# drop columns with atleast 1 missing value
print(titanic.dropna(axis=1, how="any").shape)
# drop rows with all missing value
print(titanic.dropna(axis=0, how="all").shape)
# drop columns with all missing value
print(titanic.dropna(axis=1, how="all").shape)

# here the above parameters are not so useful hence we use thresh
print(titanic.dropna(axis=0, thresh=8).shape)
# here we will drop those rows where we have 2 missing values
print(titanic.dropna(axis=1, thresh=500).shape)
# here we drop those columns where we don't have at least 500 not null values

titanic.dropna(axis=1, thresh=500, inplace=True)
# hence we drop deck column where more that 500 values are missing
print(titanic.shape)

''' subset parameter - helps decide which columns we want to focus for dropna()
here it drops all rows where we have less than 4 non missing values or
more than 4 missing values or we shouldn't have any missing value for
these 4 columns, here it drops all rows of age column with NA values '''
print(titanic.dropna(axis=0, subset=["Survived", "Class", "Gender", "Age"],
                     thresh=4).shape)
print(titanic.dropna(axis=0, subset=["Survived", "Class", "Gender", "Age"],
                     how="any").shape)
# drops rows for NA values in any of the columns mentioned, works same as above
# but here we decide not to drop those rows since we will loose important data

# Olympic Dataset
summer.info()
print(summer[summer.isna().any(axis=1)])
summer.dropna(inplace=True)
summer.info()
