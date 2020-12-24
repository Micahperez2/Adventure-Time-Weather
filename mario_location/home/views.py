from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.geoip2 import GeoIP2
import requests
from datetime import date
import json
from home.models import Post

# Create your views here.
def home(request):
    # Gets openweathermap API
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a3f2b06fd38a9b5637604acff1d5c54f'
    g = GeoIP2()
    #request IP address from User
    ip = request.META.get('REMOTE_ADDR', None)
    #ip Used for Testing Commented out Below
    #ip = '35.245.219.70'
    if ip:
        city = g.city(ip)['city']
    else:
        city = 'Chico' # default city

    if str(city) == 'None':
        city = 'Chico' # default city

    # Lookups JSON from API Data with City Name Derived from IP
    city_weather = requests.get(url.format(city)).json()
    today = str(date.today())
    #Prints to Command Line
    print(today)
    print (city)
    #Get data needed for object creation
    main_data = city_weather['main']
    weather = city_weather['weather']
    this_weather = weather[0]['description']
    weather_type = weather[0]['main']
    #Puts data into strings
    temperature = str(int(main_data['temp']))
    this_weather = str(this_weather)
    # Create Post and renders to HTML
    if (weather_type == "Fog" or weather_type == "Mist" or weather_type == "Smoke" or weather_type == "Haze"):
            my_post = Post(title_city=city, at_city="Graveyard", at_image = "images/graveyard.png", date = today, temp = temperature, desc = this_weather)
    elif (int(temperature) >= 100):
        my_post = Post(title_city=city, at_city="Nightosphere", at_image = "images/nightosphere.jpg", date = today, temp = temperature, desc = this_weather)
    elif (int(temperature) <= 32 or weather_type == "Snow"):
        my_post = Post(title_city=city, at_city="Ice Kingdom", at_image = "images/icekingdom.jpg", date = today, temp = temperature, desc = this_weather)
    elif (weather_type == "Clouds"):
        my_post = Post(title_city=city, at_city="Cloud Kingdom", at_image = "images/cloudkingdom.jpg", date = today, temp = temperature, desc = this_weather)
    elif (weather_type == "Rain" or weather_type == "Thunderstorm"):
        my_post = Post(title_city=city, at_city="Knife Storm", at_image = "images/knifestorm.png", date = today, temp = temperature, desc = this_weather)
    elif (int(temperature) >= 81 or weather_type == "Sand"):
        my_post = Post(title_city=city, at_city="Badlands", at_image = "images/badlands.png", date = today, temp = temperature, desc = this_weather)
    elif (int(temperature) <= 44):
        my_post = Post(title_city=city, at_city="Evil Forest", at_image = "images/evilforest.png", date = today, temp = temperature, desc = this_weather)
    else:
        my_post = Post(title_city=city, at_city="Candy Kingdom", at_image = "images/CandyKingdom.jpg", date = today, temp = temperature, desc = this_weather)
    my_post.save()
    return render(request, 'home/home.html', {'Post':my_post})
