from weather_api import get_weather_data
from weather_api import get_geo_data
from weather_display import display_possible_matches
from weather_display import extract_weather_data
from weather_display import display_weather_report


def ask_to_continue():
    while True:
        choice = input("Search another city?(y/n): ").strip().lower()
        if choice in ('y', 'yes'):
            return True
        elif choice in ('n', 'no'):
            return False
        else:
            print("Invalid selection, please try again")

def get_city_choice(displayed_matches):
    while True:
        display_possible_matches(displayed_matches)

        try:
            choice = int(input("Which city is correct?: "))

            if 1 <= choice <= len(displayed_matches):
                return choice
            elif choice == 6:
                return choice
            elif choice == 7:
                return choice
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid entry. Please try again.")

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

            correct_city = get_city_choice(displayed_matches)

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








if __name__ == "__main__":
    main()