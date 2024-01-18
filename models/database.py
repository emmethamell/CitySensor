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


"""""""""
* Takes: list of links, city name, and subtype.
* For each link:
  * Upsert the row with the primary key 'link', location (if it exists), subtype (if it exists),
      last-check (now), and new content
  * Extract new-content(JSON) and old-content(JSON), see if they are different:
  * If yes:
    * Check to see if the "hours" are different, if yes add to alert obj "hours have changed"
    * Check to see if the "phone" are different, if yes add to alert obj "phone has changed"
    * Upsert the alert_text with this
"""""""""
def update_database_spain(links: List[str], city: str, subtype: str):
    for link in links:
        html = Helper.get_html(link)
        phone = Spain.parse_phone_number(html) # list
        hours = Spain.parse_hours(html) #list
        
        new_content = {
            "phone": phone,
            "hours": hours
        }
        new_content = json.dumps(new_content)
        
        current_time = datetime.now().isoformat()
        existing = supabase.table('Spain').select('url').eq('url', link).execute().data
        if existing:
            supabase.table('Spain').upsert({
                'url': link,
                'location': city,
                'subtype': subtype,
                'last_check': current_time,
                'new_content': new_content
            }).execute()
            #pull the old_content and new_content
            updated = supabase.table('Spain').select('old_content', 'new_content').eq('url', link).execute().data
            if updated:
                alert = create_alert(updated[0], updated[1])
                #if the alert is not None, update the "alert_text" with the alert
                #and the "alert" to true
                if alert['hours'] != False or alert['phone'] != False:
                    supabase.table('Spain').update({
                        'alert': True,
                        'alert_text': alert
                    }).eq('url', link).execute()
        else: #the link does not exist in the table yet
            supabase.table('Spain').insert({
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

        


