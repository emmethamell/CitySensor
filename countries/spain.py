from typing import List, Dict

class Spain:
    @staticmethod
    def update_restaurants(links: List[str]):
        # Your implementation here
        for link in links:
            content = Spain.scrape_website(link)
            existing = supabase.table('websites').select('url').eq('url', link).execute().data
            current_time = datetime.now().isoformat()

            if existing:
                supabase.table('websites').upsert({
                    'url': link,
                    'last_check': datetime.now().isoformat(),
                    'new_content': content          
                }).execute()

                # check if the old hours and new hours are different
                updated_website = supabase.table('websites').select('old_content', 'new_content').eq('url', link).execute().data
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
                    'old_content': content,
                    'new_content': content
                }).execute()

    @staticmethod
    def scrape_website(link: str):
        # Your implementation here
        pass


"""""""""
* Scrape content from webpage
* Parse and clean content a bit, try and get phone number and hours
* If existing:
  * upsert with new content and last_check
  * check if old content and new content are different
    * If different, set alert to true
* else: 
  * NEW: call the yelp api for all the content needed, filling the database with the new content
  * also, fill the database the the last_update, last_check, alert, old_content, new_content 
"""""""""