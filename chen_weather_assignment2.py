import json
import sys
import urllib.parse
from urllib.request import urlretrieve

access_key = "a9b3b3c03662da4b3e5f21706695d616"
url_basis = "http://api.weatherstack.com/current?access_key="

if len(sys.argv) > 1:
    cities = sys.argv[1].split(",")
else:
    cities = ""
    print("Oops! no city was requested, please add a city to your request and try again!")

if len(sys.argv) < 3 or sys.argv[2] == "-c":
    temperature_unit = "Celsius"
    units = ""

elif sys.argv[2] == "-f":
    temperature_unit = "Fahrenheit"
    units = "&units=f"

elif sys.argv[2] != "-f" or "-c":
    print("Tip: add '-f' or '-c' to search for the temperature in Fahrenheit or Celsius degrees, respectively")
    temperature_unit = "Celsius"
    units = ""

for city in cities:
    city = urllib.parse.quote(str(city))
    url_query = (url_basis + access_key + "&query=" + city + units)

    with urllib.request.urlopen(url_query) as url:
        data = json.loads(url.read().decode())

    try:
        dict_location = data['location']
        dict_location_city = dict_location.get('name', {})
        dict_temperature = (data['current']).get('temperature', {})
        print("The weather in " + dict_location_city.capitalize() + " today is " + str(dict_temperature) + " degrees " + temperature_unit + ".")
    except KeyError:
        print("The city you're looking for does not exist in our records, how about searching for Milan, Berlin or Dublin instead?")
