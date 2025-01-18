# pakai pixela api


import requests
import datetime as dt

USERNAME = ""
TOKEN = ""
GRAPH_ID = ""

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

pixela_endpoint = "https://pixe.la/v1/users"

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "page",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# sekarang = dt.datetime(year=2025, month=1, day=17)
sekarang = dt.datetime.now()

# RIBET PAKAI INI, MENDING PAKAI STRFTIME()
# tanggal_hari_ini = str(sekarang.day)
# bulan_ini = str(sekarang.month)
# tahun_ini = str(sekarang.year)

# if len(bulan_ini) < 2:
#     hari_ini = tahun_ini + "0" + bulan_ini + tanggal_hari_ini
# else:
#     hari_ini = tahun_ini + bulan_ini + tanggal_hari_ini

jumlah_hal = input("Udah baca berapa halaman hari ini?: ")

pixel_config = {
    "date": sekarang.strftime("%Y%m%d"),
    "quantity": jumlah_hal,
}

add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# response = requests.post(url=add_pixel_endpoint, json=pixel_config, headers=headers)
# print(response)

put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{sekarang.strftime("%Y%m%d")}"

# response = requests.put(url=put_pixel_endpoint, json={"quantity": jumlah_hal}, headers=headers)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{sekarang.strftime("%Y%m%d")}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)


