"""with open("weather_data.csv") as weather_days:
    weather = weather_days.readlines()
    print(weather)"""

"""import csv


with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row[1])
"""

"""import pandas

data = pandas.read_csv("weather_data.csv")
#print(data["temp"])"""

"""data_dict = data.to_dict()

#print(data_dict)

data_list = data["temp"].to_list()
print(data_list)
print(data["temp"].max())"""

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#gray_squirrel = data[data["Primary Fur Color"] == "Gray"]
#print(gray_squirrel)

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_squirrel_count)

cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(cinnamon_squirrel_count)

black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrel_count)

dict_squirrel ={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

data_frame = pandas.DataFrame(dict_squirrel)

data_frame.to_csv("Squirrel Count.csv")
