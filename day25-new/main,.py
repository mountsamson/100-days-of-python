
# with open ("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open ("weather_data.csv") as data_file:
#    data =  csv.reader(data_file)
#    tempreatures = []

#    for row in data:
#        if(row[1]) != "temp":
#            tempreatures.append(int(row[1]))
           
# print(tempreatures)

import pandas

data = pandas.read_csv("weather_data.csv")

# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# print(data["temp"].mean())

# print(data["temp"].max())

# #Get data in columns
# print(data["condition"])
# print(data.condition)

#get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# Monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(  monday_temp_F )

#create  a dataframe

data_dict = {
    "students" : ["Amy", "James", "Angela", "Mel"],
    "scores" : [76, 56, 65, 100]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")