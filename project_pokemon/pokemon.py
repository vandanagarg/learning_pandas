import pandas as pd

df = pd.read_csv("/Users/peeyushsingla/projects/learning_pandas/project_pokemon/pokemon_data.csv")

# print(df)

# print(df.head(3))
# print(df.tail(3))

# print(df.columns)
# print(df.Name)
# print(df["Name"])
# print(df[['Name',"Type 1","HP" ]][0:5])
# print(df.head(4))
# print(df.iloc[1])
# print(df.iloc[1:4])

#specific location
# print(df.iloc[2,1])

# for index, row in df.iterrows():
#     print(index, row.Name)

#specific data

# print(df.loc[df["Type 1"]== "Fire"])

# print(df.describe())

#sort

# print(df.sort_values("Name"))

# print(df.sort_values(["Type 1", "HP"], ascending = [1,0]).head(10))

# df["Total"] = df.iloc[:,4:10].sum(axis= 1)
# print(df.Total.head(10))

#rearranging columns

# df = df[["Total", "HP", "Defense"]]

# cols = list(df.columns.values)
# df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

# print(df.head(5))

# df.to_csv("total.csv", index= False)

# print(df.loc[(df["Type 1"] == "Grass") | (df["Type 2"] == "Poison")].head(10))

#new dataframes

# new_df = df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison")  & (df["HP"]> 70)]
# new_df.to_csv("filtered.csv", index = False)

# new_df = new_df.reset_index(drop = True)
# new_df.to_csv("filtered_new.csv", index = False)
# print(new_df)


# exclude data

# print(df.loc[ ~ df["Name"].str.contains("Mega")])

#conditional change

# df.loc[df["Type 1"]== "Fire", "Type 1"] = "Flamer"
# print(df)
# print(df.loc[df["Type 1"]== "Flamer"])


#aggregate

# print(df.groupby(["Type 1"]).count())

# df["count"] = 1
# print(df.groupby(["Type 1"]).count()["count"])
# print(df.groupby(["Type 1", "Type 2"]).count()["count"])


# partial data

chunk_df = pd.DataFrame(columns = df.columns)

for df in pd.read_csv("/Users/peeyushsingla/projects/learning_pandas/project_pokemon/pokemon_data.csv", chunksize = 5):
    results = df.groupby(["Type 1"]).count()

chunk_df = pd.concat([chunk_df, results])

print(chunk_df)