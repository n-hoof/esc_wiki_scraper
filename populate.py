from esc_wiki_scraper import get_esc_participants_by_year, get_esc_scores_by_year_2023_2025, get_esc_scores_by_year_2010_2022
from esc_supabase_insert import insert_esc_entries, esc_entries_year_check, esc_scores_year_check, insert_esc_real_scores
from datetime import datetime

def populate_esc_entries(year: int, header: dict):
    is_year_populated = esc_entries_year_check(year)

    curr_year = datetime.now().year

    if year == curr_year and datetime.now().month < 5:
        print(f"Full data not retrievable until May for Eurovision {year}")
        return
    
    if year > curr_year:
        print(f"Eurovision {year} is too far in the future")
        return

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


def populate_esc_real_scores(year: int, header: dict):
    is_entries_year_populated = esc_entries_year_check(year)
    if not is_entries_year_populated:
        print(f"Entries have not been populated for {year}")
        return
    
    is_scores_year_populated = esc_scores_year_check(year)
    if is_scores_year_populated:
        print(f"Scores have already been populated for {year}")
        return
    
    if year <= 2025 and year >= 2023:
        scoring_data = get_esc_scores_by_year_2023_2025(year, header)

    elif year >= 2010 and year <= 2022:
        scoring_data = get_esc_scores_by_year_2010_2022(year, header)
    else:
        print(f"Scoring data retrieval has not been implemented for {year}")
        return
    response = insert_esc_real_scores(scoring_data, year)
    return response

#TODO: Implement
def populate_pze_real_scores():
    print("Not yet implemented")
    pass

def populate(year: int, table: str, header: dict):
    response = None
    
    match table:
        case "esc_entries":
            response = populate_esc_entries(year, header)

        case "esc_real_scores":
            response = populate_esc_real_scores(year, header)

        case "pze_entries":
            populate_pze_entries(year, header)

        case "pze_real_scores":
            populate_pze_real_scores()
            
        case _:
            print("Not a valid table")

    if response:
        return response