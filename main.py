# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# pseudocode
# Use the requests module to fetch weather data from the Open Weather API.
# Prompt user for their location city name? postcode?
# Use the input to construct the API request URL (same as last course)
# Fetch the weather data for location.
# parse JSON from the API response, such as temperature? rain? sunny? Picnic Weather!!
# Present the weather forecast to user
# Write the final results to a file - need to hand this in

# 1. getting the data
import requests
import json
import api_keys

api_key = api_keys.OPEN_WEATHER_API_KEY

#help source:  https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/

def get_weather_forecast(location):
    # Construct URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

    # Fetch/json format
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print("Failed to fetch weather data!")
        return None

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
