STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

import requests
import datetime as dt

parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":"INIY9YRSCCS87HKQ",
    "outputsize": "compact"
}

response = requests.get("https://www.alphavantage.co/query?", params=parameters)
response.raise_for_status()

data_tesla = response.json()
print(data_tesla["Time Series (Daily)"]["2025-01-17"]['4. close'])

sekarang = dt.datetime.now().date()

# RIBET KALAU MANIPULASI STRING GINI
# bulan_ini = sekarang.month
# tahun_ini = sekarang.year

# tanggal_kemarin = f"{tahun_ini}-{bulan_ini}-{tanggal_sekarang - 1}"
# tanggal_kemarin_lusa = f"{tahun_ini}-{bulan_ini}-{tanggal_sekarang - 2}"
# print(tanggal_kemarin)
# print(tanggal_kemarin_lusa)

# PAKE TIMEDELTA AJA
selang_sehari = dt.timedelta(days=1) 
kemarin = sekarang - selang_sehari 
kemarin_lusa = kemarin - selang_sehari

print(kemarin)
print(kemarin_lusa)

harga_kemarin = float(data_tesla["Time Series (Daily)"][f"{kemarin}"]['4. close'])
harga_kemarin_lusa = float(data_tesla["Time Series (Daily)"][f"{kemarin_lusa}"]['4. close'])

persentase = (abs(harga_kemarin - harga_kemarin_lusa) / harga_kemarin_lusa) * 100
print(persentase)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if persentase >= 1: # INI HARUSNYA 5, TAPI JADIIN 1 AJA BIAR BISA DITES
    # q=Tesla&from=2025-01-18&sortBy=popularity&apiKey=API_KEY
    parameters_2 = {
        "q": COMPANY_NAME,
        "from": kemarin_lusa,
        "sortBy": "popularity",
        "apiKey": "eab9e35777da493e964486429c67819a"
    }
    response_2 = requests.get("https://newsapi.org/v2/everything?", params=parameters_2)
    data_berita = response_2.json()
    print("INI BERITANYA!")
    for i in range(3):
        print(data_berita["articles"][i]['url'])

 



## ===========[SKIP]============ STEP 3: Use https://www.twilio.com  ===========[SKIP]============
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

