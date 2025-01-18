# kebetulan sekarang lagi ujan
MY_LAT = -6.23976000
MY_LON = 106.72741000

# yang cerah, mungkin sekarang jeddah cerah merona
LAT_CERAH = 21.492500
LON_CERAH = 39.177570

openweather_parameters = {
    "lat": LAT_CERAH,
    "lon": LON_CERAH,
    "appid": "masukin id nya",
    # the next 6 timestamps
    "cnt": 6 # ini buat batesin jumlah data yang muncul, dalam hal ini, 6 data terdekat yang muncul
}

import requests

response = requests.get("https://api.openweathermap.org/data/2.5/forecast?", params=openweather_parameters)
response.raise_for_status()
weather_data = response.json()

bakal_hujan = False
for i in range(len(weather_data['list'])):
    if weather_data['list'][i]['weather'][0]['id'] < 700:
        bakal_hujan = True

if bakal_hujan == True:
    print("Hari ini kudu bawa payung")
else:
    print("Hari ini bakal cerah, terserah mau bawa payung atau ga ;)")



# note:
# part sms / wa nya skip dulu
