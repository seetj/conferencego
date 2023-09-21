from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY
import requests
import json


def get_photo(city, state):
    url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": PEXELS_API_KEY}
    params = {
        "per_page": 1,
        "query": city + " " + state,
    }

    response = requests.get(url, headers=headers, params=params)
    content = json.loads(response.content)
    try:
        return {"image_url": content["photos"][0]["src"]["original"]}
    except (KeyError, IndexError):
        return {"image_url": None}


def get_weather_data(city, state):
    geo_url = "http://api.openweathermap.org/geo/1.0/direct"
    headers = {"Authorization": OPEN_WEATHER_API_KEY}
    geo_params = {
        "q": f"{city},{state},USA",
        "appid": OPEN_WEATHER_API_KEY,
    }
    response = requests.get(
        geo_url,
        headers=headers,
        params=geo_params,
    )
    geo_content = json.loads(response.content)

    try:
        coordinates = {
            "latitude": geo_content[0]["lat"],
            "longitude": geo_content[0]["lon"],
        }
    except (KeyError, IndexError):
        coordinates = {
            "latitude": None,
            "longitude": None,
        }

    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    weather_params = {
        "lat": coordinates["latitude"],
        "lon": coordinates["longitude"],
        "appid": OPEN_WEATHER_API_KEY,
        "units": "imperial",
    }
    response = requests.get(
        weather_url,
        headers=headers,
        params=weather_params,
    )
    weather_content = json.loads(response.content)
    try:
        weather_data = {
            "temp": weather_content["main"]["temp"],
            "description": weather_content["weather"][0]["description"],
        }
    except (KeyError, IndexError):
        weather_data = {
            "temp": None,
            "description": None,
        }

    return weather_data
