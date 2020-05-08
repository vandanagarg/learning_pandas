''' Creating population and sample numpy arrays '''
import pandas as pd
import config_file  # noqa: F401
from utilities.file_utilities import FileUtilities


PATH = FileUtilities.get_abs_path("../../Course_Materials_Part1/Statistics/Course_Materials_Statistics/Video_Lectures_NBs/")  # noqa: E501
TARGET_PATH = FileUtilities.get_abs_path("../Statistics/")
movie_data_file = PATH + "movies_metadata.csv"

# metadata for the movies which were released before july 2017 from Kaggle site
movie_df = pd.read_csv(movie_data_file, low_memory=False)
# print(movie_df)
# sys:1: DtypeWarning: Columns (10) have mixed types.Specify dtype option
#  on import or set low_memory=False.
# to avoid this warning we have to keep low_memory=False default is True

# reading the target file
df = pd.read_csv(TARGET_PATH + "bud_vs_rev.csv", parse_dates=["release_date"],
                 index_col="release_date")
# print(df)
