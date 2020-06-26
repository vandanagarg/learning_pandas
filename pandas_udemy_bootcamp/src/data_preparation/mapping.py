''' Transformation/Mapping
Transform values in a column to other values using transformation
rules for each element in the column '''
from create_dataframes import summer, titanic


sample = summer.sample(n=7, random_state=123).sort_values(by="Year")
print(sample)

# Along with the city(host city) column we would like to add host country
# column too which will be decided on below dictionary keys
city_country = {"Paris": "France", "Mexico": "Mexico", "Montreal": "Canada",
                "Moscow": "Russia", "Barcelona": "Spain", "Athens":  "Greece"}
print(city_country)

# apply transformation rules with the map method for city column each element
print(sample.City.map(city_country))

sample["Host_Country"] = sample.City.map(city_country)
print(sample)

# titanic dataset
# create a new mapping rule for pclass column
mapper = {1: "First", 2: "Second", 3: "Third"}

print(titanic.pclass.map(mapper))

titanic.pclass = titanic.pclass.map(mapper)
print(titanic.head())
''' The whole essence of using map method is to if we need to replace/map
existing values with some new values we can create a dictionary with old
values(keys) and new values(values) and pass this dictionary to map method '''
