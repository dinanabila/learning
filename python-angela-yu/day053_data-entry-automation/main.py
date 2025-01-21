LINK_GFORM = ""
URL_WEB = "https://appbrewery.github.io/Zillow-Clone/"

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# beautifulsoup untuk scrape data dari web
# selenium untuk otomasi fill gform


# ====== beautifulsoup part =======

response = requests.get(URL_WEB)
data = response.text

soup = BeautifulSoup(data, "lxml")

# test buat dapetin link properti
# link = soup.find(name="a", class_="property-card-link")
# print(link.get("href"))

semua_link_properti = soup.find_all(name="a", class_="property-card-link")
links = [link.get("href") for link in semua_link_properti]

# test buat dapetin harga properti
# harga = soup.find(name="span", class_="PropertyCardWrapper__StyledPriceLine")
# print(int(harga.getText().replace('$', "").replace(',', "").replace('+/mo', "")))
# itu pakai replace soalnya output aslinya $2,895+/mo
# jadi biar bersih, sekalian dijadiin int juga

semua_harga_properti = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
prices = [int(harga.getText().replace('$', "").replace(',', "").replace('+', "").replace('/', "").replace('mo', "").replace('1 bd', "").replace('1bd', "").replace(' ', '')) for harga in semua_harga_properti]

# test buat dapetin alamat properti
# alamat = soup.find(name="address")
# print(alamat.getText().strip())

semua_alamat_properti = soup.find_all(name="address")
addresses = [alamat.getText().strip() for alamat in semua_alamat_properti]


# print(len(prices))
# print(len(addresses))
# print(len(links))
# sip sama semua :D


# ===== selenium part =====

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(LINK_GFORM)
time.sleep(5) # untuk internet lemot loading lama, biar programnya ga hah hoh pas lagi run

# ini gagal, jadi pakai xpath aja biar gampang
# isi_alamat = driver.find_element(By.CLASS_NAME, value="whsOnd zHQkBf")

for i in range(0, len(addresses)):
    isi_alamat = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    isi_alamat.send_keys(addresses[i])

    isi_harga = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    isi_harga.send_keys(prices[i])

    isi_link = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    isi_link.send_keys(links[i])

    tombol = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    tombol.click()

    kirim_jawaban_lain = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    kirim_jawaban_lain.click()