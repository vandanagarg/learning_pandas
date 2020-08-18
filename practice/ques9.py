import pandas as pd


raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks',
                         'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons',
                         'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd',
                        '2nd', '1st', '1st', '2nd', '2nd'],
            'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon',
                     'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
            'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

# regiment = pd.DataFrame(raw_data, columns=raw_data.keys())
regiment = pd.DataFrame.from_dict(raw_data)
print(regiment)

print(regiment.groupby("regiment").mean())
print(regiment.groupby("regiment").preTestScore.mean())
print(regiment.loc[regiment.regiment == "Nighthawks"].preTestScore.mean())

print(regiment.groupby("company").describe())
print(regiment.groupby(["regiment", "company"]).describe())

print(regiment.groupby("company").preTestScore.mean())

print(regiment.groupby(["regiment", "company"]).preTestScore.mean())

''' Present the mean preTestScores grouped by regiment and
company without heirarchical indexing '''
print(regiment.groupby(['regiment', 'company']).preTestScore.mean().unstack())

print(regiment.groupby(["regiment", "company"]))
print(regiment.groupby(["regiment", "company"]).mean())
print(regiment.groupby(["regiment", "company"]).size())

# total observations
df = regiment.groupby(["regiment", "company"])
print(len(df))

for i in df:
    print(i)

# Group the dataframe by regiment, and for each regiment,
for name, group in regiment.groupby('regiment'):
    # print the name of the regiment
    print(name)
    # print the data of that regiment
    print(group)
