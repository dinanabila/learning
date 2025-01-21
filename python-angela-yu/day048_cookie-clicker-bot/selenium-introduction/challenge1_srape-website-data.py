from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

semua_nama_event = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')

# for event in semua_nama_event:
#     print(event.text)

semua_tanggal_event = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li time')

# for tanggal in semua_tanggal_event:
#     print(tanggal.text)

semua_event = {}

for i in range(len(semua_tanggal_event)):
    semua_event[i] = {
        "time": semua_tanggal_event[i].text,
        "name": semua_nama_event[i].text,
    }

print(semua_event)
driver.quit()


