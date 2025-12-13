import os
from dotenv import load_dotenv
from populate import populate

import time

load_dotenv()
user_agent: str = os.getenv("USER_AGENT")
header = {"User-Agent": f"ESCDataRetrieval/1.0 {user_agent}"}
table = "esc_entries"

for year in range(2009, 2016):
    try:
        response = populate(year, table, header)
        print(response)
        time.sleep(10)
    except Exception as e:
        print(e)