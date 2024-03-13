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
# This is my additional module
import api_keys

# I worked out how to get these into a gitignore file after lots of mistakes!
# I can send you the api keys if requited or they are available free from
# https://openweathermap.org/appid
# https://developer.tomtom.com/free-maps-api
api_key_open_weather = api_keys.OPEN_WEATHER_API_KEY
api_key_tom_tom = api_keys.TOM_TOM_API_KEY


# help source:  https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/

def get_weather_forecast(location):
    # Construct URL
    # test in browser to view what is returned
    # need to add "&units=metric" to get in degrees c
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key_open_weather}&units=metric"

    # Fetch/json format
    response = requests.get(url)
    # I looked up about status codes
    # https://www.moesif.com/blog/technical/monitoring/10-Error-Status-Codes-When-Building-APIs-For-The-First-Time-And-How-To-Fix-Them/
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print("Failed to fetch weather data! - Please check the name of your city or country.")
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

def get_POI(location, country):
    # Constructs URL
    # I tested in browser to view what is returned
    # This took a lot of trial and error and api testing.
    # Ideally I wanted an api that returned parks or green spaces but I could only find an american one.
    # Spent quite a lot of time searching so settled on points of interest.
    # Tried a lot of keywords when parsing, any alterations seemed to return only businesses!
    # After testing, options for a clean response are: 1. Blackpool, UK 2. Cardiff, Wales 3. Bude, UK
    # I have used tomtom before and managed to get the city and country to work eventually!
    url = f"https://api.tomtom.com/search/2/poiSearch/{location},{country}.json?key={api_key_tom_tom}"

    # Fetch/json format
    response = requests.get(url)
    if response.status_code == 200:
        # Return parsed data
        return json.loads(response.text)
    else:
        print("Failed to fetch picnic places! - Please check the name of your city.")
        return None

def determine_picnic_weather(temperature, wind_speed, weather_description):
    # Need to say if it's picnic weather based on the conditions
    if 20 <= temperature <= 36 and wind_speed < 5 and 'clear' or 'broken' or 'scattered' or 'light' in weather_description.lower():
        return "It is picnic weather! Grab your blanket and let's eat!"
    elif 15 <= temperature <= 25 and wind_speed < 5 and 'clouds' in weather_description.lower():
        return "It may be picnic weather, take a brolly just in case!"
    else:
        return "Eat that picnic in your living room today - stay inside!"

# More help source:
# https://www.google.com/search?client=safari&rls=en&q=build+a+weather+app+console+python&ie=UTF-8&oe=UTF-8#fpstate=ive&vld=cid:c22b2efc,vid:Y84MGU_ZL18,st:0
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

        # This took me a long time.
        # I had to remove cloud descriptions because there were too many variables.


def main():
    # Prompt for location (need to look at accuracy/specificity of location her - use reverse geocode?
    # 'input' is an inbuilt function
    location = input("Enter your town name: ")
    country = input("Enter your country name: ")


    # Call weather forecast function with location as an argument.
    # Forecast is fetched after user input.
    forecast_data = get_weather_forecast(location)

    # Present forecast function recall with argument. Prints results to console.
    present_forecast(forecast_data)

    # Prompt for poi - is this the best way to do this?
    input("Would you like a picnic spot suggestion (point of interest) for now or the future? yes/no").lower()

    poi_data = get_POI(location, country)

    # Prints POI data
    # if poi_data:
    #     print("Points of Interest data:")
    #     print(poi_data)

    if poi_data:
        poi_list = poi_data['results']
        # While loop iterates over results.
        # Adds 1 each time to display the next in list that is IMPORTANT TOURIST ATTRACTION
        # Variable
        i = 0
        # Will iterate as long as variable is less than the list of pois
        while i < len(poi_list):
            # Retrieves next element and stores it
            poi = poi_list[i]
            # https://www.w3schools.com/python/python_while_loops.asp
            #
            # Parse returned data
            if 'IMPORTANT_TOURIST_ATTRACTION' in poi['poi']['classifications'][0]['code']:
                name = poi['poi']['name']
                postal_code = poi['address']['postalCode'][:3]  # Slicin' first three characters of the post code
                print(f"Name: {name}, Postal Code: {postal_code}")
                choice = input("Do you want to see another point of interest? (yes/no): ")
                # Ensures lower case - built-in function
                if choice.lower() == 'no':
                    break
            # Adds one/ increments until end of list
            i += 1
        else:
            print("No important tourist attractions found.")
    else:
        print("No data available for the given location.")

# Write results to a file syntax - need to write to file

# Variable for file
input_file_name = "main.py"

# Output file exports to here
output_file_name = "exported_code.py"

# Open the input file for reading using context manager
with open(input_file_name, 'r') as input_file:
    # Reads the input file
    code = input_file.read()

# Add indentation to the code from web stack overflow
# old files and new files - GIT replaces the names with _old and _new!! Very strange to me!
indented_code = "\t" + code.replace("\n", "\n\t")

# Lesson code to write whole file to the output file
with open(output_file_name, 'w') as output_file:
    output_file.write(indented_code)

print(f"Code exported with proper indentation to {output_file_name}")



print("API Key:", api_key_open_weather)
print("API Key tomtom:", api_key_tom_tom)

if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
