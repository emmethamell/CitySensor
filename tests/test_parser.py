import sys
import pytest
sys.path.append('/Users/emmethamell/Desktop/CitySensor/scraper')
from content_parser import parse_html
from site_scraper import scrape_website
from parse_from_google import parse_google_hours, scrape_website_google


# run with command: "pytest"
# if you want to see print statements, use command "pytest -s"
def test_parse_html_no_hours():
    html = "<html><body><p>this does not contain any of the right keywords</p></body></html>"
    result = parse_html(html)
    print("PRINTRESULT: ", result)
    assert result == "Opening hours not found"

# uses strategy 1
def test_with_savinos():
    result = scrape_website("https://savinosgrill.com/")
    print("PRINTRESULT: ", result)
    assert result == "HoursTue, Wed, Thur, Fri, Sat12:00 PM - 9:00 PMMon5:00 PM - 9:00 PM"

# uses strategy 2
def test_with_spokewinebar():
    result = scrape_website("https://www.spokewinebar.com/")
    print("PRINTRESULT: ", result)
    assert result == "Hourswednesday-saturday 5pm-11pmkitchen is open unil 10pm"

# uses strategy 2
def test_with_phoandthai():
    result = scrape_website("https://www.phoandthairestaurant.com/")
    print("PRINTRESULT: ", result)
    assert result == "Opening HoursMonday – Friday11.30 AM – 9.00 PMSaturday12.00 PM – 9.00 PMSunday12.00 PM – 9.00 PM"


# uses strategy 4
def test_with_myotherkitchen():
    result = scrape_website("https://www.my-other-kitchen.com/")
    print("PRINTRESULT: ", result)
    assert result == "762 Pleasant StreetBelmont, MA 02478Tuesday – Saturday   11:00AM – 7:30PMSunday & Monday      ClosedTel: 617-932-1444​Order Online Here"

# uses strategy 2
def test_with_patou():
    result = scrape_website("https://www.patouthai.com/")
    print("PRINTRESULT: ", result)
    assert result == "Tel: 617-489-699969 Leonard Street, Belmont, MA 02478Get DirectionsHours:Sunday - Wednesday4 PM - 9 PMThursday - Saturday11:30 AM - 9:30 PM"

# uses strategy 4
def test_with_shines():
    result = scrape_website("https://goshines.com/")
    print("PRINTRESULT: ", result)
    assert result == "Location30 Leonard StBelmont, MA 02478Phone617.489.6333HoursMonday ClosedTuesday-Sunday 11:00am-9:00pm"

def test_with_ritceyeast():
    result = scrape_website("https://www.ritceyeast.com/")
    print("PRINTRESULT: ", result)
    assert result == "We do not accept reservations. We are first come, first servedHoursTuesday 3pm - 10pmWednesday 3pm - 10pmThursday 3pm - 10pm (Office Trivia 8pm)Friday 12pm - 11pm*LunchSaturday 3pm - 11pmKitchen HoursTuesdays, Wednesdays, & Thursdays Closes at 9:00Fridays &  Saturdays Closes at 9:30CLOSED SUNDAY & MONDAY"

def test_with_donahues():
    result = scrape_website("https://donohuesbar.com/")
    print("PRINTRESULT: ", result)
    assert result == "HoursMon, Tue, Wed, Thur, Fri9:00 AM - 1:00 AMSat8:00 AM - 1:00 AMSun9:00 AM - 12:00 AM"

def test_with_cityworks():
    result = scrape_website("https://www.cityworksrestaurant.com/locations/watertown/")
    print("PRINTRESULT: ", result)
    assert result == "Mon11:00am - 11:00pmTues11:00am - 11:00pmWed11:00am - 11:00pmThurs11:00am - 12:00amFri11:00am - 1:00amSat10:00am - 1:00amSun10:00am - 11:00pm"

# THESE TESTS SHOULD USE SELENIUM TO CLICK "HOURS"
def test_with_markandtonis_new():
    result = scrape_website("https://markandtonis.com/")
    print("PRINTRESULT: ", result)
    assert result == "hoursWe are open!Monday:11am – 9pmTuesday:11am – 9pmWednesday:11am – 9pmThursday:11am – 9pmFriday:11am – 9pmSaturday:11am – 9pmSunday:11am – 9pm"

def test_with_lisas():
    result = scrape_website("https://www.lisaspizzeriabelmont.com/")
    print("PRINTRESULT: ", result)
    assert result == "hoursWe are openMonday:10:30am - 9pmTuesday:10:30am - 9pmWednesday:10:30am - 9pmThursday:10:30am - 9pmFriday:10:30am - 9pmSaturday:10:30am - 9pmSunday:11:00am - 9pm"  



# THESE TESTS ARE USING THE GOOGLE SEARCH RESULT

def test_with_savinos_google():
    result = scrape_website_google("https://www.google.com/search?q=savinos+belmont&hl=en")
    print("PRINTRESULT: ", result)
    assert result == "Monday(Christmas) (Christmas) 5–8:30 PMHours might differ Hours might differ Hours might differ Tuesday 12–2:30 PM, 5–8:30 PM Wednesday 12–2:30 PM, 5–8:30 PM Thursday 12–2:30 PM, 5–8:30 PM Friday 12–2:30 PM, 5–8:30 PM Saturday 12–2:30 PM, 5–8:30 PM Sunday(Christmas Eve) (Christmas Eve) Closed"


def test_with_spoke_google():
    result = scrape_website_google("https://www.google.com/search?q=spoke+wine+bar+belmont&hl=en")
    print("PRINTRESULT: ", result)
    assert result == "Monday(Christmas) (Christmas) Closed Tuesday Closed Wednesday 5–11 PM Thursday 5–11 PM Friday 5–11:30 PM Saturday 5–11:30 PM Sunday(Christmas Eve) (Christmas Eve) Closed"


def test_with_pho_and_thai():
    result = scrape_website_google("https://www.google.com/search?q=pho+and+thai+belmont&hl=en")
    print("PRINTRESULT: ", result)
    assert result == "Monday(Christmas) (Christmas) 11 AM–9 PMHours might differ Hours might differ Hours might differ Tuesday 11 AM–9 PM Wednesday 11 AM–9:45 PM Thursday 11 AM–9:45 PM Friday 11 AM–9:45 PM Saturday 4–9:30 PM Sunday(Christmas Eve) (Christmas Eve) 4–10 PMHours might differ Hours might differ Hours might differ Monday(Christmas) (Christmas) 11 AM–9:45 PMHours might differ Hours might differ Hours might differ Tuesday 11 AM–9:45 PM Wednesday 11 AM–9 PM Thursday 11 AM–9 PM Friday 11 AM–9 PM Saturday 11 AM–9 PM Sunday(Christmas Eve) (Christmas Eve) 11 AM–9 PMHours might differ Hours might differ Hours might differ Monday(Christmas) (Christmas) 11 AM–9 PMHours might differ Hours might differ Hours might differ Tuesday 11 AM–9 PM Wednesday 11 AM–9 PM Thursday 11 AM–9 PM Friday 11 AM–9 PM Saturday 11 AM–9 PM Sunday(Christmas Eve) (Christmas Eve) 11 AM–9 PMHours might differ Hours might differ Hours might differ"


def test_with_my_other_kitchen():
    result = scrape_website_google("https://www.google.com/search?q=my+other+kitchen+belmont&hl=en")
    print("PRINTRESULT: ", result)
    assert result == "Monday(Christmas) (Christmas) Closed Tuesday 11 AM–7:30 PM Wednesday 11 AM–7:30 PM Thursday 11 AM–7:30 PM Friday 11 AM–7:30 PM Saturday 11 AM–7:30 PM Sunday(Christmas Eve) (Christmas Eve) Closed"