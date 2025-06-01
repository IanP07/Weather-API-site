from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  
    allow_credentials=True,
    allow_methods=["GET"],  
    allow_headers=["*"],  
)


@app.get("/")
def return_data(location: str):
    key = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key=UWG46QHN2MF3V8VYKZJXC49CW&contentType=json"
    response = requests.get(key)

    if response.status_code == 200:
        # Grabbing hourly data
        data = response.json()
        hourly = data['days'][0]['hours']
        hourly_temp = []
        for hour in hourly:
            hourly_temp.append(hour['temp'])
        
        # Calculating current time
        local_time = time.localtime().tm_hour
        local_current_weather = data['days'][0]['hours'][local_time]['temp']

        return {"hourly": hourly_temp, "current": local_current_weather}
    else:
        return {"error": "unable to find location"}