# TO-DO

my_dmi api er lavet på baggrund af etl_dmi database
etl_dmi er en process der henter data fra DMI Open Data API og indlæser vejrdata i en PostgreSQL database. 
Det er denne database my_dmi udstiller data fra.

Projekt to-do:
- Tilføj docker database script 
- Evt. Docker compose der starter etl_dmi, database og my_dmi


### notes

python -m venv .venv

.venv\Scripts\Activate.ps1

pip install fastapi uvicorn sqlalchemy psycopg[binary]
Pydantic 


run in project root:
uvicorn app.main:app --reload

Uvicorn running on http://127.0.0.1:8000

ctlr + c to quit server 

OpenAPI (Swagger)
http://127.0.0.1:8000/docs


