from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# existing_cities = ['Samarkand']

def index(request):
	api_key = 'afa97e4858f8965c67848f3d19f54582'
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + api_key
	
	if request.method == 'POST':
		if request.POST:
			# if request.POST in existing_cities:
			form = CityForm(request.POST)
			form.save()
		else:
			pass

	form = CityForm()

	cities = City.objects.all().order_by('-id')

	weather_data = []

	for city in cities:
		r = requests.get(url.format(city)).json()
		city_weather = {
			'city' : city.name,
			'tempreature' : round( ((r["main"]["temp"] - 32)*5/9), 2),
			'description' : r["weather"][0]["description"],
			'icon' : r["weather"][0]["icon"],
		}
	
		weather_data.append(city_weather)
	
	

	context = { 'weather_data':weather_data, 'form' : form}
	return render(request, 'the_weather/weather.html', context)