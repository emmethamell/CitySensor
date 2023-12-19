# database interactions, models, and utilities
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
supabaseURL: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabaseURL, key)

# remember you need to update policies to read and write to table
#TEST
response = supabase.table('websites').select('url').execute()
print(response.data)

# add functionality to read and write to database
# create functions like such

"""""""""
class Database:
    def __init__(self, url: str, key: str):
        self.supabase: Client = create_client(url, key)

    def fetch_website_data(self, url: str):
        query = self.supabase.table("Websites").select("*").eq("url", url).execute()
        return query.data

    def update_website_data(self, website_id: int, data: dict):
        self.supabase.table("Websites").update(data).eq("website_id", website_id).execute()

    def insert_new_website(self, data: dict):
        self.supabase.table("Websites").insert(data).execute()
"""""""""