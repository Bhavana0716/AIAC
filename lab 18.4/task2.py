import requests
import json
def display_weather(city: str, api_key: str, timeout: int = 5) -> None:
    """
    Fetch and print weather details for a city as JSON.
    On error prints: "Error: Could not connect to API. Check your API key or network connection."
    """
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    try:
        resp = requests.get(url, params=params, timeout=timeout)
        if resp.status_code == 200:
            print(json.dumps(resp.json(), indent=2))
        else:
            print("Error: Could not connect to API. Check your API key or network connection.")
    except (requests.exceptions.InvalidURL,
            requests.exceptions.Timeout,
            requests.exceptions.ConnectionError):
        print("Error: Could not connect to API. Check your API key or network connection.")
    except Exception:
        print("Error: Could not connect to API. Check your API key or network connection.")
if __name__ == "__main__":
    try:
        city = input("Enter city name: ").strip()
        api_key = input("Enter API key: ").strip()
        if not city or not api_key:
            print("Error: City and API key must be provided.")
        else:
            display_weather(city, api_key)
    except KeyboardInterrupt:
        print()  # allow graceful exit on Ctrl+C