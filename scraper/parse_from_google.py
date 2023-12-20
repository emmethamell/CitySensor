"""""""""
This file is to parse to hours from google maps in the fastest way, 
provided that the hours are in the same format

base url: https://www.google.com/search?q=business+name+location+keyword&hl=en
(keyword is optional)
"""""""""

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from content_parser import parse_html
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from content_parser import parse_html


def scrape_website_google(url):
    driver = webdriver.Chrome()  
    driver.get(url)

    try:

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "BTP3AC"))
        )
        element.click()
    except:
        pass  

    html = driver.page_source
    driver.quit()

    parsed_content = parse_google_hours(html)
    return parsed_content


def parse_google_hours(html):
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.select('.SKNSIb')
    result = []

    for element in elements:
        parent_tr = element.find_parent('tr')
        if parent_tr:
            text = ' '.join(item.text for item in parent_tr.select('*'))
            result.append(text)

    return ' '.join(reorder_to_monday(result))


def reorder_to_monday(hours_list):
    monday_index = next((i for i, s in enumerate(hours_list) if "Monday" in s), None)

    if monday_index is not None:
        ordered_hours = hours_list[monday_index:] + hours_list[:monday_index]
    else:
        ordered_hours = hours_list

    return ordered_hours
