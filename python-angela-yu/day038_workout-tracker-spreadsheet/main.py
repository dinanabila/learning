APP_ID = ""
API_KEY = ""
SHEETY_BASIC_AUTH = ""
URL_SHEETY = ""

import requests
import datetime as dt

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

udah_exercise_apa = input("Udah exercise apa hari ini?: ")
# username=YourApiUsername&secret=YourUrlEncodedSecret
parameters = {
    "query": udah_exercise_apa
}

# nyari kemana-mana di docs, gatau nya ada di dalam tabel info link api nya
# https://docx.syndigo.com/developers/docs/natural-language-for-exercise
response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise?", json=parameters, headers=headers)
response.raise_for_status()
data = response.json()
print(data)

sekarang = dt.datetime.now()
jam = sekarang.strftime('%X') # X biar ga ada second milisecond nya
tanggal = sekarang.date().strftime('%d/%m/%Y')

isi_spreadsheet = {
    "workout": {
        "date": tanggal,
        "time": jam,
        "exercise": (data["exercises"][0]["user_input"]).title(),
        "duration": data["exercises"][0]["duration_min"],
        "calories": data["exercises"][0]["nf_calories"],
    }
}

# Basic Sheety Autentication
basic_headers_sheety = {
    "Authorization": f"Basic {SHEETY_BASIC_AUTH}"
}

response_sheety_post = requests.post(url=URL_SHEETY, json=isi_spreadsheet, headers=basic_headers_sheety)



# ====STEP 6 SKIP====