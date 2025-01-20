from bs4 import BeautifulSoup

with open("day045/parsing-exercise/website.html") as file:
    html_file = file.read()
    
soup = BeautifulSoup(html_file, 'html.parser')
print(soup.prettify())

print(soup.title.string)

print(soup.a)

print(soup.find_all("p"))

all_anchor_tags = soup.find_all("a")

for tag in all_anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading.string)


section_heading = soup.find(name="h3", class_="heading") # attr class di bs pakai _

print(section_heading)


# ambil specific anchor tag
# caranya amati, apa yang unik dari apa yang mau kita ambil?
# mungkin dia terkurung di antara div dengan nama id tertentu, atau class, atau mungkin
# bisa juga terkurung di antara list

# pakai select
company_url = soup.select_one(selector = "p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)