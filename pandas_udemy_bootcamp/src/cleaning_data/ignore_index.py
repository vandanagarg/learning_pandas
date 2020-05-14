''' The ignore_index parameter (NEW in Pandas 1.0) '''
import pandas as pd


alphabet = pd.DataFrame(["a", "b", "c", "c", "d", "e", "f", "g", "g", "g"],
                        columns=["Alphabet"])
print(alphabet)

# checks for all rows for duplicate values/entries
# keep=False marks all occurrences as True, can be changed as well
print(alphabet.duplicated(keep=False))  # boolean series
print(alphabet[alphabet.duplicated(keep=False)])  # duplicate entries
print(alphabet.drop_duplicates())
alphabet.drop_duplicates().info()
# gives entries Int64Index: 7 entries, 0 to 7, but 3 is missing here
# hence the indexes are not correct, this can be corrected either by
# using reset_index() method or in new version there is this new
# parameter ignore_index which can be used to correct the indexes
print(alphabet.drop_duplicates(ignore_index=True))
alphabet.drop_duplicates(ignore_index=True).info()
# now we have correct range index 0 to 6 : RangeIndex: 7 entries, 0 to 6
