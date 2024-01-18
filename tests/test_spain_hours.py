import pytest
from countries.spain import Spain
from helpers.parse_helpers import Helper

pytestmark = pytest.mark.skip()
#@pytest.mark.skip() 
#HAS HREF
def test_getting_phone1():
    result = Helper.get_html("https://lechedetigretx.com/")
    number = Spain.parse_hours(result)
    print("ONE PRINTRESULT: ", number)

#@pytest.mark.skip()
#HAS HREF
def test_getting_phone2():
    result = Helper.get_html("https://www.seasonrestaurante.es/en/")
    number = Spain.parse_hours(result)
    print("TWO PRINTRESULT: ", number)

#@pytest.mark.skip()
#HAS HREF
def test_getting_phone3():
    result = Helper.get_html("https://www.mrportersteakhouse.com/barcelona")
    number = Spain.parse_hours(result)
    print("THREE PRINTRESULT: ", number)

#@pytest.mark.skip()
#HAS HREF: DOES NOT AUTHORIZE THE HTML REQUEST (403)
def test_getting_phone4():
    result = Helper.get_html("https://cincsentits.com/en/")
    number = Spain.parse_hours(result)
    print("FOUR PRINTRESULT: ", number)

#@pytest.mark.skip()
#HAS HREF:
def test_getting_phone5():
    result = Helper.get_html("https://alkimia.cat/alkimia-eng/")
    number = Spain.parse_hours(result)
    print("FIVE PRINTRESULT: ", number)

#@pytest.mark.skip()
#HAS HREF:
def test_getting_phone6():
    result = Helper.get_html("https://www.canfisher.com/en/reservations/")
    number = Spain.parse_hours(result)
    print("SIX PRINTRESULT: ", number)

def test_getting_phone10():
    result = Helper.get_html("https://restaurantcansole.com/en/")
    number = Spain.parse_hours(result)
    print("TEN PRINTRESULT: ", number)