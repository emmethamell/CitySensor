import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urljoin, urlparse

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
        
        
    #TODO: make the webdrive wait for dynamic content to load
    @staticmethod
    def get_html_selenium(url):
            # Initialize the Chrome driver
        driver = webdriver.Chrome()
        driver.get(url)
        html_content = driver.page_source
        driver.quit()
        return html_content
    
    
    #Try retrieving the html for the web page but also all of the child pages
    #returns a list with html from each child page
    @staticmethod
    def get_all_html(url):
        driver = webdriver.Chrome()
        driver.get(url)
    
        #find child page links
        anchors = driver.find_elements(By.TAG_NAME, 'a')
        child_page_urls = [urljoin(url, anchor.get_attribute('href')) for anchor in anchors]
    
        #fetch and store html from child pages
        child_pages_content = []
        for child_url in child_page_urls:
            try:
                result = urlparse(child_url)
                # Check if the URL is valid by checking if it has a network location (netloc) and a scheme (like http or https)
                if all([result.scheme, result.netloc]):
                    driver.get(child_url)
                    child_pages_content.append(driver.page_source)
                else:
                    print(f"Skipping invalid URL: {child_url}")
            except Exception as e:
                print(f"Error occurred while processing URL {child_url}: {str(e)}")
            
        driver.close()
        driver.quit()
        
        return child_pages_content
        
            
        