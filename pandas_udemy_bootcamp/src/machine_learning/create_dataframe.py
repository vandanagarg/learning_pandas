''' Creating housing dataframe '''
import pandas as pd
import config_file  # noqa: F401
from utilities.file_utilities import FileUtilities


PATH = FileUtilities.get_abs_path("../../Course_Materials_Part4/Bonus_Project_ML/")  # noqa: E501
housing_data_file = PATH + "housing.csv"

# information on houses of more than 20,000 districts of California
# each row stands for a district in California and we have 10 features
housing_df = pd.read_csv(housing_data_file)
# print(housing_df)
