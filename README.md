# 🌦️ Weather Monitor

Projeto em Python que consulta informações meteorológicas com base na localização do usuário.

A aplicação identifica a localização via IP, obtém latitude e longitude automaticamente e utiliza uma API de clima para retornar os dados meteorológicos da região.



## Como funciona

1. O usuário realiza uma requisição.
2. A aplicação identifica o IP do usuário.
3. Uma API de geolocalização retorna a latitude e longitude.
4. Esses dados são enviados para uma API de clima.
5. As informações meteorológicas são retornadas ao usuário.
6. Os dados podem ser armazenados em um banco PostgreSQL.



## Tecnologias Utilizadas

- Python 3.11
- Requests
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose


### Criar o arquivo .env

DB_HOST=db
DB_NAME=weather
DB_USER=postgres
DB_PASSWORD=postgres
DB_PORT=5432


## Estrutura do projeto

weather-monitor/<br>
│<br>
├── Dockerfile<br>
├── docker-compose.yml<br>
├── requirements.txt<br>
└── app/<br>
