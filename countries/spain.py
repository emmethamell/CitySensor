from typing import List, Dict
from supabase import create_client, Client
from dotenv import load_dotenv
from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
import re


load_dotenv()
supabaseURL: str = os.environ.get("SUPABASE_URL")
service_role_key: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
supabase: Client = create_client(supabaseURL, service_role_key)

class Spain:
    
    @staticmethod
    def update_restaurants(links: List[str]):
        for link in links:
            content = Spain.scrape_website(link)
            existing = supabase.table('Spain').select('url').eq('url', link).execute().data
            current_time = datetime.now().isoformat()

            if existing:
                supabase.table('Spain').upsert({
                    'url': link,
                    'last_check': datetime.now().isoformat(),
                    'new_content': content          
                }).execute()

                # check if the old hours and new hours are different
                updated_website = supabase.table('Spain').select('old_content', 'new_content').eq('url', link).execute().data
                if updated_website:
                    first_website = updated_website[0]
                    if first_website['old_content'] != first_website['new_content']:
                        supabase.table('websites').update({
                            'alert': True
                        }).eq('url', link).execute()

            else:
                # query yelp api for the data and insert it into the database
                # get the yelp id, name, city, phone, and hours and add them along with other stuff
                
                supabase.table('Spain').insert({
                    'url': link,
                    'last_update': current_time,
                    'last_check': current_time,
                    'alert': False,
                    'old_content': content,
                    'new_content': content
                }).execute()



    #PARSE FOR PHONE NUMBER 
    #Takes: html, Returns: all instances of phone number
    @staticmethod
    def parse_phone_number(html):
        # Make sure that request was successful
        if html.startswith('Failed'):
            return html

        soup = BeautifulSoup(html, 'html.parser')

        # Strategy 1: See if there is href="tel:....."
        tel_links = soup.find_all('a', href=lambda href: href and href.startswith('tel:'))
        if tel_links:
            return [link['href'] for link in tel_links]
        
        # Strategy 2: look for phone number patterns
        text = soup.get_text(separator=' ')
        pattern = r'(\+\d{2}\s*\d{3}\s*\d{3}\s*\d{3})|(\d{2}\s*\d{3}\s*\d{2}\s*\d{2})|(\d{3}\s*\d{2}\s*\d{2}\s*\d{2})|(\d{9})|(\+\d{2})|\(\+\d{2}\)'
        phone_numbers = re.findall(pattern, text)
        return [''.join(num) for num in phone_numbers if any(num)]
    

        
    #PARSE FOR HOURS
    #Takes:html, Returns: all instances of opening hours
    @staticmethod
    def parse_hours(html):
        if html.startswith('Failed'):
            return html
        
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text(separator=' ')

        pattern = r'\d{1,2}[:]\d{2}'
        opening_hours = re.findall(pattern, text.replace(" ", ""))
        
        if opening_hours == []:
            pattern = r'\d{1,2}[.]\d{2}'
            opening_hours = re.findall (pattern, text.replace(" ", ""))
        
        return opening_hours
        
        


