from esc_wiki_scraper import get_esc_participants_by_year, get_esc_scores_by_year_2023_2025
from esc_supabase_insert import insert_esc_entries, esc_entries_year_check, esc_scores_year_check, insert_esc_real_scores
import os
from dotenv import load_dotenv

def populate_esc_entries(year: int, header: dict):
    is_year_populated = esc_entries_year_check(year)

    if is_year_populated:
        print(f"Table has already been populated for {year}")
        return

    esc_entry_data = get_esc_participants_by_year(year, header)
    response = insert_esc_entries(esc_entry_data)
    return response

#TODO: Implement
def populate_pze_entries(year: int, header: dict):
    print("Not yet implemented")
    pass

#TODO: Implement
def populate_esc_real_scores(year: int, header: dict):
    is_entries_year_populated = esc_entries_year_check(year)
    if not is_entries_year_populated:
        print(f"Entries have not been populated for {year}")
        return
    
    is_scores_year_populated = esc_scores_year_check(year)
    if is_scores_year_populated:
        print(f"Scores have already been populated for {year}")
        return
    
    scoring_data = get_esc_scores_by_year_2023_2025(year, header)
    response = insert_esc_real_scores(scoring_data, year)
    return response
    

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
    table = "esc_real_scores"

    match table:
        case "esc_entries":
            response = populate_esc_entries(year, header)
            print(response)

        case "esc_real_scores":
            response = populate_esc_real_scores(year, header)
            print(response)

        case "pze_entries":
            populate_pze_entries(year, header)

        case "pze_real_scores":
            populate_pze_real_scores()
            
        case _:
            print("Not a valid table")