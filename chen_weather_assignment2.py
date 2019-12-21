import json
import sys
import urllib.parse
from urllib.request import urlretrieve

city = sys.argv[1].split(",")
city = urllib.parse.quote(str(city))
url_basis = "http://api.weatherstack.com/current?access_key=a9b3b3c03662da4b3e5f21706695d616&query="
if len(sys.argv) < 3 or sys.argv[2] == "-c":
    url_query = (url_basis + str(city))
    temp_unit = "Celsius"

elif sys.argv[2] == "-f":
    url_query = (url_basis + city + "&units=f")
    temp_unit = "Fahrenheit"

with urllib.request.urlopen(url_query) as url:
    data = json.loads(url.read().decode())

try:
    dict_location = data['location']
    dict_location_city = dict_location.get('name', {})
    dict_temp = (data['current']).get('temperature', {})
    print("The weather in " + dict_location_city.capitalize() + " today is " + str(dict_temp) + " degrees " + temp_unit + ".")
except KeyError:
    print("The city you're looking for does not exist in our records, how about searching for Milan, Berlin or Dublin instead?")



