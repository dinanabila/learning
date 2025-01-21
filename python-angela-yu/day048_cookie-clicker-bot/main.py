from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
lima_menit_kemudian = time.time() + 60 * 5
timeout = time.time() + 5

while True:
    cookie.click()

    # Cek toko setiap lima detik
    if time.time() > timeout:
        # Ambil semua toko
        semua_toko = driver.find_elements(By.CSS_SELECTOR, value='#store div')
        
        # Ambil toko yang udah buka (yang ga punya class "grayed")
        semua_toko_yang_sudah_terbuka = [toko for toko in semua_toko if "grayed" not in toko.get_attribute('class')]
        
        # Klik toko paling bawah yang udah kebuka
        if semua_toko_yang_sudah_terbuka:
            toko_yang_terbuka = semua_toko_yang_sudah_terbuka[-1] # -1 nandain toko terakhir yang diklik
            toko_yang_terbuka.click()
        
        # Reset timeout untuk pengecekan toko di 5 detik selanjutnya
        timeout = time.time() + 5

    # Matikan program setelah lima menit berlalu
    if time.time() > lima_menit_kemudian:
        cookies_per_second = driver.find_element(By.ID, value='cps')
        print(cookies_per_second.text)
        break
