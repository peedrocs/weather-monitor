import requests

def get_location():
    response = requests.get('http://ip-api.com/json/')
    data = response.json()
    cidade = f"{data['city']}, {data['country']}"
    lat = round(data['lat'],2)
    lon = round(data['lon'],2)
    return cidade,lat,lon

