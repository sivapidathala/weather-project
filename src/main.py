from .config import CITIES
from .weather_client import fetch_weather
from .s3_client import upload_to_s3

def main():
    if not CITIES:
        print("No cities found in .env file")
        return

    print("Fetching weather data...")

    results = []

    for city in CITIES:
        print(f"Getting weather for: {city}")
        data = fetch_weather(city)
        results.append(data)

    print("\nWeather Results:")
    for item in results:
        print(item)

    print("\nUploading to AWS S3...")
    upload_to_s3(results)

if __name__ == "__main__":
    main()
