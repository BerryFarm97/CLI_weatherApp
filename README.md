# CLI Weather App

This is a Python command-line weather app I built to practice working with APIs, user input, error handling, and organizing a project into multiple files.

The app lets you search for a city, choose the correct location from a list of matches, and view current weather data like temperature, humidity, precipitation, and wind speed.

## Features

- Search for a city by name
- Choose from multiple matching locations
- View current temperature, humidity, precipitation, and wind speed
- Search again without restarting the app
- Handles invalid city searches
- Handles API/network issues without crashing
- Uses live weather data from the Open-Meteo API
- Organized into separate files for API requests, display logic, and app flow

## Tech Used

- Python
- Requests
- Open-Meteo Geocoding API
- Open-Meteo Forecast API
- Git and GitHub

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/BerryFarm97/CLI_weatherApp.git
```

2. Move into the project folder:

```bash
cd CLI_weatherApp
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the program:

```bash
python main.py
```

## What I Learned

This project helped me get more comfortable with building a real Python program instead of just writing everything in one file.

I practiced making API requests, working with JSON data, validating user input, handling errors, and breaking code into smaller functions. I also refactored the project into multiple files so the API logic, display logic, and main program flow are easier to understand and maintain.

## Future Improvements

- Add automated tests with pytest
- Save recent searches
- Add favorite cities
- Show a multi-day forecast
- Turn the app into a simple Flask or FastAPI web app
