import pandas

data = pandas.read_csv("day025_us-states-game/exercise/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

jumlah_tupai_berdasarkan_warna = data.groupby('Primary Fur Color')['Unique Squirrel ID'].count()

jumlah_tupai_berdasarkan_warna.to_csv("day025_us-states-game/exercise/jumlah_tupai_berdasarkan_warna.csv")


# ==============
# SOLUSI ANGELA:
# ==============
# filter dulu datanya berdasarkan 'Primary Fur Color' == warna bulu nya, 
# terus hitung jumlah row data yang udah difilter itu pakai len
# nanti outputnya masukin ke variabel data jumlah tupai per warna bulu nya apa
# kayak gini contohnya:
# jumlah_tupai_hitam = len(data[data["Primary Fur Color"] == "Black"])

# lalu, bikin dictionary
# keys nya "warna_bulu" sama "jumlah"
# values nya kalau warna_bulu itu isi aja sama str masing-masing warna bulu
# kalau jumlah, isinya si variabel yang udah kita bikin sebelumnya
# jadi kayak gini dictionary nya:
# data_dict = {
#   "warna_bulu": ["hitam", "merah", "abu"],
#   "jumlah": [jumlah_tupai_hitam, jumlah_tupai_merah, jumlah_tupai_abu]
# }

# abis itu, bikin dataframe baru, namain df
# bikinnya pakai pandas
# kayak gini:
# df = pandas.DataFrame(data_dict)

# terus konversikan df nya ke csv:
# df.to_csv("file path nya")

# =================
# END SOLUSI ANGELA
# =================