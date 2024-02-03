# database interactions, models, and utilities
import os
from supabase import create_client, Client
from dotenv import load_dotenv
from scraper.site_scraper import scrape_website
from datetime import datetime
from typing import List, Dict
from helpers.parse_helpers import Helper
from countries.spain import Spain
import json
from travel_advisories.scraper import TravelAdvisory

load_dotenv()
supabaseURL: str = os.environ.get("SUPABASE_URL")
service_role_key: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
supabase: Client = create_client(supabaseURL, service_role_key)


def update_database_spain(links: List[str], city: str, subtype: str):
    for link in links:
        html = Helper.get_html_selenium(link)
        phone = Spain.parse_phone_number(html) # list
        hours = Spain.parse_hours(html) #list
        
        # Here if phone or hours are empty, try to use selenium scraper that looks around site for hours and phone numbers
        if not phone or not hours:
            child_pages_content = Helper.get_all_html(link)
            for page in child_pages_content:
                phone = Spain.parse_phone_number(page) 
                hours = Spain.parse_hours(page) 
        
        new_content = {
            "phone": phone,
            "hours": hours
        }
        
        current_time = datetime.now().isoformat()
        existing = supabase.table('spain').select('url').eq('url', link).execute().data
        if existing:
            supabase.table('spain').upsert({
                'url': link,
                'location': city,
                'subtype': subtype,
                'last_check': current_time,
                'new_content': new_content
            }).execute()
            #pull the old_content and new_content
            updated = supabase.table('spain').select('old_content', 'new_content').eq('url', link).execute().data
            if updated:
                content = updated[0]
                old_content = content['old_content']
                new_content = content['new_content']
                alert = create_alert(old_content, new_content)
                #if the alert is not None, update the "alert_text" with the alert
                #and the "alert" to true
                if alert['hours'] != False or alert['phone'] != False:
                    supabase.table('spain').update({
                        'alert': True,
                        'alert_text': alert
                    }).eq('url', link).execute()
        else: 
            supabase.table('spain').insert({
                'url': link,
                'location': city,
                'subtype': subtype,
                'last_update': current_time,
                'last_check': current_time,
                'alert': False,
                'new_content': new_content,
                'old_content': new_content
                
            }).execute()
            

"""""""""
* Takes: old_content(json) and new_content(json).
* Checks if their "hours" and "phone" attributes are different and
  creates the change alert
* Returns: the change alert, which is NULL (None) if there was no change
"""""""""
"""""""""
{
    hours: ['12:00', '15:00']
    phone: ['+34 123 456 789']
}
"""""""""
def create_alert(old_content, new_content):
    alert = {'hours': False, 'phone': False}
    if old_content['hours'] != new_content['hours']:
        alert['hours'] = True
    if old_content['phone'] != new_content['phone']:
        alert['phone'] = True
    return alert
    
def update_database(links):
    for link in links:
        hours = scrape_website(link)
        existing = supabase.table('websites').select('url').eq('url', link).execute().data
        current_time = datetime.now().isoformat()
        if existing:
            supabase.table('websites').upsert({
                'url': link,
                'last_check': datetime.now().isoformat(),
                'new_hours': hours           
            }).execute()

            # check if the old hours and new hours are different
            updated_website = supabase.table('websites').select('old_hours', 'new_hours').eq('url', link).execute().data
            if updated_website:
                first_website = updated_website[0]
                if first_website['old_hours'] != first_website['new_hours']:
                    supabase.table('websites').update({
                        'alert': True
                    }).eq('url', link).execute()

        else:
            supabase.table('websites').insert({
                'url': link,
                'last_update': current_time,
                'last_check': current_time,
                'alert': False,
                'old_hours': hours,
                'new_hours': hours
            }).execute()
        
def update_travel_advisories():
    contentList = TravelAdvisory.scrape_website()
    print(contentList)
    # item = [country, level, date, summary]
    for item in contentList:
        supabase.table('travel_advisories').upsert({
            'country': item[0],
            'level': item[1],
            'date_updated': item[2],
            'summary': item[3]
        }).execute()

def get_travel_advisory(country):
    result = supabase.table('travel_advisories').select('*').ilike('country', f'%{country}%').execute() 
    if result:       
        data = result.data
        if not data:
            return "Nothing found"
        data_json = data[0]
        return data_json
    else:
        return "Nothing found"

#Return all json format list of objects with link and alert
def get_updates_spain(city):
    businesses = supabase.table('spain').select('url', 'alert_text').ilike('location', city).eq('alert', True).execute()
    return businesses
        