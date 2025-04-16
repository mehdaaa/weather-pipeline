# extract/fetch_weather.py

import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def fetch_weather(lat, lon):
    url = (
        f"https://api.openweathermap.org/data/3.0/onecall"
        f"?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=fr"
    )

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print(f"[ERROR] Failed to fetch weather data, status: {response.status_code}")
        print(response.text)
        raise Exception("API call failed.")

    return response.json()

if __name__ == "__main__":
    lat = 48.1173
    lon = -1.6778

    data = fetch_weather(lat, lon)

    print("[INFO] Données météo actuelles :")
    print(data["current"])