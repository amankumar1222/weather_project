from django.shortcuts import render
import requests
from .models import City


# Create your views here.


def index(request):

    allCitye = City.objects.all()

    if request.method == "POST":
        city = request.POST.get('city')
        city = City(city=city)
        city.save()

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=AddYourKey"

    city = "India"
    world_data = []
    for city in allCitye:

        city_weather = requests.get(url.format(city)).json()
        world_weather = {
            'city':city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
        }
        world_data.append(world_weather)
    
    params = {"weather_data":world_data}



    return render(request , 'weather/index.html',params)

