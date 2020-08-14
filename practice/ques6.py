import pandas as pd


# Create an example dataframe about a fictional army
raw_data = {'regiment':
            ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks',
             'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts',
             'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd',
                        '2nd', '1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973,
                     1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine',
                       'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming',
                       'Louisana', 'Georgia']}

army = pd.DataFrame.from_dict(raw_data)

army.set_index("origin", inplace=True)
print(army)
print(army[["veterans", "deaths"]])
print(army.columns)
print(army.loc[["Maine", "Alaska"], ['deaths', 'size', 'deserters']])
print(army.iloc[2:7, 2:6])
print(army.iloc[4:, :])
print(army.iloc[:4, :])
print(army.iloc[:, 2:7])

print("\n deaths")
print(army[army.deaths > 50])
print(army[(army.deaths > 500) | (army.deaths < 50)])

print(army.loc[army.regiment != "Dragoons"])
print(army.loc[["Texas", "Arizona"], :])
print(army.loc["Arizona"][2])
print(army.loc["Arizona"])
print(army.loc[["Arizona"]])
print(army.loc[["Arizona"]].iloc[:, 2])

print(army.iloc[2]["deaths"])
print(army.loc[:, ["deaths"]].iloc[2])
# print(army.values[2]["deaths"])  # WON'T WORK
# WORKS ONLY FOR INTEGER INDEXES
print(army.values[2][2])
