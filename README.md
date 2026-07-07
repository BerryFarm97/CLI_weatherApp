# CLI Weather App

A Python command-line weather app that lets users search for a city, choose the correct location, and view current weather data using the Open-Meteo API.

## Features

* Search for a city by name
* Choose from multiple matching locations
* View current temperature, humidity, precipitation, and wind speed
* Search again without restarting the program
* Uses live weather data from the Open-Meteo API

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

While building this project, I practiced working with APIs, handling JSON data, using user input, building loops, and organizing a command-line Python program.

## Future Improvements

* Add better error handling for failed API requests
* Clean up the code into smaller functions
* Add tests with pytest
* Save recent searches
* Add a simple GUI or web version later
