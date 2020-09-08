''' Create dataframe Module to create df from csv files '''
import pandas as pd
import config_file  # noqa: F401
from utilities.file_utilities import FileUtilities


PATH = FileUtilities.get_abs_path("../../Course_Materials_Part6/Course_Materials_Version_1_0/")  # noqa: E501
players_file2 = PATH + "players2.csv"
players_file3 = PATH + "players3.csv"

# Players dataset
players = pd.read_csv(PATH + "players.csv")
players1 = pd.read_csv(PATH + "players.csv", index_col="Player")
# print(players)

# Players2 Dataset
players2 = pd.read_csv(players_file2, index_col="Player")
# print(players2)

# Players2 Dataset
players3 = pd.read_csv(players_file3)
# print(players3)
