import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# Cities list: "Hyderabad,Chennai,Mumbai"
cities_str = os.getenv("CITIES")
if cities_str:
    CITIES = [city.strip() for city in cities_str.split(",")]
else:
    CITIES = []
