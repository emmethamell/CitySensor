"""""""""
Here you need to make a function that takes in a string and looks for patterns to
identify the opening days and hours
"""""""""
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai_key: str = os.environ.get("openai_api_key")

def parse_hours(text, key):
    openai.api_key = key
    response = openai.Completion.create(
      engine="ft:davinci-002:university-of-massachusetts-amherst::8XtZcf8T",  # You can choose different models
      prompt = f"Extract the business hours for each day of the week from the following text:\n\n{text}\n\nPlease provide the opening and closing times for each day from Monday to Sunday. If the business is closed on a particular day, indicate it as 'Closed'.",
      max_tokens=150  # Adjust based on expected length of response
    )

    return response.choices[0].text.strip()





# Example usage
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
    print(parse_hours(text, openai_key))
