import requests

base_url = "http://api.weatherapi.com/v1"

API_KEY = " "

par = {
    "key": API_KEY,
    "q": "Rawalpindi"}

def get_weather_info(type):
    url = f"{base_url}/{type}"
    response = requests.get(url, params= par)
    
    if response:
        data = response.json()
        return data
    else:
        print(f"Error retrieving data! {response}")

name = "current.json"
weather_info = get_weather_info(name)

if weather_info:
    print(f"Name: {weather_info['location']['name']}")
    print(f"Country: {weather_info['location']['country']}")
    print(f"Latitude: {weather_info['location']['lat']}")
    print(f"Local Time: {weather_info['location']['localtime']}")
    