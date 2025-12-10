import requests
from datetime import datetime
from .config import OPENWEATHER_API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city):
    """Fetch weather for one city."""
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        return {
            "city": city,
            "timestamp": datetime.utcnow().isoformat(),
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"]
        }

    except Exception as e:
        return {
            "city": city,
            "error": str(e)
        }
