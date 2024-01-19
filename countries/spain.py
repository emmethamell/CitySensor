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
        
        


