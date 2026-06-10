import requests


def get_country_coordinates(country: str):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": country,
        "format": "json"
    }

    headers = {
        "User-Agent": "aviation-project"
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    if data:
        return float(data[0]["lat"]), float(data[0]["lon"])

    return None, None