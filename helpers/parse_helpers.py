import requests
from selenium import webdriver
class Helper:
    
    #RETRIEVE HTML
    #Takes: url, Returns: html or error message if fails
    @staticmethod
    def get_html(url):
        response = requests.get(url)

        if response.status_code == 200:
            html_content = response.text
            return html_content
        else:
            return Helper.get_html_selenium(url)
        
    @staticmethod
    def get_html_selenium(url):
            # Initialize the Chrome driver
        driver = webdriver.Chrome()
        driver.get(url)
        html_content = driver.page_source
        driver.quit()
        return html_content