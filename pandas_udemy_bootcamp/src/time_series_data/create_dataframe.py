''' Time Series dataframes '''
import pandas as pd
import config_file  # noqa: F401
from utilities.file_utilities import FileUtilities


PATH = FileUtilities.get_abs_path("../../Course_Materials_Part5/Video_Lecture_NBs/")  # noqa: E501
temp_file = PATH + "temp.csv"

temp = pd.read_csv(temp_file)
# print(temp)
