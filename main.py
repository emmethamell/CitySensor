from fastapi import FastAPI
from typing import Union
from typing import List, Dict
from countries.spain import Spain

import sys
sys.path.append('/Users/emmethamell/Desktop/CitySensor/models')
from database import update_database

# run with uvicorn main:app --reload
# body should be a dictionary with a key "links" and a value of a list of links
app = FastAPI()
@app.post("/update-database/")
async def update_database_route(body: Dict[str, List[str]]):
    links = body.get("links")
    if links:
        update_database(links)
    return {"message": "Database updated successfully"}

@app.post("/update-database/spain-restaurants/")
async def update_spain_restaurants_route(body: Dict[str, List[str]]):
    links = body.get("links")
    if links:
        Spain.update_restaurants(links)
    return {"message": "Spanish restaurants database updated successfully"}