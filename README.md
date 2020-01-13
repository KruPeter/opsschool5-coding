# opsschool5-coding

Assignment #1:

Given the input:
https://github.com/ops-school/opsschool4-coding/blob/master/hw.json
Which contains names paired with their ages, and the bucket ranges (age ranges).

for example:
{“ppl_names”: {
“arie”: 35, “david”: 99},
“buckets”: [11, 22, 40]}
0-11, 11-22, 22-40, 40-100

And turn the input in to a YAML:
22-40:
arie
40-100:
david

Notes:
1. condition to enter the bucket is being equal or larger than the lower number and smaller of the higher number.
2. you can assume that the lowest limit for age is 0 and the highest is the maximum age +1.


Plan:
1. import the json file to python
2. sort the list by the ages
3. calculate the higher limit -  what's the maximum age and add 1 to limit
4. create the buckets and name them
5. sort the names into the buckets created
6. turn the output into  YAML file
7. done

#############################################################################################################

Assignment #2:
`python my_weather.py dublin`

1. Should print the following to the console:
“The weather in Dublin today 5 celsius.”

2. When given either a “-f” or “-c” flag after the city name - should print
either Celsius or Fahrenheit. For example:
`python my_weather.py paris -f`
Will produce this:
“The weather in Paris today 32 Fahrenheit.”

3. If city name is not found:
http://api.weatherstack.com/current?access_key=KEY&query=lalalala
Print out an error that the city does not exists and offer other possible
cities (a few cities not really important which)

4. Adjust the script to be able to get multiple cities:
`python my_weather.py dublin,london,rome`
“The weather in Dublin today 5 Celsius.”
“The weather in London today 4 Celsius.”
“The weather in Rome today 9 Celsius.”
