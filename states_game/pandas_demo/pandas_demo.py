# # # with open("weather_data.csv") as data_file:
# # #     data = data_file.readlines()
# # #     #print(data)
# # #
# # # import csv
# # #
# # # with open("weather_data.csv") as data_file:
# # #     data = csv.reader(data_file)
# # #     temperatures = []
# # #     for row in data:
# # #         if row[1] != 'temp':
# # #             temperatures.append(int(row[1]))
# # #     print(temperatures)
# #
# # import pandas
# # data_file = pandas.read_csv("weather_data.csv")
# # # print(data["temp"])
# # temp_list = data_file["temp"].to_list()
# # # print(temp_list)
# # # print(sum(temp_list)/len(temp_list))
# #
# #
# # data_dict = data_file.to_dict()
# # # print(data_dict)
# # monday_data = data_file.day == "Monday"
# # monday_temp = int(data_file.temp[monday_data])
# # fahrenheit = (monday_temp * 1.8) + 32
# # print(fahrenheit)
# # # print(data_file[data_file.temp == data_file.temp.max()])
# #
# import pandas
# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# fur_color_column = squirrel_data["Primary Fur Color"]
# red_squirrel_data = len(squirrel_data[fur_color_column == "Cinnamon"])
# black_squirrel_data = len(squirrel_data[fur_color_column == "Black"])
# gray_squirrel_data = len(squirrel_data[fur_color_column == "Gray"])
#
# df = pandas.DataFrame({'red': [red_squirrel_data],
#                    'black': [black_squirrel_data],
#                    'gray': [gray_squirrel_data]})
# df.to_csv("squirrel_count.csv", index=False)
#
# # TODO: create squirrel_count.csv that Primary Fur Color with Fur Color, Count headers
# # TODO: use data.to_csv("squirrel_count.csv")
