import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "lxml")

semua_a = soup.select(selector = ".titleline a")
# print(selector_a)

for soup in semua_a:
    print(soup.getText())
    print(soup.get("href"))