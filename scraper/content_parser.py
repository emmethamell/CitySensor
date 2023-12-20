"""""""""
This file contains functions or a function that takes in html content as intput and uses 
beautiful soup to parse it. It extracts the data based on predefined html selectors and patterns
"""""""""
from bs4 import BeautifulSoup
import re

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    #Attempt to find the opening hours using different strategies

    # Strategy 1: Look for elements with specific class names or ids
    class_names = ['opening-hours', 'hours', 'store-hours']
    for class_name in class_names:
        hours_section = soup.find(class_=class_name)
        if hours_section:
            return hours_section.get_text(strip=True) 

    # Strategy 2: Look for elements with specific titles (no links)
    names = ["opening hours", "hours open", "hours"]
    for name in names:
        title = soup.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'p'], string=re.compile(rf'\b{name}\b', re.IGNORECASE))
        if title:
            if title.find_parent('a'):
                continue
            parent_div = title.find_parent('div')
            if parent_div:
                return parent_div.get_text(strip=True)


    # Strategy 3: Look for elements containing specific keywords
    for name in names:
        possible_hours_elements = soup.find_all(string=re.compile(rf'\b{name}\b', re.IGNORECASE))
        for element in possible_hours_elements:
            if element.find_parent('a'):
                continue
            parent = element.parent
            if parent and parent.name in ['div', 'p', 'span']:
                return parent.get_text(strip=True)

    # Strategy 4: look for elements with monday, tuesday, etc.
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
                return ' '.join(found_days)

    return "Opening hours not found"