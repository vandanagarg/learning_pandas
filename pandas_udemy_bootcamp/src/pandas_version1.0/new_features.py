''' Addition of the ignore_index parameter '''
import numpy as np
from create_dataframe import players, players1, players3


# way 1: After sorting players df ignore previous jumbled
# indexes by reset_index method explicitly
print(players.sort_values(by="Height", ascending=False).reset_index(drop=True))

# way 2: After sorting players df ignore previous jumbled
# indexes by ignore_index parameter (False by default)
print(players.sort_values(by="Height", ascending=False, ignore_index=True))

print(players3)
# also for drop_duplicates method to ignore previous jumbled
# indexes by ignore_index parameter (False by default)
print(players3.drop_duplicates(ignore_index=True))

''' Removal of prior version deprecations '''

''' 1. label and position based indexing '''
# possible in previous versions with ix method
# players1.ix["Lionel Messi", [1, 4]]

# alternative in current version
# get the label names
print(players1.columns[[1, 4]])
print(players1.loc["Lionel Messi", players1.columns[[1, 4]]])

''' 2. handling missing keys'''
# possible in previous versions: unknown keys returns NAN values
# players1.loc[["Lionel Messi", "Donald Duck"]]

# alternative in current version use reindex method
print(players1.reindex(labels=["Lionel Messi", "Donald Duck"]))
# reindex only works with unique indexes not duplicate

''' 3. direct ptp() method to find range of a numerical column '''
# possible in previous versions:
# players1.Height.ptp()

# alternative in current version
print(players1.Height.max() - players1.Height.min())
# using np.ptp() method
print(np.ptp(players1.Height))
