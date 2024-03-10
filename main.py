# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# pseudocode
# Use the requests module to fetch weather data from the Open Weather API.
# Prompt user for their location city name? postcode?
# Use the input to construct the API request URL (same as last course)
# Fetch the weather data for location.
# parse JSON from the API response, such as temperature? rain? sunny? Picnic Weather!!
# Present the weather forecast to user
# Decide if weather conditions are suitable for a picnic
# Write the final results to a file - need to hand this in

# 1. getting the data
import requests
import json
import api_keys
from walkthrough import present_forecast

api_key = api_keys.OPEN_WEATHER_API_KEY


# help source:  https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/

def get_weather_forecast(location):
    # Construct URL
    # test in browser to view what is returned
    # need to add "&units=metric" to get in degrees c
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    # Fetch/json format
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print("Failed to fetch weather data!")
        return None

    # Returned data - need to parse
    # {"coord": {"lon": -2.0309, "lat": 52.6904},
    #  "weather": [{"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04d"}], "base": "stations",
    #  "main": {"temp": 280.42, "feels_like": 278.6, "temp_min": 279.81, "temp_max": 281.27, "pressure": 996,
    #           "humidity": 96}, "visibility": 10000, "wind": {"speed": 2.68, "deg": 92, "gust": 4.47},
    #  "clouds": {"all": 100}, "dt": 1710070099,
    #  "sys": {"type": 2, "id": 2002946, "country": "GB", "sunrise": 1710052417, "sunset": 1710093794}, "timezone": 0,
    #  "id": 2653883, "name": "Cannock", "cod": 200}
    # parse help source: https://brightdata.com/blog/how-tos/parse-json-data-with-python


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
