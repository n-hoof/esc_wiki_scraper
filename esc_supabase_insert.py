import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
sb_url: str = os.getenv("SUPABASE_URL")
sb_key: str = os.getenv("SUPABASE_KEY")
sb: Client = create_client(sb_url, sb_key)

def esc_entries_year_check(year: int) -> bool:
    try:
        response = (
            sb.table("esc_entries")
            .select("year")
            .eq("year", year)
            .limit(1)
            .execute()
        )

        if len(response.data) > 0:
            return True
        
        return False
    
    except Exception as e:
        return e

def insert_esc_entries(entry_data: list):
    try:
        response = (sb.table("esc_entries").insert(entry_data).execute())
        return response
    
    except Exception as e:
        return e