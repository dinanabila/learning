import requests
from bs4 import BeautifulSoup
import lxml

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(URL, headers=header)
data = response.text

soup = BeautifulSoup(data, "lxml")
# harga = soup.find(name="p", class_="a-spacing-none a-text-left a-size-mini twisterSwatchPrice")

# harga = soup.select_one(selector="li span div span span span button div div div div span p")
# print(harga)


# belum bejo
# hasilnya none D:
