""" Module to create dataframe from a csv file for Course_Materials_Part2 """
import pandas as pd
from utilities.file_utilities import FileUtilities


class DataframeUtilitiesProject:
    """ Returns dataframes either normally indexed or column indexed"""
    FILE_PATH = FileUtilities.get_abs_path("../../Course_Materials_Part2/Video_Lecture_NBs/")  # noqa: E501

    @classmethod
    def get_dataframe(cls, csv_file):
        """ Returns a normally indexed dataframe """
        source_file = cls.FILE_PATH + csv_file
        return pd.read_csv(source_file)

    @classmethod
    def get_indexed_dataframe(cls, csv_file, index_column):
        """ Returns a dataframe indexed on the specified index_column """
        source_file = cls.FILE_PATH + csv_file
        return pd.read_csv(source_file, index_col=index_column)
