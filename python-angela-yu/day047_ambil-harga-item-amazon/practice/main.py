import requests
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(URL)
data = response.text

soup = BeautifulSoup(data, "lxml")

harga = soup.find(name="p", class_="a-spacing-none a-text-left a-size-mini twisterSwatchPrice")

print(harga.getText().strip())



