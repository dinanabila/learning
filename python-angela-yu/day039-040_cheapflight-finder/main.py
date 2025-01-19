#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
import time

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.ambil_kota()
print(sheet_data)


for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] == flight_search.dapetin_iata_code(row["city"])
        time.sleep(2)
print(f"sheet data:\n{sheet_data}")

data_manager.data_sheety = sheet_data
data_manager.masukin_iata_code_ke_spreadsheet()
