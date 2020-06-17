''' Transformation with method transform() on groupby object '''
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


# Titanic Dataset
titanic = dfu.get_dataframe("titanic.csv")
print(titanic.groupby(["sex", "pclass"]).survived.mean())

''' to set this values against each row so as it is easy to understand data
further we can create a new column and assign it the mean values using
transform method '''
print(titanic.groupby(["sex", "pclass"]).survived.transform("mean"))
# gives a pandas series

# creating a new column and assigning mean values
titanic["group_surv_rate"] = titanic.groupby(["sex", "pclass"]
                                             ).survived.transform("mean")
print(titanic.head())

''' to check outliers we substract group_surv_rate value from survived value
& lower the outliers value more closer is the answer to being accurate & if the
outlier value is higher then either it is a outlier or is a special case '''

titanic["outliers"] = abs(titanic.survived - titanic.group_surv_rate)
# a few cases where we have outliers means we have high survival rate but still
# the passanger died and vice versa
print(titanic[titanic.outliers > .85])
