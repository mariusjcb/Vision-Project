#!/usr/bin/env python

from sys import argv
from sys import exit

modes = {
    "-c": "Current Weather", 
    "-f": "Forecast Weather (not yet)"
}

mode = "-c"
city = ""

# parse user params from shell
for i in range(1, len(argv)):
    if argv[i][0] != "-":
        city = city + str(argv[i]) + "+"
    else:
        mode = argv[i]

# check if user entered a city or not
# else: show help
if mode != "-help":
    if city == "" or not mode in modes:
        print "(!) ERROR 1: No city or zip code inserted.\n(!) Use -help to learn more."
        exit()
elif mode == "-help":
    print "\n\
Weather command needs a mode and a city name to return datas.\n\n\
Modes:"
    for (key, value) in modes.iteritems():
        print "\t" + key + ": "+ value
    print "\n\
The city name or zip code is required. (Example 1)\n\
If you are using -f mode. Days of forecast are required. (Example 2)\n\n\
\
EXAMPLE 1: weather -c Bucharest\n\
EXAMPLE 2: weather -f Bucharest 7\n\
    "
    exit()

# if mode is not help and city exists
# remove last "+" from city string
city = city[:-1]

# fetch datas from RestAPI
import WeatherAPI

API_Key = '6c3a7f95e478467fad0130018171904'
WeatherClient = WeatherAPI.Client(API_Key)

if mode == "-c":
    CurrentWeather = WeatherClient.getCurrentWeatherWith(Query=city)
    print "Temperature:", CurrentWeather['current']['temp_c'], "C"  # show temprature in celsius
    print "Humidity:", str(CurrentWeather['current']['humidity']) + "%"  # humidity
    print "Precip:", str(CurrentWeather['current']['precip_mm']) + "mm"  # precip
    print "Wind KM/H:", CurrentWeather['current']['wind_kph']  # show wind

    print "\nTime:", CurrentWeather['location']['localtime']  # local time
    print "City:", str(CurrentWeather['location']['name']) + ", " + str(CurrentWeather['location']['region']) + ", " + str(CurrentWeather['location']['country'])
    print "Lat/Long:", CurrentWeather['location']['lat'], "/", CurrentWeather['location']['lon']  # latitude value
elif mode == "-f":
    print "comming soon\n"