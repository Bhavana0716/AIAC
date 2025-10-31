import requests
import json

def get_weather(city):
    api_key = 'e47300f3998620f25cc5c15b23495b38'  # Replace with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    weather_data = response.json()
    
    print(json.dumps(weather_data, indent=4))

# Get city input from the console
city = input("Enter the city name: ")
get_weather(city)