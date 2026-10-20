import datetime
import zoneinfo

from fastapi import FastAPI
from pydantic import BaseModel

class Customer(BaseModel):
    first_name: str
    last_name: str
    description: str | None
    email: str
    age: int

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "pepe"}



COUNTRY_ZONES = {
    "NI": "America/Managua",              # Nicaragua
    "CO": "America/Bogota",               # Colombia
    "MX": "America/Mexico_City",          # México
    "AR": "America/Argentina/Buenos_Aires", # Argentina
    "PE": "America/Lima",                 # Perú
    "US": "America/New_York",             # Estados Unidos
    "ES": "Europe/Madrid",                # España
    "JP": "Asia/Tokyo",                   # Japón
    "AU": "Australia/Sydney",             # Australia
    "BR": "America/Sao_Paulo"             # Brasil
}

@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = COUNTRY_ZONES.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return {"time": datetime.datetime.now(tz)}

@app.post("/customer")
async def create_customer(customer: Customer):
    return customer
