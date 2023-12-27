from fastapi import FastAPI
from typing import Union
from typing import List, Dict

import sys
sys.path.append('/Users/emmethamell/Desktop/CitySensor/models')
from database import update_database

# run with uvicorn main:app --reload
app = FastAPI()
@app.post("/update-database/")
async def update_database_route(body: Dict[str, List[str]]):
    links = body.get("links")
    if links:
        update_database(links)
    return {"message": "Database updated successfully"}