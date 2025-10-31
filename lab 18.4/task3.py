import requests
def get_weather_data(city):
    api_key = 'e47300f3998620f25cc5c15b23495b38'  # Replace with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        print(f'City: {city}')
        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
        print(f'Weather: {description.capitalize()}')
    else:
        print('City not found or API request failed.')
if __name__ == '__main__':
    city = input('Enter city name: ')
    get_weather_data(city)