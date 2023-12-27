# database interactions, models, and utilities
import os
from supabase import create_client, Client
from dotenv import load_dotenv
import sys
sys.path.append('/Users/emmethamell/Desktop/CitySensor/scraper')
from site_scraper import scrape_website
from parse_from_google import parse_google_hours, scrape_website_google

from datetime import datetime

load_dotenv()


supabaseURL: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
service_role_key: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
supabase: Client = create_client(supabaseURL, service_role_key)



# function that takes in a list of links, and updates database accordingly
def update_database(links):
    for link in links:
        hours = scrape_website_google(link)

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
        

list_of_links = [
    "https://www.google.com/search?q=savinos+belmont&hl=en",
    "https://www.google.com/search?q=spoke+wine+bar+belmont&hl=en",
    "https://www.google.com/search?q=my+other+kitchen+belmont&hl=en"
]


