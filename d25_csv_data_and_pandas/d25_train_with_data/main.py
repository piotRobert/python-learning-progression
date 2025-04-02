PROJECT_FILES = "d25_csv_data_and_pandas/d25_train_with_data"

# with open(f"{PROJECT_FILES}/weather_data - Sheet1.csv") as file:
#     data = [line.strip() for line in file.readlines()]

# print(data)


# import csv
# with open(f"{PROJECT_FILES}/weather_data - Sheet1.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas


# EXAMPLES of use 
# data = pandas.read_csv(f"{PROJECT_FILES}/weather_data - Sheet1.csv")

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# average_temp = data["temp"].mean()
# print(average_temp)

# max = data["temp"].max()
# print(max)

# GET DATA IN COLUMNS 
# print(data["condition"])
# print(data.condition)

# GET DATA IN ROW
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# CREATE A DATA FROM SCRATCH

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv(f"{PROJECT_FILES}/new_data.csv")

data = pandas.read_csv(f"{PROJECT_FILES}/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250402.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv(f"{PROJECT_FILES}/squirrel_count.csv")