import requests


def get_airplanes():
    url = "https://opensky-network.org/api/states/all"

    response = requests.get(url)

    data = response.json()

    return data.get("states", [])
