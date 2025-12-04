from esc_wiki_scraper import get_esc_participants_by_year
from esc_supabase_insert import insert_esc_entries, esc_entries_year_check
import os
from dotenv import load_dotenv

def populate_esc_entries(year: int, header: dict):
    is_year_populated = esc_entries_year_check(year)

    if is_year_populated:
        print(f"Table has already been populated for the year {year}")

    else:
        esc_entry_data = get_esc_participants_by_year(year, header)
        response = insert_esc_entries(esc_entry_data)
        print(response)

#TODO: Implement
def populate_pze_entries(year: int, header: dict):
    print("Not yet implemented")
    pass

#TODO: Implement
def populate_esc_real_scores():
    print("Not yet implemented")
    pass

#TODO: Implement
def populate_pze_real_scores():
    print("Not yet implemented")
    pass

if __name__ == "__main__":

    # Load personal email/website for contact if necessary
    load_dotenv()
    user_agent: str = os.getenv("USER_AGENT")

    # Change these variables as desired
    year = 2025
    header = {"User-Agent": f"ESCDataRetrieval/1.0 {user_agent}"}
    table = "esc_entries"

    match table:
        case "esc_entries":
            populate_esc_entries(year, header)

        case "esc_real_scores":
            populate_esc_real_scores()

        case "pze_entries":
            populate_pze_entries(year, header)

        case "pze_real_scores":
            populate_pze_real_scores()
            
        case _:
            print("Not a valid table")