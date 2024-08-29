import requests
from requests.exceptions import RequestException
from django.shortcuts import render
from .models import City
from .forms import CityForm

def fetch_weather_data(city_name, url, app_id):
    try:
        response = requests.get(url.format(city_name, app_id))
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        print(f"Ошибка при получении данных для города {city_name}: {e}")
        return None

def index(request):
    app_id = "72daa33d94dc356a2ccd10899de68aa3"
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city_name = form.cleaned_data['name'].strip().lower()
            existing_city = City.objects.filter(name__iexact=new_city_name).first()

            if existing_city:
                City.objects.filter(name__iexact=new_city_name).delete()
            form.save()
    
    form = CityForm()
    cities = City.objects.all()
    all_cities = []
    city_names_in_list = set()

    for city in cities:
        data = fetch_weather_data(city.name, url, app_id)
        if data and "main" in data and "weather" in data:
            city_info = {
                'city': city.name,
                'temp': data["main"]["temp"],
                'icon': data["weather"][0]["icon"],
            }
            if city.name.lower() in city_names_in_list:
                all_cities = [info for info in all_cities if info['city'].lower() != city.name.lower()]
            else:
                city_names_in_list.add(city.name.lower())
            all_cities.insert(0, city_info)

    highlighted_city = all_cities[0] if all_cities else None
    context = {'all_info': all_cities, 'form': form, 'highlighted_city': highlighted_city}
    return render(request, 'weather/index.html', context)
