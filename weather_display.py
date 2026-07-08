

def display_possible_matches(displayed_matches):
    for number, matches in enumerate(displayed_matches, start=1):
        name = matches.get('name', 'Unknown')
        state = matches.get('admin1', 'Unknown')
        print(f"{number}. {name},{state}")
    print("6. New Search")
    print("7.Exit")

def extract_weather_data(forecast_data):
    current_forecast = forecast_data['current']
    forecast_measurements = forecast_data['current_units']

    weather_details = {
        "temp": current_forecast.get("temperature_2m", "Unknown"),
        "humidity": current_forecast.get("relative_humidity_2m", "Unknown"),
        "precipitation": current_forecast.get("precipitation", "Unknown"),
        "wind_spd": current_forecast.get("wind_speed_10m", "Unknown"),
        "temp_symbol": forecast_measurements.get("temperature_2m", " "),
        "humidity_symbol": forecast_measurements.get("relative_humidity_2m", " "),
        "precipitation_symbol": forecast_measurements.get("precipitation", " "),
        "wind_spd_symbol": forecast_measurements.get("wind_speed_10m", " ")
    }
    return weather_details

def display_weather_report(selected_city, weather_details):
    name = selected_city.get('name')
    state = selected_city.get('admin1')

    print(f"\n\n{name},{state}\n   Current Temperature:{weather_details['temp']}{weather_details['temp_symbol']}\n   Current Humidity:{weather_details['humidity']}{weather_details['humidity_symbol']}\n   Current Precipitation: {weather_details['precipitation']} {weather_details['precipitation_symbol']}\n   Current Wind Speed: {weather_details['wind_spd']} {weather_details['wind_spd_symbol']}")