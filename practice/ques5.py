import pandas as pd


url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"  # noqa: E501

euro12 = pd.read_csv(url)
# euro12 = pd.read_csv(url, usecols=["Goals"])
print(euro12.Goals)
print(euro12)
print(euro12.Team.nunique())
print(euro12.shape[0])
print(euro12.shape[1])

discipline = euro12[["Team", "Yellow Cards", "Red Cards"]]
print(discipline.sort_values(["Red Cards", "Yellow Cards"])[
    ["Team", "Red Cards", "Yellow Cards"]])

print(discipline["Yellow Cards"].mean())

print(euro12[euro12["Goals"] > 6])

# print(euro12[euro12.Team.filter(regex="^G")])
print(euro12[euro12.Team.str.startswith('G')])

print(euro12.iloc[:, :7])
print(euro12.iloc[:, :-3])

print(euro12.loc[euro12.Team.isin(
    ["England", "Italy", "Russia"]), ["Team", "Shooting Accuracy"]])
