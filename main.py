# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Dear Instructor, my api key was stored in a .gitignore file. You can sign up to open weather and have one yourself at https://openweathermap.org/api, or please contact me for my API key. Thank you.

# Pseudocode
# Use the requests module to fetch weather data from the Open Weather API.
# Prompt user for their location city name? postcode?
# Use the input to construct the API request URL (same as last course)
# Fetch the weather data for location.
# parse JSON from the API response, such as temperature? rain? sunny? Picnic Weather!!
# Present the weather forecast to user
# Decide if weather conditions are suitable for a picnic
# Write the final results to a file - need to hand this in
# use tomtom api - as user 'do you want a picnic suggestion?' loop through a fetch and then slice for these criteria

# 1. getting the data
import requests
import json
import api_keys

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
        print("Failed to fetch weather data! - Please check the name of your city.")
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


def determine_picnic_weather(temperature, wind_speed, weather_description):
    # need to say if it's picnic weather based on the conditions
    if 20 <= temperature <= 36 and wind_speed < 5 and 'clear' or 'few clouds' or 'scattered clouds' in weather_description.lower():
        return "It is picnic weather! Grab your blanket and let's eat!"
    elif 15 <= temperature <= 25 and 'cloudy' in weather_description.lower():
        return "It may be picnic weather, take a brolly just in case!"
    else:
        return "Eat that picnic in your living room today - stay inside!"

# more help source: https://www.google.com/search?client=safari&rls=en&q=build+a+weather+app+console+python&ie=UTF-8&oe=UTF-8#fpstate=ive&vld=cid:c22b2efc,vid:Y84MGU_ZL18,st:0
def present_forecast(forecast_data):
    if forecast_data:
        # Parse data (example above) - variable for each part of the description that makes it picnic weather
        temperature = forecast_data['main']['temp']
        weather_description = forecast_data['weather'][0]['description']
        wind_speed = forecast_data['wind']['speed']

        # picnic weather -  calling the determine_picnic_weather function and passing three args
        picnic_message = determine_picnic_weather(temperature, wind_speed, weather_description)

        # print conditions and if it is picnic weather!!
        print(f"The current temperature is {temperature}°C with {weather_description}.")
        print(f"The current wind speed is {wind_speed} m/s.")
        print(picnic_message)


def main():
    # Prompt for location (need to look at accuracy/specificity of location her - use reverse geocode?
    # 'input' is an inbuilt function
    location = input("Enter your city name: ")

    # Call weather forecast function with location as an argument. Forecast is fetched after user input.
    forecast_data = get_weather_forecast(location)

    # Present forecast function recall with argument. Prints results to console.
    present_forecast(forecast_data)

    # Write results to a file syntax - need to write to file


print("API Key:", api_key)

if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
