import requests

def get_geo_data(city):
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=5&language=en&format=json"

    try:
        response = requests.get(geocoding_url, timeout=10)
        response.raise_for_status()
        geo_data = response.json()
        result = geo_data.get('results')
        return result
    except requests.exceptions.RequestException:
        return None

def get_weather_data(latitude, longitude):
    forecast_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch"
    try:
        forecast_response = requests.get(forecast_url, timeout=10)
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()
        return forecast_data
    except requests.exceptions.RequestException:
        return None