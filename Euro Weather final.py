import requests
from datetime import datetime
import pytz

API_KEY = "21ded2d7368baa1aaf5b76baa936dbbc"

CITIES = {
    "London": "Europe/London",
    "Paris": "Europe/Paris",
    "Berlin": "Europe/Berlin",
    "Rome": "Europe/Rome",
    "Kyiv": "Europe/Kyiv",
    "Madrid": "Europe/Madrid",
    "Vienna": "Europe/Vienna",
    "Athens": "Europe/Athens",
    "Warsaw": "Europe/Warsaw",
    "Prague": "Europe/Prague",
    "Oslo": "Europe/Oslo",
    "Stockholm": "Europe/Stockholm",
    "Lisbon": "Europe/Lisbon",
    "Helsinki": "Europe/Helsinki",
    "Brussels": "Europe/Brussels"
}

def get_weather(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    res = requests.get(url)
    data = res.json()
    if res.status_code == 200:
        temp = data['main']['temp']
        return temp
    else:
        return None

def show_cities():
    print("🌍 Столиці Європи:")
    for idx, city in enumerate(CITIES.keys(), start=1):
        print(f"{idx}. {city}")

def get_city_info(city_name):
    if city_name in CITIES:
        timezone = CITIES[city_name]
        now = datetime.now(pytz.timezone(timezone))
        temp = get_weather(city_name)
        temp_str = f"{temp}°C" if temp is not None else "н/д"
        print(f"\n🌍 {city_name}")
        print(f"Час: {now.strftime('%H:%M:%S')}")
        print(f"Температура: {temp_str}")
    else:
        print("❌ Такої столиці не існує в списку.")

def main():
    show_cities()
    user_input = input("\nВведіть номер столиці або її назву для отримання часу та температури: ")
    
    try:
        city_idx = int(user_input)
        city_name = list(CITIES.keys())[city_idx - 1]
    except ValueError:
        city_name = user_input.strip()

    get_city_info(city_name)

if __name__ == "__main__":
    main()
