""" Adding new rows """
import pandas as pd


# Having columns in place
player = ["Lionel Messi", "Cristiano Ronaldo", "Neymar Junior",
          "Kylian Mbappe", "Manuel Neuer"]
nationality = ["Argentina", "Portugal", "Brasil", "France", "Germany"]
club = ["FC Barcelona", "Juventus FC", "Paris SG", "Paris SG", "FC Bayern"]
world_champion = [False, False, False, True, True]
height = [1.70, 1.87, 1.75, 1.78, 1.93]
goals = [45, 44, 28, 21, 0]

dic = {"Player": player, "Nationality": nationality, "Club": club,
       "World_Champion": world_champion, "Height": height, "Goals_2018": goals}
# print(dic)
df = pd.DataFrame(data=dic)
# print(df)
players = df.set_index("Player")
# print(players)

# Adding one Row
players.reset_index(inplace=True)
players.loc[5, :] = ["Sergio Ramos", "Spain", "Real Madrid",
                     True, 1.84, 5]
print(players)

# Adding many Rows
new_df = pd.DataFrame(data=[
    ["Mohamed Salah", "Egypt", "FC Liverpool", False, 1.75, 44],
    ["Luis Suarez", "Uruguay", "FC Barcelona", False, 1.82, 31]],
    columns=players.columns)
# index by default will be range index
print(new_df)
players = players.append(new_df, ignore_index=True)
print(players)
