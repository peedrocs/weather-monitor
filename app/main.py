from app.database import engine, SessionLocal
from app.models import Base, Weather
from app.weather_service import get_weather
from app.location_search import get_location

def run():
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    location_data = get_location()
    weather_data = get_weather()

    weather = Weather(**weather_data)
    session.add(weather)
    session.commit()
    session.close()

    print("Dados salvos com sucesso")

if __name__ == "__main__":
    run()