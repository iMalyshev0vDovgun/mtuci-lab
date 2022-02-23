import requests

city = "Moscow, RU"
appid = "c1e081254d909ec4302157a0b58af96b"

res = requests.get(
    "http://api.openweathermap.org/data/2.5/forecast",
    params = {
        'q': city,
        'units': 'metric',
        'lang': 'ru',
        'APPID': appid
    }
)

data = res.json()

print("Прогноз погоды на неделю:")
for i in data['list']:
    print(
        "Дата <", i['dt_txt'],
        "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']),
        "> \r\nПогодные условия <",
        i['weather'][0]['description'], ">"
    )
    print("____________________________")