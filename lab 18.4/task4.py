import requests
def get_weather(city):
    api_key = 'e47300f3998620f25cc5c15b23495b38'  # Replace with your actual API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'  
    try:
        response = requests.get(base_url, params={'q': city, 'appid': api_key, 'units': 'metric'})
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()       
        if data['cod'] != 200:
            print("Error: City not found. Please enter a valid city.")
            return    
        city_name = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']        
        print(f"City: {city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description.capitalize()}")       
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    city_input = input("Enter city name: ")
    get_weather(city_input)