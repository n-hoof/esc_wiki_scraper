import os
from dotenv import load_dotenv
from populate import populate
from esc_supabase_insert import fetch_country_ids

import time

load_dotenv()
user_agent: str = os.getenv("USER_AGENT")
header = {"User-Agent": f"ESCDataRetrieval/1.0 {user_agent}"}
table = "esc_real_scores"
country_ids = fetch_country_ids()

for year in range(2022, 2026):
    try:
        response = populate(year, table, header, country_ids)
        print(response)
        time.sleep(1)
    except Exception as e:
        print(e)