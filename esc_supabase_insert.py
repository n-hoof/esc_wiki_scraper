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

def esc_scores_year_check(year: int) -> bool:
    try:
        response = (
            sb.table("esc_entries")
            .select("id")
            .eq("year", year)
            .limit(1)
            .execute()
        )

        entry_id = response.data[0]["id"]

        response = (
            sb.table("esc_real_scores")
            .select("*")
            .eq("entry_id", entry_id)
            .limit(1)
            .execute()
        )

        if len(response.data) > 0:
            return True
        
        False

    except Exception as e:
        return e

def insert_esc_entries(entry_data: list):
    try:
        response = (
            sb.table("esc_entries")
            .insert(entry_data)
            .execute()
        )
        return response
    
    except Exception as e:
        return e

def fetch_entry_ids_by_year(year: int) -> dict:
    try:
        response = (
            sb.table("esc_entries")
            .select("country, id")
            .eq("year", year)
            .execute()
        )

        entry_ids = {}

        for row in response.data:
            country = row["country"]
            entry_id = row["id"]
            entry_ids[country] = entry_id

        return entry_ids

    except Exception as e:
        return e
    
def insert_esc_real_scores(scoring_data: dict, year: int):
    rows = []
    entry_ids = fetch_entry_ids_by_year(year)

    for country, data in scoring_data.items():
        entry_id = entry_ids[country]
        for row in data:
            row["entry_id"] = entry_id
            rows.append(row)

    try:
        response = (
            sb.table("esc_real_scores")
            .insert(rows)
            .execute()
        )
        return response
    
    except Exception as e:
        return e

    