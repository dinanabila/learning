import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# buat raise error dari response pakai method dari module requests nya
response.raise_for_status()

data = response.json()
# print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)