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
        print("Something went wrong. Please try again later")
        return None

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

def ask_to_continue():
    while True:
        choice = input("Search another city?(y/n): ").strip().lower()
        if choice in ('y', 'yes'):
            return True
        elif choice in ('n', 'no'):
            return False
        else:
            print("Invalid selection, please try again")


def main():
    getting_weather = True
    print("Welcome to my weather app.")

    while getting_weather:

        weather_results = True
        city_name = input("What city?: ")
        possible_matches = get_geo_data(city_name)
        if possible_matches is None:
            print("Something went wrong. Please try again later.")
            break

        if not possible_matches:
            print("Invalid entry. Please enter a valid city.")
            continue

        displayed_matches = possible_matches[:5]

        while weather_results:
            try:

                display_possible_matches(displayed_matches)

                correct_city = int(input("Which city is correct?: "))
                if len(displayed_matches) >= correct_city > 0:
                    selected_city = displayed_matches[correct_city - 1]
                    longitude = selected_city.get('longitude')
                    latitude = selected_city.get('latitude')

                    forecast_data = get_weather_data(latitude, longitude)
                    if forecast_data is None:
                        print("Weather could not be loaded. Please try again later.")
                        break
                    else:
                        weather_details = extract_weather_data(forecast_data)
                        display_weather_report(selected_city, weather_details)

                    search_again = ask_to_continue()
                    if search_again:
                        break
                    else:
                        getting_weather = False
                        weather_results = False
                    break

                elif correct_city == 6:
                    break
                elif correct_city == 7:
                    getting_weather = False
                    break
                else:
                    print("Invalid entry. Please enter a valid option.")
                    continue

            except ValueError:
                print("Invalid option, please try again")






if __name__ == "__main__":
    main()