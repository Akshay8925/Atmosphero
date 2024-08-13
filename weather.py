import requests

def get_weather(city,country):
    api_key ='d4cb251cceaba47bd5e051c9ed6ba784'
    current_weather_url = f"https://openweathermap.org/data/2.5 weather?q={city},{country}&appid={api_key}"
    forecast_weather_url = f"https://openweathermap.org/data/2.5/forecast/daily?q{city},{country}&cnt=7&appid={api_key}"

    current_weather_response = requests.get(current_weather_url)
    forecast_weather_response = requests.get(forecast_weather_url)

    if current_weather_response.status_code == 200 and forecast_weather_response.status_code == 200:
        return{
            'current': current_weather_response.json(),
            'forecast': forecast_weather_response.json()
        }
    else:
        return None