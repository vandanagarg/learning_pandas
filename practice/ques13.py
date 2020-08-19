import pandas as pd


raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

data1 = pd.DataFrame.from_dict(raw_data_1)
data2 = pd.DataFrame.from_dict(raw_data_2)
data3 = pd.DataFrame.from_dict(raw_data_3)
print(data1.shape, data2.shape, data3)

all_data = data1.append(data2)
# all_data = pd.concat([data1, data2])
print(all_data.shape)
print(all_data)

all_data_col = pd.concat([data1, data2], axis=1)
print(all_data_col)

''' Merge all_data and data3 along the subject_id value '''
print(pd.merge(all_data, data3, on='subject_id'))
# 6 sub id is missing

''' Merge only the data that has the same 'subject_id' on both
data1 and data2 '''
print(pd.merge(data1, data2, on='subject_id', how='inner'))

'''  Merge all values in data1 and data2, with matching records
from both sides where available '''
print(pd.merge(data1, data2, on='subject_id', how='outer'))
