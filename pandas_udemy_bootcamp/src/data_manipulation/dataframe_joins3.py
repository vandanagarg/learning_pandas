''' Joining dataframes on more than one Column '''
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


men2004_det = dfu.get_dataframe("men2004_det.csv")
men2008_det = dfu.get_dataframe("men2008_det.csv")
print(men2004_det.head())
print(men2008_det.head())
print(men2004_det.loc[men2004_det.Athlete == "PHELPS, Michael"])
print(men2008_det.loc[men2008_det.Athlete == "PHELPS, Michael"])

''' Here if we consider rows only for "PHELPS, Michael" then we have duplicate
rows in 2004 df but if we look for combination of Athlete and Medal column
then rows are unique. Hence to decide keys on which we need to join dataframe
we need to identify how we want data to be grouped as in this case if we join
only on Athlete column we get combination of data from 2 dataframes if we join
on both columns then the data groups correctly as per the medals '''

# Joining on Athlete column
men0408 = men2004_det.merge(men2008_det, how="outer", on="Athlete",
                            suffixes=("_2004", "_2008"))
print(men0408.loc[men0408.Athlete == "PHELPS, Michael"])  # not expected o/p
# o/p on combination of athlete

# Joining on Athlete and Medal column
men0408 = men2004_det.merge(men2008_det, how="outer", on=["Athlete", "Medal"],
                            suffixes=("_2004", "_2008"))
print(men0408.loc[men0408.Athlete == "PHELPS, Michael"])  # expected o/p
# o/p on combination of athlete and medals

# inner join
men0408 = men2004_det.merge(men2008_det, how="inner", on=["Athlete", "Medal"],
                            suffixes=("_2004", "_2008"))
print(men0408.loc[men0408.Athlete == "PHELPS, Michael"])  # expected o/p
# o/p on combination of athlete and medal(gold) present in both dataframes
