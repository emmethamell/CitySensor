"""""""""
Here you need to make a function that takes in a string and looks for patterns to
identify the opening days and hours
"""""""""

import re
import os
import openai
from dotenv import load_dotenv

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import RegexpParser
from nltk.tokenize import RegexpTokenizer

# Ensure required resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

load_dotenv()
openai_key: str = os.environ.get("openai_api_key")


def parse_hours(text):
    text = normalize(text)
    """""""""
    Some examples of what text should look like up to this point:
    * tuewedthufrisat1200pm-900pmmon500pm-900pm
    * wednesday-saturday5pm-11pm10pm
    * 617-489-699969mon02478sunday-wednesday4pm-9pmthursday-saturday1130am-930pm
    * monday11am-9pmtuesday11am-9pmwednesday11am-9pmthursday11am-9pmfriday11am-9pmsaturday11am-9pmsunday11am-9pm
    """""""""
    # add spaces after days, hyphens, and am/pm
    # pattern = r"(monday|tuesday|wednesday|thursday|friday|saturday|sunday|mon|tue|wed|thu|fri|sat|sun|-|am|pm)"
    # text = re.sub(pattern, lambda match: match.group(0) + ' ', text)

    # get rid of phone numbers
    pattern = r"(\+\d{1,3}\s?)?(\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}"
    text = re.sub(pattern, '', text)

    #remove any random day abbrev before possible zip code
    pattern = r"(mon|tue|wed|thurs|fri|sat|sun)\d{5}"
    text = re.sub(pattern, '', text)
    
    # remove any text before the first instance of a letter (if there is any) ex: remove phone number before 'mon'
    pattern = r"^[^a-zA-Z]*"
    text = re.sub(pattern, '', text)

    """""""""
    Now text should look like this:
    * tue wed thu fri sat 1200pm - 900pm mon 500pm - 900pm
    * wednesday - saturday 5pm - 11pm 10pm
    * mon 02478sunday - wednesday 4pm - 9pm thursday - saturday 1130am - 930pm
    * monday 11am - 9pm tuesday 11am - 9pm wednesday 11am - 9pm thursday 11am - 9pm friday 11am - 9pm saturday 11am - 9pm sunday 11am - 9pm
    """""""""

    return text




def normalize(text):
    input_string = text.lower()
    input_string = input_string.replace("–", "-")
    pattern = r"(monday|tuesday|wednesday|thursday|friday|saturday|sunday|mon|tue|wed|thu|fri|sat|sun|\d|-|am|pm)"
    matches = re.findall(pattern, input_string)
    result = ''.join(matches)
    return result



def main():
    example_texts = [
    "HoursTue, Wed, Thur, Fri, Sat12:00 PM - 9:00 PMMon5:00 PM - 9:00 PM",
    "Hourswednesday-saturday 5pm-11pmkitchen is open unil 10pm",
    "Opening HoursMonday – Friday11.30 AM – 9.00 PMSaturday12.00 PM – 9.00 PMSunday12.00 PM – 9.00 PM",
    "762 Pleasant StreetBelmont, MA 02478Tuesday – Saturday   11:00AM – 7:30PMSunday & Monday      ClosedTel: 617-932-1444​Order Online Here",
    "Tel: 617-489-699969 Leonard Street, Belmont, MA 02478Get DirectionsHours:Sunday - Wednesday4 PM - 9 PMThursday - Saturday11:30 AM - 9:30 PM",
    "Location30 Leonard StBelmont, MA 02478Phone617.489.6333HoursMonday ClosedTuesday-Sunday 11:00am-9:00pm",
    "We do not accept reservations. We are first come, first servedHoursTuesday 3pm - 10pmWednesday 3pm - 10pmThursday 3pm - 10pm (Office Trivia 8pm)Friday 12pm - 11pm*LunchSaturday 3pm - 11pmKitchen HoursTuesdays, Wednesdays, & Thursdays Closes at 9:00Fridays &  Saturdays Closes at 9:30CLOSED SUNDAY & MONDAY",
    "hoursWe are open!Monday:11am – 9pmTuesday:11am – 9pmWednesday:11am – 9pmThursday:11am – 9pmFriday:11am – 9pmSaturday:11am – 9pmSunday:11am – 9pm",
    "hoursWe are openMonday:10:30am - 9pmTuesday:10:30am - 9pmWednesday:10:30am - 9pmThursday:10:30am - 9pmFriday:10:30am - 9pmSaturday:10:30am - 9pmSunday:11:00am - 9pm"
    ]

    for text in example_texts:
        print("LINE: ")
        print( parse_hours(text))

if __name__ == "__main__":
    main()









