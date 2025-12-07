import esc_supabase_insert
import esc_wiki_scraper
import os
from dotenv import load_dotenv

if __name__ == "__main__":
     # Load personal email/website for contact if necessary
    load_dotenv()
    user_agent: str = os.getenv("USER_AGENT")

    # Change these variables as desired
    year = 2010
    header = {"User-Agent": f"ESCDataRetrieval/1.0 {user_agent}"}

    response = esc_wiki_scraper.get_esc_scores_by_year_2010_2022(year, header)
    print(response)
    print(len(response))