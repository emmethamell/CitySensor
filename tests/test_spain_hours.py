import pytest
from countries.spain import Spain
from helpers.parse_helpers import Helper

#pytestmark = pytest.mark.skip()
@pytest.mark.skip() 
def test_getting_hours1():
    result = Helper.get_html("https://lechedetigretx.com/")
    number = Spain.parse_hours(result)
    print("ONE PRINTRESULT: ", number)

@pytest.mark.skip()
def test_getting_hours2():
    result = Helper.get_html("https://www.seasonrestaurante.es/en/")
    number = Spain.parse_hours(result)
    print("TWO PRINTRESULT: ", number)

@pytest.mark.skip()
def test_getting_hours3():
    result = Helper.get_html("https://www.mrportersteakhouse.com/barcelona")
    number = Spain.parse_hours(result)
    print("THREE PRINTRESULT: ", number)

@pytest.mark.skip()
def test_getting_hours5():
    result = Helper.get_html("https://alkimia.cat/alkimia-eng/")
    number = Spain.parse_hours(result)
    print("FIVE PRINTRESULT: ", number)

@pytest.mark.skip()
def test_getting_hours6():
    result = Helper.get_html("https://www.canfisher.com/en/reservations/")
    number = Spain.parse_hours(result)
    print("SIX PRINTRESULT: ", number)

@pytest.mark.skip()
def test_getting_hours10():
    result = Helper.get_html("https://restaurantcansole.com/en/")
    number = Spain.parse_hours(result)
    print("TEN PRINTRESULT: ", number)
    

#DOES NOT AUTHORIZE THE HTML REQUEST (403)
def test_getting_hours4():
    result = Helper.get_html("https://cincsentits.com/en/")
    number = Spain.parse_hours(result)
    print("FOUR PRINTRESULT: ", number)
    
def test_getting_hours11():
    result = Helper.get_html("https://barramon.dudaone.com/")
    hours = Spain.parse_hours(result)
    print("ELEVEN PRINTRESULT: ", hours)
    
def test_getting_hours12():
    result = Helper.get_html("https://www.caelis.com/en/")
    hours = Spain.parse_hours(result)
    print("TWELVE PRINTRESULT: ", hours)