from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

"""""""""
Get the html for each page in the travel advisories website
"""""""""
class TravelAdvisory:
    
    """""""""
    def scrape_website():
        driver = webdriver.Chrome()
        driver.get("https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories.html/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "paginate_button")))
        
        page_numbers = driver.find_elements(By.CLASS_NAME, "paginate_button")
        number_of_buttons = len(page_numbers)
        
        for i in range(2, number_of_buttons + 1):
            WebDriverWait(driver, 10).until(
                lambda d: d.find_element(By.XPATH, f"//a[contains(@class, 'paginate_button') and text()='{str(i)}']").is_displayed()
            )
            xpath = f"//a[contains(@class, 'paginate_button') and text()='{str(i)}']"
            element = driver.find_element(By.XPATH, xpath)
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()

            # Wait for a short period to ensure the page has loaded
            time.sleep(15)  

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
        
            first_row_display = soup.find(class_="rowDisplay")
            if first_row_display:
                print("First 'rowDisplay' element on this page:", first_row_display)
            else:
                print("No 'rowDisplay' element found on this page.")

        driver.quit()
        """""""""
        
    """""""""
    Takes: nothing (the url is the same always)
    Returns: a list of lists EX [ [country, level, date, summary], etc. etc.]
    """""""""
    @staticmethod
    def scrape_website():
        base_url = "https://travel.state.gov"
        response = requests.get("https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories.html/")
        
        return_list = []
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            rows = soup.find_all('tr')
           
            for row in rows:
                data = row.find_all('td')
                
                data_text = [td.text for td in data]
                
                link = row.find('a')
                
                if link and link.get('href'):
                    link_url = base_url + link['href']
                    summary = TravelAdvisory.scrape_advisory_page(link_url)
                    
                    data_text.append(summary)
                    return_list.append(data_text)
        else:
            print("Error:", response.status_code)
        
        # call clean content before returning
        return TravelAdvisory.clean_content(return_list)
    
    
    
    @staticmethod
    def scrape_advisory_page(url):
        try:
            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
        
            summary_tag = soup.find('b', string=lambda text: 'summary' in text.lower())
        
            if summary_tag and summary_tag.parent.name == 'p':
                return summary_tag.parent.text.strip()
        
            return 'N/A'
        except:
            return 'N/A'
          
    @staticmethod
    def clean_content(content_list):
        new_list = []
        for item in content_list:
            if 'Travel' in item[0]:
                words = item[0].split()
                index = words.index('Travel')
                country = ' '.join(words[:index])
                new_list.append([country, item[1], item[2], item[3]])
        return new_list
                
               
            
        
        
        
        