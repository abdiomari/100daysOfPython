import requests

weather_api = 'b217ea8ce34cb9a15c879db79e2d5a9b'

def weather(city, units='metric', weather_api = 'b217ea8ce34cb9a15c879db79e2d5a9b'):

    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={weather_api}&units={units}'
    weather = requests.get(url)
    weather = weather.json()
    with open('weather_data.txt', 'a') as file:
        for dicty in weather['list']:
            file.write(f"{dicty['dt_txt']}, {dicty['main']} {['temp']}, {dicty['weather'][0]['description']}\n")

print(weather(city = 'Nairobi'))