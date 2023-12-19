# logic to scrape websites
# requests for static content and selenium for dynamic content

"""""""""
This file is responsible for fetching the html from a website.
This can be done through requests for static or selenium for dynamic

Once the content is fetched, you will call a function from content_parser.py to
parse the content
"""""""""


import requests
from selenium import webdriver
from content_parser import parse_html
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# old method, works with when hours are static
def scrape_website_no_selenium(url):
    response = requests.get(url)
    if response.status_code == 200:
        parsed_content = parse_html(response.text) # parse_html is a function from content_parser.py
        return parsed_content
    else:
        # handle HTTP errors or add logging
        return None

def scrape_website(url):
    driver = webdriver.Chrome()  
    driver.get(url)

    try:
        # Wait up to 10 seconds for the button or link to be present
        button_or_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'hours')] | //a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'hours')]"))
        )
        button_or_link.click()
    except:
        pass  # If the button is not found, continue with the scraping

    html = driver.page_source
    driver.quit()

    parsed_content = parse_html(html)
    return parsed_content



