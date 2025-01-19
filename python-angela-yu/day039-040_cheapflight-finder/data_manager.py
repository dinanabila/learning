SHEETY_BASIC_AUTH = ""
URL_SHEETY = ""

import requests

# Basic Sheety Autentication
basic_headers_sheety = {
    "Authorization": f"Basic {SHEETY_BASIC_AUTH}"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data_sheety = {}
    
    
    def ambil_kota(self):
        response_sheety_post = requests.get(url=URL_SHEETY, headers=basic_headers_sheety)
        response_sheety_post.raise_for_status()
        data = response_sheety_post.json()
        self.data_sheety = data['prices']
        # print(self.data_sheety)
        # ini hasil print data_sheety nya:
        # {'prices': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Frankfurt', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Hong Kong', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Dublin', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}
        return self.data_sheety
    
    
    def masukin_iata_code_ke_spreadsheet(self):
        for kota in self.data_sheety:
            data_yang_mau_dimasukin = {
                "price": {
                    "iataCode": kota['iataCode']
                }
            }      
            response_sheety_put = requests.put(
                url=f"{URL_SHEETY}/{kota['id']}",
                json=data_yang_mau_dimasukin
            )
            response_sheety_put.raise_for_status()
            print(response_sheety_put.text)
