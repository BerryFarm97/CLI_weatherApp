import requests


def get_geo_data(city):
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=5&language=en&format=json"
    response = requests.get(geocoding_url, timeout=10)
    geo_data = response.json()
    result = geo_data.get('results')
    return result

def get_weather_data(latitude, longitude):
    forecast_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch"
    forecast_response = requests.get(forecast_url, timeout=10)
    forecast_data = forecast_response.json()
    return forecast_data

def display_possible_matches(displayed_matches):
    for number, matches in enumerate(displayed_matches, start=1):
        name = matches.get('name', 'Unknown')
        state = matches.get('admin1', 'Unknown')
        print(f"{number}. {name},{state}")
    print("6. New Search")
    print("7.Exit")

def display_weather_report(selected_city, forecast_data):
    current_forecast = forecast_data['current']
    forecast_measurements = forecast_data['current_units']
    name = selected_city.get('name')
    state = selected_city.get('admin1')
    humidity = current_forecast.get('relative_humidity_2m', 'Unknown')
    temp = current_forecast.get('temperature_2m', 'Unknown')
    precipitation = current_forecast.get('precipitation', 'Unknown')
    wind_spd = current_forecast.get('wind_speed_10m', 'Unknown')
    temp_symbol = forecast_measurements.get('temperature_2m', ' ')
    humidity_symbol = forecast_measurements.get('relative_humidity_2m', ' ')
    precipitation_symbol = forecast_measurements.get('precipitation', ' ')
    wind_spd_symbol = forecast_measurements.get('wind_speed_10m', ' ')

    print(f"\n\n{name},{state}\n   Current Temperature:{temp}{temp_symbol}\n   Current Humidity:{humidity}{humidity_symbol}\n   Current Precipitation: {precipitation} {precipitation_symbol}\n   Current Wind Speed: {wind_spd} {wind_spd_symbol}")

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

    while getting_weather:

        weather_results = True
        city_name = input("What city?: ")
        possible_matches = get_geo_data(city_name)
        if not possible_matches:
            print("Invalid entry. Please enter a  valid city.")
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

                    display_weather_report(selected_city, forecast_data)

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