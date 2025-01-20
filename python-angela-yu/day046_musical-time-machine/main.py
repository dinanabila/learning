import requests
from bs4 import BeautifulSoup

masa = input("Haii yang mau balik ke masa lalu, mau balik ke masa mana? (ketik & enter YYYY-MM-DD):")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(f"https://www.billboard.com/charts/hot-100/{masa}/", headers=header)
# print(response)
data = response.text

soup = BeautifulSoup(data, "html.parser")
# print(soup.prettify())

# ini gagal
# titles = soup.select(selector="h3 #title-of-a-story")

# ini yang bener:
titles = soup.select(selector="li ul li h3")

# print(titles)
semua_judul_lagu = [judul_lagu.getText().strip() for judul_lagu in titles]

# strip() buat ngapusin semua /t/t/t/t/t/t nya, biar bersih judul lagu doang di dalam listnya

# print(semua_judul_lagu)