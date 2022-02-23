import requests

city = "Moscow, RU"
appid = "c1e081254d909ec4302157a0b58af96b"

params = {
    'q': city,
    'units': 'metric',
    'lang': 'ru',
    'APPID': appid
}

res_weather = requests.get("http://api.openweathermap.org/data/2.5/weather", params)
res_forecast = requests.get("http://api.openweathermap.org/data/2.5/forecast", params)

data = res_weather.json()

print("Прогноз погоды на сейчас:")
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура:", data['main']['temp_max'])
print("Видимость:", data['visibility'])
print("Скорость ветра:", data['wind']['speed'])

print("-" * 30)

print("Прогноз погоды на неделю:")
for i in res_forecast.json()['list']:
    print(
        "Дата <", i['dt_txt'], "> \r\n",
        "Температура <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\n",
        "Видимость <", i['visibility'], "> \r\n",
        "Скорость ветра <", '{0:.2f}'.format(i['wind']['speed']), "> \r\n",
        "Погодные условия <", i['weather'][0]['description'], ">"
    )
    print("____________________________")
