import pandas as pd


url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"
users = pd.read_csv(url, sep="|", header=0)
# print(users)

df = users.groupby("occupation")
print(df.age.mean())


def gender_to_numeric(x):
    # create a function
    if x == 'M':
        return 1
    if x == 'F':
        return 0


# apply the function to the gender column and create a new column
users['gender_n'] = users['gender'].apply(gender_to_numeric)

a = (users.groupby('occupation').gender_n.sum() /
     users.occupation.value_counts()) * 100

print(a)
print(users.occupation.value_counts())
# sort to the most male
print(a.sort_values(ascending=False))

print(df.age.agg(["min", "max"]))

print(users.groupby(["occupation", "gender"]).age.mean())
print(users.groupby(["gender", "occupation"]).age.mean())

# create a data frame and apply count to gender
gender_ocup = users.groupby(['occupation', 'gender']).agg({'gender': 'count'})

# create a DataFrame and apply count for each occupation
occup_count = users.groupby(['occupation']).agg('count')

# divide the gender_ocup per the occup_count and multiply per 100
occup_gender = gender_ocup.div(occup_count, level="occupation") * 100

# present all rows from the 'gender column'
print(occup_gender)
print(occup_gender.loc[:, 'gender'])
