import os
import sys
import json
import requests
RESULTS_FILE = "results.json"
OWM_URL = "https://api.openweathermap.org/data/2.5/weather"
def fetch_weather(city, api_key):
    params = {"q": city, "appid": api_key, "units": "metric"}
    try:
        r = requests.get(OWM_URL, params=params, timeout=10)
    except requests.RequestException as e:
        raise RuntimeError(f"Network error: {e}")
    if not r.ok:
        try:
            err = r.json().get("message", r.text)
        except Exception:
            err = r.text
        raise RuntimeError(f"API error ({r.status_code}): {err}")
    try:
        d = r.json()
        return {
            "city": d.get("name") or city,
            "temp": d["main"]["temp"],
            "humidity": d["main"]["humidity"],
            "weather": d["weather"][0]["description"].capitalize()
        }
    except Exception:
        raise RuntimeError("Invalid or unexpected API response")
def load_results(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []
def save_results(path, results):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
def display_weather():
    api_key = os.getenv("OPENWEATHER_API_KEY") or input("Enter OpenWeatherMap API key: ").strip()
    if not api_key:
        print("API key is required.", file=sys.stderr)
        return
    city = input("Enter city name: ").strip()
    if not city:
        print("City name is required.", file=sys.stderr)
        return
    try:
        weather = fetch_weather(city, api_key)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        return
    print(json.dumps(weather, ensure_ascii=False, indent=2))
    results = load_results(RESULTS_FILE)
    results.append(weather)
    try:
        save_results(RESULTS_FILE, results)
    except Exception as e:
        print(f"Failed to save results: {e}", file=sys.stderr)
if __name__ == "__main__":
    display_weather()
