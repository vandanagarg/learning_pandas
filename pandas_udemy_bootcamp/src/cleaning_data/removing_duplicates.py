''' Handling/Removing Duplicates '''
from duplicates import titanic, summer, alphabet


''' In titanic dataset due to no key identifier, also mostly duplicate
entries is for 3rd class passengers for whom the fare price is same and
we don't have their age data and we have manually assigned mean value for
those fields in age column. Hence, we can't confirm if those rows of
the potential duplicates are real duplicates, hence we just will
practice deleting last 3 duplicate rows from our dataframe '''

print(titanic.tail())
print(titanic.duplicated().sum())
print(titanic[titanic.duplicated()])
titanic.drop(index=[891, 892, 893], inplace=True)
print(titanic.head())
print(titanic.tail())
titanic.info()

# Olympic Dataset
print(summer.head())
print(summer.duplicated().sum())
print(summer[summer.duplicated(keep=False)])  # 7 pairs
summer.drop(index=[2069, 12253, 15596, 21833, 28678], inplace=True)
print(summer[summer.duplicated(keep=False)])

''' if we see for rest 2 duplicate pairs, the name Singh is very common
in india and also a bit of google research shows that these were 2
different people and hence pretty sure these entries are not duplicate.
Also for other 2 entries the game was double player game and that person
Zhao probably played in 2 different team groups and hence 2 entries for 2
different events but an identifier is missing to prove that; hence these
can't be real duplicates and shouldn't be deleted '''
print(summer.loc[16085:16110])
print(summer.loc[29780:29795])

# alphabet dataframe
print(alphabet[alphabet.duplicated(keep=False)])
alphabet.drop_duplicates(inplace=True)
print(alphabet)
''' Hence for handling duplicates it becomes quite important to have
domain knowledge as well, since the combination of pandas and domain
knowledge combined will help take better decisions to eliminate duplicates '''
