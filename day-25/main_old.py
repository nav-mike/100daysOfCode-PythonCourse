# import csv

# with open("weather_data.csv", mode="r") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
#
# print(f"{data['temp'].max()}")

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

COLORS = ['Gray', 'Cinnamon', 'Black']
result = []

for key in COLORS:
    result.append(data[data['Primary Fur Color'] == key]['Unique Squirrel ID'].count())

new_data = pandas.DataFrame.from_dict({'Fur Color': COLORS, 'Count': result})
new_data.to_csv("squirrel_data.csv")
