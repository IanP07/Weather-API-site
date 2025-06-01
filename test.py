import time
import requests

location = "france"
key = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key=UWG46QHN2MF3V8VYKZJXC49CW&contentType=json"
response = requests.get(key)
data = response.json()

local = time.localtime().tm_hour

print(data['days'][0]['hours'][local]['temp'])