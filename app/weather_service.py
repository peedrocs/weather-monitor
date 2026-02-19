import requests
from app.location_search import get_location

def get_weather():
    cidade,lat,lon = get_location()
    
    response = requests.get(
        'https://api.open-meteo.com/v1/forecast',
        params= {
            'latitude':lat,
            'longitude':lon,
            'current_weather':True
        }
    )
    data = response.json()

    temperatura = data["current_weather"]["temperature"]
    descricao = f"Velocidade do vento: {data['current_weather']['windspeed']}, Direcao do vento: {data['current_weather']['winddirection']}"
    return {
        "city": cidade,
        "temperature": temperatura,
        "description": descricao, 
    }