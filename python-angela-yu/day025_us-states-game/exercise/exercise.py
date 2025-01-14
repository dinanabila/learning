# import csv

# with open("day025_us-states-game\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row[1])
#         if row[1] == 'temp': # kecualiin si temp, kita ga mau masukin tulisan temp
#             pass
#         else:
#             temperatures.append(int(row[1]))

# print(temperatures)

# =============================
# cara di atas, bertele-tele
# makanya, mending pakai pandas
# lihat bedanya:
# =============================

import pandas

data = pandas.read_csv("day025_us-states-game/exercise/weather_data.csv")

# print(data["temp"])

# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# hitung rata-rata temperature
# ini cara sangat manual
total_suhu = 0
for suhu in temp_list:
    total_suhu += suhu

temp_avg = total_suhu/(len(temp_list))
print(f"Rata-rata suhu: {temp_avg}")

# cara simpel, manfaatin pandas
print(f"Rata-rata suhu pakai pandas: {data["temp"].mean()}")


# suhu max
print(f"Suhu max pakai pandas: {data["temp"].max()}")

# dapetin data row
print(data[data["day"] == "Monday"])


# dapetin data row dengan suhu max
print(data[data["temp"] == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# data[data.day == "Monday"]["condition"]


# konversi suhu monday ke fahrenheit. sebelumnya celcius
print(f"Suhu hari Senin dalam fahrenheit: {monday.temp * 9/5 + 32}")