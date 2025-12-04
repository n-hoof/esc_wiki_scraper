import requests
from bs4 import BeautifulSoup

year = 2025
url = f"https://en.wikipedia.org/api/rest_v1/page/html/Eurovision_Song_Contest_{year}"
header = {"User-Agent": "ESCDataRetrieval/1.0 (https://github.com/n-hoof)"} 

try:
    response = requests.get(url, headers=header).text
    soup = BeautifulSoup(response, "html.parser")

    participants = None
    
    for table in soup.find_all("table"):
        caption = table.find("caption")

        if caption and "participants" in caption.get_text(strip=True).lower():
            participants = table
            break

    if not participants:
        raise ValueError("Participants table not found")
    
    rows = []
    header_row = participants.find("tr")
    headers = [th.get_text(strip=True) for th in header_row.find_all("th")]
    countries = [th.get_text(strip=True) for th in participants.find_all("th")][7:]

    artist_index = 1
    song_index = 2
    country_index = 0

    rows = []
    for tr in participants.find_all("tr")[1:]:
        tds = tr.find_all("td")
        row = {}
        row["country"] = countries[country_index]
        row["artist"] = tds[1].get_text(strip=True)
        row["song_title"] = tds[2].get_text(strip=True)
        row["year"] = year
        rows.append(row)
        country_index += 1
    
    print(rows)

except:
    print("Parsing failed.")

