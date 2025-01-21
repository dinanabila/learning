from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value='fName')
last_name = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')
tombol_signup = driver.find_element(By.CSS_SELECTOR, value='form button')

first_name.send_keys("Ai")
last_name.send_keys("Hoshino")
email.send_keys("aihoshino@idol.com")
tombol_signup.click()
