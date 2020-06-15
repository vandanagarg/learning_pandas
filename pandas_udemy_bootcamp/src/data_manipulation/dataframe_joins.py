''' Performing Joins on Dataframes using method merge()
Works similar to database concepts of joins
We can also use join() method but it is not so versatile '''
from create_dataframes import men2004, men2008


''' Outer Join (Full Outer Join)
Athletes with atleast 1 medal in either year '''
print(men2004.shape)
print(men2008.shape)
print(len(men2004) + len(men2008))

print(men2004.merge(men2008, how="outer", on="Athlete"))
# changing the column labels
print(men2004.merge(men2008, how="outer", on="Athlete",
      suffixes=("_2004", "_2008")))
# using indicator parameter, initially False. It tells if
# the row is from left df or right or is present in both df's
print(men2004.merge(men2008, how="outer", on="Athlete",
      suffixes=("_2004", "_2008"), indicator=True))

men0408 = men2004.merge(men2008, how="outer", on="Athlete",
                        suffixes=("_2004", "_2008"), indicator=True)
print(men0408)
print(men0408._merge)
# further evaluations
print(men0408._merge.value_counts())

''' Inner Join
athletes present in both years '''
print(men2004.merge(men2008, how="inner", on="Athlete",
      suffixes=("_2004", "_2008"), indicator=True))

''' Outer Join without intersection (Half Outer Join)
It is opposite to inner Join means athletes who were successful
in only one Edition, not in both '''
# option1: excluding value "both" from _merge in full outer join
print(men0408.loc[men0408._merge != "both"])  # 89 rows

''' Left Join without Intersection (Left half Outer Join)
All athletes who were successful only in Edition 2004
This can be done filtering the dataframe from outer join
for left_only rows in _merge column '''
print(men0408.loc[men0408._merge == "left_only"])
# or
print(men0408[men0408._merge == "left_only"].shape)  # 43 rows

''' Right Join without Intersection (Right half Outer Join)
All athletes who were successful only in Edition 2008
This can be done filtering the dataframe from outer join
for right_only rows in _merge column '''
print(men0408.loc[men0408._merge == "right_only"])
# or
print(men0408[men0408._merge == "right_only"].shape)  # 46 rows

''' Left Join
All athletes who were successful in Edition 2004(incld 2008 medals) '''
print(men2004.merge(men2008, how="left", on="Athlete",
      suffixes=("_2004", "_2008"), indicator=True))  # 59 rows

''' Right Join
All athletes who were successful in Edition 2008(incld 2004 medals) '''
print(men2004.merge(men2008, how="right", on="Athlete",
      suffixes=("_2004", "_2008"), indicator=True))  # 62 rows
