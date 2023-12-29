"""""""""
This file is responsible for fetching the html from a website.
This can be done through requests for static or selenium for dynamic

Once the content is fetched, you will call a function from content_parser.py to
parse the content
"""""""""


import requests
from selenium import webdriver
from content_parser import parse_html
from hours_parser import parse_hours
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# old method, works with when hours are shown on the html of exact url
def scrape_website_no_selenium(url):
    response = requests.get(url)
    if response.status_code == 200:
        parsed_content = parse_html(response.text)
        return parsed_content
    else:
        return None


def scrape_website(url):
    driver = webdriver.Chrome()  
    driver.get(url)

    try:
        button_or_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'hours')] | //a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'hours')]"))
        )
        button_or_link.click()
    except:
        pass 

    html = driver.page_source
    driver.quit()

    parsed_content = parse_html(html)

    hours = parse_hours(parsed_content)

    return hours



