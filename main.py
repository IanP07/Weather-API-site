from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

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
        data = response.json()
        return {"temperature": data['days'][0]['temp']}
    else:
        return {"error": "unable to find location"}