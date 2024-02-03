import pytest
from countries.spain import Spain
from helpers.parse_helpers import Helper
# run with command: "pytest"
# if you want to see print statements, use command "pytest -s"


def test_get_info():
    result = Helper.get_html_selenium("https://www.saladedespiece.com/contacto/")
    print("PRINTRESULT:", result)
    assert result != None



@pytest.mark.skip()
def test_getHtml():
    result = Helper.get_html("https://www.canfisher.com/en/reservations/")
    print("PRINTRESULT: ", result)
    assert result != None




"""""""""
The following sites contain a href with the phone number, this is easiest
"""""""""
@pytest.mark.skip() 
#HAS HREF
def test_getting_phone1():
    result = Helper.get_html("https://lechedetigretx.com/")
    number = Spain.parse_phone_number(result)
    print("ONE PRINTRESULT: ", number)

@pytest.mark.skip()
#HAS HREF
def test_getting_phone2():
    result = Helper.get_html("https://www.seasonrestaurante.es/en/")
    number = Spain.parse_phone_number(result)
    print("TWO PRINTRESULT: ", number)

@pytest.mark.skip()
#HAS HREF
def test_getting_phone3():
    result = Helper.get_html("https://www.mrportersteakhouse.com/barcelona")
    number = Spain.parse_phone_number(result)
    print("THREE PRINTRESULT: ", number)

@pytest.mark.skip()
#HAS HREF: DOES NOT AUTHORIZE THE HTML REQUEST (403)
def test_getting_phone4():
    result = Helper.get_html("https://cincsentits.com/en/")
    number = Spain.parse_phone_number(result)
    print("FOUR PRINTRESULT: ", number)

@pytest.mark.skip()
#HAS HREF:
def test_getting_phone5():
    result = Helper.get_html("https://alkimia.cat/alkimia-eng/")
    number = Spain.parse_phone_number(result)
    print("FIVE PRINTRESULT: ", number)

@pytest.mark.skip()
#HAS HREF:
def test_getting_phone6():
    result = Helper.get_html("https://www.canfisher.com/en/reservations/")
    number = Spain.parse_phone_number(result)
    print("SIX PRINTRESULT: ", number)

@pytest.mark.skip()
def test_getting_phone10():
    result = Helper.get_html("https://restaurantcansole.com/en/")
    number = Spain.parse_phone_number(result)
    print("TEN PRINTRESULT: ", number)





"""""""""
The following sites do not contain a href with phone number
"""""""""
@pytest.mark.skip()
def test_getting_phone7():
    result = Helper.get_html("https://en.bodegajoan.com/")
    number = Spain.parse_phone_number(result)
    print("SEVEN PRINTRESULT: ", number)

#FAILED TO RETRIEVE WEBSITE (403)
@pytest.mark.skip()
def test_getting_phone8():
    result = Helper.get_html("https://barramon.dudaone.com/")
    number = Spain.parse_phone_number(result)
    print("EIGHT PRINTRESULT: ", number)

@pytest.mark.skip()
def test_getting_phone9():
    result = Helper.get_html("https://www.restaurantestevet.com/en/")
    number = Spain.parse_phone_number(result)
    print("NINE PRINTRESULT: ", number)

@pytest.mark.skip()
def test_getting_phone11():
    result = Helper.get_html("https://restaurantcansole.com/en/")
    number = Spain.parse_phone_number(result)
    print("ELEVEN PRINTRESULT: ", number)

@pytest.mark.skip()
def test_getting_phone12():
    result = Helper.get_html("https://elchigre1769.com/en/")
    number = Spain.parse_phone_number(result)
    print("TWELVE PRINTRESULT: ", number)

@pytest.mark.skip()
def test_getting_phone13():
    result = Helper.get_html("https://www.caelis.com/en/")
    number = Spain.parse_phone_number(result)
    print("THIRTEEN PRINTRESULT: ", number)

@pytest.mark.skip()
def test_getting_phone14():
    result = Helper.get_html("https://formaje.com/pages/contacto")
    number = Spain.parse_phone_number(result)
    print("FOURTEEN PRINTRESULT: ", number)

@pytest.mark.skip()
def test_getting_phone15():
    result = Helper.get_html("https://tripea.es/contacto")
    number = Spain.parse_phone_number(result)
    print("FIFTEEN PRINTRESULT: ", number)

@pytest.mark.skip()
def test_getting_phone16():
    result = Helper.get_html("https://www.saladedespiece.com/contacto/")
    number = Spain.parse_phone_number(result)
    print("SIXTEEN PRINTRESULT: ", number)

@pytest.mark.skip()
def test_getting_phone17():
    result = Helper.get_html("https://desde1911.es/en/")
    number = Spain.parse_phone_number(result)
    print("SEVENTEEN PRINTRESULT: ", number)

@pytest.mark.skip()
def test_getting_phone18():
    result = Helper.get_html("https://diverxo.com/en/home/")
    number = Spain.parse_phone_number(result)
    print("EIGHTEEN PRINTRESULT: ", number)

@pytest.mark.skip()
def test_getting_phone18():
    result = Helper.get_html("https://www.restaurantesacha.com/")
    number = Spain.parse_phone_number(result)
    print("EIGHTEEN PRINTRESULT: ", number)





    

