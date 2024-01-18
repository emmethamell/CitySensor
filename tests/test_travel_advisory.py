import pytest
from travel_advisories.scraper import TravelAdvisory
from models.database import update_travel_advisories


def test_travel_advisories():
    TravelAdvisory.scrape_website()
    assert True == True
    
def test_update_database():
    update_travel_advisories()
    assert True == True