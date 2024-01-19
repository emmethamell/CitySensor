from fastapi import FastAPI
from typing import Union
from typing import List, Dict
from countries.spain import Spain
from models.database import update_database, update_database_spain, update_travel_advisories, get_travel_advisory 
from models.api_models import MyModel
from models.api_models import MyModel


# run with uvicorn main:app --reload
# body should be a dictionary with a key "links" and a value of a list of links
app = FastAPI()
@app.post("/update-database/")
async def update_database_route(body: Dict[str, List[str]]):
    links = body.get("links")
    if links:
        update_database(links)
    return {"message": "Database updated successfully"}

@app.post("/update-database/spain/")
async def update_spain_restaurants_route(body: MyModel):
    links = body.links
    subtype = body.subtype
    city = body.city
    if links:
        update_database_spain(links, city, subtype)
    return {"message": "Spain database updated successfuly"}





#TRAVEL ADVISORIES
@app.post("/update-database/travel-advisories/")
async def update_travel_advisories_route():
    update_travel_advisories()
    
@app.get("/travel-advisories/{country}/")
async def get_travel_advisories_route(country: str):
    return get_travel_advisory(country)

