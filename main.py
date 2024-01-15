from fastapi import FastAPI
from typing import Union
from typing import List, Dict
from countries.spain import Spain
from models.database import update_database, update_database_spain
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
    return {"message": "Spanish restaurants database updated successfully"}