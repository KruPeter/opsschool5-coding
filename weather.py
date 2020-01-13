#Coding assignment  number 3:
import click
import json
import urllib.parse
from urllib.request import urlretrieve


@click.command()
@click.option('--token', help='Your API access token')
@click.option('--city', help='the city or cities you would like to check')
@click.option('--T', 'temperature', type=click.Choice(['Celsius', 'Fahrenheit']), default='Celsius',
              help='the temperature unit you would like to check')
def weather_function(token, city, temperature):
    if temperature == 'Fahrenheit':
        temperature_unit = 'f'
    else:
        temperature_unit = 'm'
    cities = city.split(',')

    for city in cities:
        city = urllib.parse.quote(str(city))
        url_query = ('http://api.weatherstack.com/current?access_key={}&query={}&units={}'.format(token, city,
                                                                                                  temperature_unit))

        with urllib.request.urlopen(url_query) as url:
            data = json.loads(url.read().decode())

        try:
            dict_location = data['location']
            dict_location_city = dict_location.get('name', {})
            dict_temperature = (data['current']).get('temperature', {})
            print("The weather in " + dict_location_city.capitalize() + " today is " + str(dict_temperature) +
                  "degrees.")
        except KeyError:
            if data['error']['code'] == 101:
                print("The token you've entered is invalid, please try again")
            else:
                print(
                    "The city you're looking for does not exist in our records, how about searching for Milan, "
                    "Berlin or Dublin instead?")


if __name__ == '__main__':
    weather_function()