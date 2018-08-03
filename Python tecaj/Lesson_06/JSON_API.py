import json
import urllib.request as urllib2
"""
with open("people.json") as file:
    data = json.load(file)

for user in data:
    print(user)
    print(user["id"], ":", user["first_name"], user["last_name"])
    print(user["email"])

file.close()
"""

# b7013fc7ec2ec7fc5bd3f16efef08d76
weather_URL = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&units=metric&appid=b7013fc7ec2ec7fc5bd3f16efef08d76"
data = urllib2.urlopen(weather_URL).read()
weather_data = json.loads(data)

print(weather_data["main"], weather_data["main"]["temp"])