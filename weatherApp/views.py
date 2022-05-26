from urllib import response
from django.shortcuts import render
import urllib.request
import json
# Create your views here.


def home(request):
    if request.method == 'POST':
        city = request.POST['place']
        resource = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=<api_key>').read()

        list_of_resource = json.loads(resource)

        data = {
            "country_code": str(list_of_resource['sys']['country']),
            "city": city,
            "coordinate": str(list_of_resource['coord']['lat']) + ', ' + str(list_of_resource['coord']['lon']),
            "temp": str(list_of_resource['main']['temp']) + ' °C',
            "pressure": str(list_of_resource['main']['pressure']),
            "humidity": str(list_of_resource['main']['humidity']),
            "icon": str(list_of_resource['weather'][0]['icon']),
            "description": str(list_of_resource['weather'][0]['description']),
        }
    else:
        data = {}

    return render(request, 'index.html', data)
