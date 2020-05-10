import pandas as pd
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


source_file = dfu.FILE_PATH + "titanic_raw.csv"
target_file = dfu.FILE_PATH + "titanic_raw_ordered.csv"

titanic_df = dfu.get_dataframe("titanic_raw.csv")
print(titanic_df)

col_names = ["Survived", "Class", "Gender", "Age", "SibSp",
             "ParCh", "Fare", "Emb", "Deck"]
titanic_df = pd.read_csv(source_file, skiprows=3, skipfooter=2, header=None,
                         names=col_names)
# ignore warning here, and since no header given in file pass
# header=None and pass column labels
print(titanic_df)
print(titanic_df.head(10))

# storing cleaned data to a csv file
titanic_df.to_csv(target_file, index=False)
# pass index=False to not store existing indexes, else it reads it as a
# separate column while reading the file next time

imported_file = dfu.FILE_PATH + "titanic_raw_ordered.csv"
df = pd.read_csv(imported_file)
print(df)
