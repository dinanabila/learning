from selenium import webdriver
from selenium.webdriver.common.by import By

# ini biar pop up chrome browser nya tetep kebuka terus
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# price_dolar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')

# print(f"The price is {price_dolar.text}.{price_cents.text}")


search_bar = driver.find_element(By.NAME, value='q')
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

# kalau element ga punya class dan id, pakai css selector, 
# jadi dia ngandelin nama class div yang ngurungnya
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# kalau cara di atas ga ada lagi yang mempan, a.k.a ga ada keunikan dari yang mau kita ambil,
# solusinya pakai XPath

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# buat nutup pop up programmatically
# driver.close() --> ini buat nutup 1 tab doang
# driver.quit() --> ini beneran nutup browser secara keseluruhan

driver.quit()

