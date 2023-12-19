import sys
import pytest
sys.path.append('/Users/emmethamell/Desktop/CitySensor/scraper')
from content_parser import parse_html
from site_scraper import scrape_website, scrape_website_no_selenium


# run with command: "pytest"
# if you want to see print statements, use command "pytest -s"
@pytest.mark.skip()
def test_parse_html_no_hours():
    html = "<html><body><p>this does not contain any of the right keywords</p></body></html>"
    result = parse_html(html)
    print("PRINTRESULT: ", result)
    assert result == "Opening hours not found"

# uses strategy 1
@pytest.mark.skip()
def test_with_savinos():
    result = scrape_website("https://savinosgrill.com/")
    print("PRINTRESULT: ", result)
    assert result == "HoursTue, Wed, Thur, Fri, Sat12:00 PM - 9:00 PMMon5:00 PM - 9:00 PM"

# uses strategy 2
@pytest.mark.skip()
def test_with_spokewinebar():
    result = scrape_website("https://www.spokewinebar.com/")
    print("PRINTRESULT: ", result)
    assert result == "Hourswednesday-saturday 5pm-11pmkitchen is open unil 10pm"

# uses strategy 2
@pytest.mark.skip()
def test_with_phoandthai():
    result = scrape_website("https://www.phoandthairestaurant.com/")
    print("PRINTRESULT: ", result)
    assert result == "Opening HoursMonday – Friday11.30 AM – 9.00 PMSaturday12.00 PM – 9.00 PMSunday12.00 PM – 9.00 PM"


# uses strategy 4
@pytest.mark.skip()
def test_with_myotherkitchen():
    result = scrape_website("https://www.my-other-kitchen.com/")
    print("PRINTRESULT: ", result)
    assert result == "762 Pleasant StreetBelmont, MA 02478Tuesday – Saturday   11:00AM – 7:30PMSunday & Monday      ClosedTel: 617-932-1444​Order Online Here"

# uses strategy 2
@pytest.mark.skip()
def test_with_patou():
    result = scrape_website("https://www.patouthai.com/")
    print("PRINTRESULT: ", result)
    assert result == "Tel: 617-489-699969 Leonard Street, Belmont, MA 02478Get DirectionsHours:Sunday - Wednesday4 PM - 9 PMThursday - Saturday11:30 AM - 9:30 PM"

# uses strategy 4
@pytest.mark.skip()
def test_with_shines():
    result = scrape_website("https://goshines.com/")
    print("PRINTRESULT: ", result)
    assert result == "Location30 Leonard StBelmont, MA 02478Phone617.489.6333HoursMonday ClosedTuesday-Sunday 11:00am-9:00pm"

@pytest.mark.skip()
def test_with_ritceyeast():
    result = scrape_website("https://www.ritceyeast.com/")
    print("PRINTRESULT: ", result)
    assert result == "We do not accept reservations. We are first come, first servedHoursTuesday 3pm - 10pmWednesday 3pm - 10pmThursday 3pm - 10pm (Office Trivia 8pm)Friday 12pm - 11pm*LunchSaturday 3pm - 11pmKitchen HoursTuesdays, Wednesdays, & Thursdays Closes at 9:00Fridays &  Saturdays Closes at 9:30CLOSED SUNDAY & MONDAY"



# THESE TESTS SHOULD USE SELENIUM TO CLICK "HOURS"
@pytest.mark.skip()
def test_with_markandtonis_new():
    result = scrape_website("https://markandtonis.com/")
    print("PRINTRESULT: ", result)
    assert result == "hoursWe are open!Monday:11am – 9pmTuesday:11am – 9pmWednesday:11am – 9pmThursday:11am – 9pmFriday:11am – 9pmSaturday:11am – 9pmSunday:11am – 9pm"

@pytest.mark.skip()
def test_with_lisas():
    result = scrape_website("https://www.lisaspizzeriabelmont.com/")
    print("PRINTRESULT: ", result)
    assert result == "hoursWe are openMonday:10:30am - 9pmTuesday:10:30am - 9pmWednesday:10:30am - 9pmThursday:10:30am - 9pmFriday:10:30am - 9pmSaturday:10:30am - 9pmSunday:11:00am - 9pm"  



