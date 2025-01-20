import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
data = response.text

soup = BeautifulSoup(data, "html.parser")
# print(soup.prettify())

semua_h3 = soup.find_all(name="h3", class_="title")

semua_judul = []

for soup in semua_h3:
    judul = soup.getText()
    semua_judul.append(judul)

# print(semua_judul)

# tadinya kan di list nya masih descending (100, 99, dst)
# buat ngubah jadi ascending (1, 2, dst),
# kita pakai reverse()
semua_judul.reverse()

# print("\n\nList judul setelah di-reverse()\n\n")
# print(semua_judul)

# sekarang simpan ke idenobar.txt
with open("day045_scraping-movie-list/scrape-movie-list/idenobar.txt", "w", encoding="utf-8") as file:
    for judul in semua_judul:
        file.write(judul + "\n")

# ket: encoding="utf-8" biar ga kena UnicodeEncodeError: 'charmap' codec can't encode characters in position 1299-1300: character maps to <undefined>
