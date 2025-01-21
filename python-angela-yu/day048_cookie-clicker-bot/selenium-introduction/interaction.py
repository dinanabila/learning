from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# jumlah_artikel = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')

# print(jumlah_artikel.text)

# Nyari element berdasarkan text di antara <a></a>
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()


# Nyari element "Search" <input> by name
tombol_search = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a')
search = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")
tombol_search.click()
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()