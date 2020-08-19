import pandas as pd
from file_utilities import FILE_PATH


df = pd.read_csv(FILE_PATH + "dataset_student_mat.csv")

df = df.loc[:, "school": "guardian"]
print(df)

capitalizer = lambda x: x.capitalize()  # noqa: E731

df["Mjob"] = df["Mjob"].apply(capitalizer)
df["Fjob"] = df["Fjob"].apply(capitalizer)
print(df["Fjob"])

''' Print the last elements of the data set '''
print(df.tail())


def majority(x):
    # df/series wise operation
    if x > 17:
        return True
    else:
        return False


df["legal_drinker"] = df.age.apply(majority)
print(df)


def mul(x):
    # elementwise operation
    if type(x) is int:
        return 10 * x
    return x


df = df.applymap(mul)
print(df)
