''' Customizing import with pd.read_excel() '''
import pandas as pd
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


source_file = dfu.FILE_PATH + "summer_raw.xls"
target_file_csv = dfu.FILE_PATH + "summer_cleaned_xls.csv"
target_file = dfu.FILE_PATH + "summer_cleaned_xls.xls"

summer = pd.read_excel(source_file)  # default 1st sheet
summer = pd.read_excel(source_file, sheet_name="summer")
summer = pd.read_excel(source_file, sheet_name="summer", skiprows=2)
summer = pd.read_excel(source_file, sheet_name="summer",
                       skiprows=2, index_col=0, usecols="C:L")
summer = pd.read_excel(source_file, sheet_name="summer",
                       skiprows=2,  usecols="D:L")
print(summer)
print(summer.head())
print(summer.tail())
summer.info()

summer.to_csv(target_file_csv, index=False)  # don't save existing indexes
summer.to_excel(target_file)
print(pd.read_csv(target_file_csv))
