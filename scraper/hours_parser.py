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

from wordsegment import load, segment

load()

def segment_text(text):
    # Segmenting the text
    text = segment(text)
    return ' '.join(text)


input_text = "thisisateststringwithconcatenatedwords"
print (segment_text(input_text))


def parse_hours(text):
    # puts spaces between concatenated words, doesnt do a good job with numbers
    text = normalize(text)

    # add spaces after days, hyphens, and am/pm
    pattern = r"(monday|tuesday|wednesday|thursday|friday|saturday|sunday|mon|tue|wed|thu|fri|sat|sun|-|am|pm)"
    text = re.sub(pattern, lambda match: match.group(0) + ' ', text)

    # get rid of phone numbers
    pattern = r"(\+\d{1,3}\s?)?(\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}"
    text = re.sub(pattern, '', text)

    #remove any random day abbrev before possible zip code (indicates town name followed by postal code)
    pattern = r"(mon|tue|wed|thurs|fri|sat|sun) \d{5}"
    text = re.sub(pattern, '', text)
    
    # remove any text before the first instance of a letter (if there is any) ex: remove phone number before 'mon'
    pattern = r"^[^a-zA-Z]*"
    text = re.sub(pattern, '', text)

    # replace all abbreviations with full day names
    day_mapping = {
        'mon': 'monday',
        'tue': 'tuesday',
        'tues': 'tuesday',
        'wed': 'wednesday',
        'thu': 'thursday',
        'thur': 'thursday',
        'fri': 'friday',
        'sat': 'saturday',
        'sun': 'sunday'
    }

    pattern = r'\b(mon|tue|wed|thu|thur|fri|sat|sun)\b'

    # Function to replace each match with its corresponding full day name
    def replace_match(match):
        return day_mapping[match.group(0).lower()]
    
    text = re.sub(pattern, replace_match, text, flags=re.IGNORECASE)



    text = replace_consecutive_days_with_range(text)


    text = re.sub(r"\b\d{3,4}(am|pm)\b", add_semicolon, text)
    
    return text



# HELPERS
def normalize(text):
    input_string = text.lower()
    input_string = input_string.replace("–", "-")
    pattern = r"(monday|tuesday|wednesday|thursday|friday|saturday|sunday|mon|tue|wed|thu|fri|sat|sun|\d|-|am|pm)"
    matches = re.findall(pattern, input_string)
    result = ''.join(matches)

    return result

def replace_consecutive_days_with_range(text):
    # List of full day names
    days = r"(monday|tuesday|wednesday|thursday|friday|saturday|sunday)"

    # Regular expression pattern to match sequences of day names
    pattern = fr"({days} ?)+"

    # Function to replace matched sequences with a range
    def replacer(match):
        days = match.group().split()
        if days[0] == days[-1]:  # If the first and last day are the same
            return f"{days[0]} "  # Return the single day
        else:
            return f"{days[0]} - {days[-1]} "  # Otherwise, return the range

    # Replace all occurrences in the text
    return re.sub(pattern, replacer, text)


def add_semicolon(match):
    time = match.group()
    if len(time) == 5:  # If there are three numbers
        return time[:1] + ':' + time[1:]
    elif len(time) == 6:  # If there are four numbers
        return time[:2] + ':' + time[2:]
    else:
        return time



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
        print(parse_hours(text))



if __name__ == "__main__":
    main()







