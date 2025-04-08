#  =------------import data from csv files ------------

# with open("weather_data.csv.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# -----------csv data import by csv import -----------------

# import csv
# with open("weather_data.csv.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# ----------------CSV data reader by Pandas libs---------------

# import pandas
# data = pandas.read_csv("weather_data.csv.csv")
# # print(type(data))
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# print(data["temp"].mean)
#
# # average = sum(temp_list) / len(temp_list)
# # print(average)
# print (data["condition"])
# print(data.condition)
#
# # get data in raw
# print(data[data.day == "Tuesday"])
# # ==print()data.temp.max()
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday.condition)
# print(monday_temp_f)
#
# # -------data frame from scratch ---------
# data_dict = {
#     "students": ["Amy", "Jemes", "Aru"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
#
# # ----------make data to csv file ------
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


# ------------------- csv data filter NYC Squirrel -------------
import pandas

data = pandas.read_csv("Squirrel_count.csv")
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)


data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")





