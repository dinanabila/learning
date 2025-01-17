import requests
import datetime as dt
import smtplib

MY_LAT = -6.905977
MY_LONG = 107.613144
my_email = "dari@gmail.com"
password = "eherh3452345"
TOLERANSI = 5


response = requests.get(url="http://api.open-notify.org/iss-now.json")

# buat raise error dari response pakai method dari module requests nya
response.raise_for_status()

data_iss = response.json()
# print(data)

iss_longitude = float(data_iss["iss_position"]["longitude"])
iss_latitude = float(data_iss["iss_position"]["latitude"])

iss_position = (iss_longitude, iss_latitude)
print(f"Posisi ISS: {iss_position}")

posisi_acu = (MY_LONG, MY_LAT)
print(f"Posisi acu: {posisi_acu}")

# print(iss_position_tambah_5)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data_sun_kita = response.json()

# ambil jam nya doang, tanggalnya buang
# pakai method split nya string
# 1 itu karena kita butuh split kan lagi data di list index 1, si jam nya
# janlup + 7 % 4, soalnya defaultnya masih dalam UTC, bukan WIB
sunrise = int((int(data_sun_kita["results"]["sunrise"].split("T")[1].split(":")[0]) + 7) % 24)
sunset = int((int(data_sun_kita["results"]["sunset"].split("T")[1].split(":")[0]) + 7) % 24)

# print(type(sunrise))
sekarang = dt.datetime.now()

print(f"Sekarang jam: {sekarang.hour}")
print(f"Matahari terbit jam: {sunrise}") 
print(f"Matahari terbenam jam: {sunset}")


# kalau posisi iss udah deket posisi acu, 
# dan kalau gelap aka matahari udah terbenam,
# berarti kirim email ke aku buat liat iss nya lewat di langit
# bonus challenge: bikin kodenya jalan setiap 60 detik

# # tester
# # ini range waktu yang diperlukan: 
# for i in range(0,24):
#     if i not in range(sunrise, sunset):
#         print(i)


iss_udah_deket = (MY_LAT - TOLERANSI <= iss_latitude <= MY_LAT + TOLERANSI) and (MY_LONG - TOLERANSI <= iss_longitude <= MY_LONG + TOLERANSI)

langit_gelap = sekarang.hour not in range(sunrise, sunset)

if iss_udah_deket and langit_gelap:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject: ISS LEWAT!! AYO KELUAR SEKARANG, LIAT LANGIT\n\nLiat langit sekarang!!"
        )
else:
    print("\nyah, iss nya belum lewat")