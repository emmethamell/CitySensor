from bs4 import BeautifulSoup
import re

"""""""""
This file contains functions or a function that takes in html content as intput and uses 
beautiful soup to parse it. It extracts the data based on predefined html selectors and patterns
"""""""""

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    #Attempt to find the opening hours using different strategies

    # Strategy 1: Look for elements with specific class names or ids
    class_names = ['opening-hours', 'hours', 'store-hours']
    for class_name in class_names:
        hours_section = soup.find(class_=class_name)
        if hours_section:
            print("WE ARE USING STRATEGY 1")
            return hours_section.get_text(strip=True) # strip=True removes leading and trailing whitespace

    # Strategy 2: Look for elements with specific titles (no links)
    names = ["opening hours", "hours open", "hours"]
    for name in names:
        # Look for a title that contains the name
        title = soup.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'p'], string=re.compile(rf'\b{name}\b', re.IGNORECASE))
        if title:
            # If the titles parent is a link, continue to next name
            if title.find_parent('a'):
                continue
            # If a title is found, get its parent div
            parent_div = title.find_parent('div')
            if parent_div:
                # If the parent div is found, return all its text
                print("WE ARE USING STRATEGY 2")
                return parent_div.get_text(strip=True)


    # Strategy 3: Look for elements containing specific keywords
    # This uses regular expressions to find elements that contain words like 'hours' or 'open'
    for name in names:
        possible_hours_elements = soup.find_all(string=re.compile(rf'\b{name}\b', re.IGNORECASE))
        for element in possible_hours_elements:
            if element.find_parent('a'):
                continue
            parent = element.parent
            if parent and parent.name in ['div', 'p', 'span']:
                print("WE ARE USING STRATEGY 3")
                return parent.get_text(strip=True)
    
    # todo: add more strategies, strategy 4 is a last resort

    # Strategy 4: look for elements with monday, tuesday, etc.
    # returning all instances
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    found_days = []
    for day in days:
        possible_hours_elements = soup.find_all(string=re.compile(rf'\b{day}\b', re.IGNORECASE))
        for element in possible_hours_elements:
            if element.find_parent('a'):
                continue
            parent = element.find_parent('div')
            if parent and parent.name in ['div', 'p', 'span']:
                found_days.append(parent.get_text(strip=True).replace('\xa0', ' '))

            if found_days:
                print("WE ARE USING STRATEGY 4")
                return ' '.join(found_days)

    return "Opening hours not found"