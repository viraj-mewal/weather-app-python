# create a weather app that shows weather of a place

import requests
import json
import os


api = "" # -> insert your api here from weatherapi.com

os.system("cls")
print(f"\t\t WELCOME TO THE WEATHER APP \t\t\n\n")

place = input("Enter name of place :- ")

# Fetching the weather details
print("Fetching......")

place = "%20".join(place.split(" "))
source = f"https://api.weatherapi.com/v1/current.json?key={api}&q={place}&aqi=no"
got = requests.get(source).text
data = json.loads(got)

info = {
    "name": data["location"]["name"],
    "country": data["location"]["country"],
    "time": data["location"]["localtime"],
    "temp": data["current"]["temp_c"],
    "weather": data["current"]["condition"]["text"],
    "wind": data["current"]["wind_kph"],
    "humidity": data["current"]["humidity"]
}

print(f'''\n
Place       :- {info["name"]}
Country     :- {info["country"]}
Time        :- {info["time"]}
Temperature :- {info["temp"]}°C
Weather     :- {info["weather"]}
Wind        :- {info["wind"]} kmph
Humidity    :- {info["humidity"]}''')


