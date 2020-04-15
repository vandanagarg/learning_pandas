""" Creating dataframes from scratch with pd.DataFrame() :
We have 2 ways depending on the raw data that we have:
either we have set of columns or else we have rows """
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
print("\n Printing dictionary using raw columns data:")
print(dic)
df = pd.DataFrame(data=dic)
print(df)
players = df.set_index("Player")
print(players)

# Having Rows in place: lists of tuples for different players
print("\n Printing dictionary using raw rows data:")
print(list(zip(nationality, club, world_champion, height, goals)))
zipped = list(zip(nationality, club, world_champion, height, goals))
print(zipped)
# assinging to the respective variables
messi, ronaldo, neymar, mbappe, neuer = zipped
print(messi)
print(ronaldo)
df = pd.DataFrame(data=[messi, ronaldo, neymar, mbappe, neuer],
                  index=["Lionel Messi", "Cristiano Ronaldo", "Neymar Junior",
                         "Kylian Mbappe", "Manuel Neuer"],
                  columns=["Nationality", "Club", "World_Champion", "Height",
                           "Goals_2018"])
print(df)

# using pd.Series method
print("\n Printing dataframe using pd.Series method:")
df2 = pd.Series(index=player, data=nationality, name="Nationality").to_frame()
print(df2)
df2["Club"] = club
print(df2)
# hence, we can keep on adding more columns to the dataframe as required
