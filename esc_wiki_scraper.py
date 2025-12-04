import requests
from bs4 import BeautifulSoup

def get_esc_participants_by_year(year: int, user_header: dict) -> list:
    url = f"https://en.wikipedia.org/api/rest_v1/page/html/Eurovision_Song_Contest_{year}"
    try:
        response = requests.get(url, headers=user_header)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        participants = None
        
        for table in soup.find_all("table"):
            caption = table.find("caption")

            if caption and "participants" in caption.get_text(strip=True).lower():
                participants = table
                break

        if not participants:
            raise ValueError("Participants table not found")
        
        rows = []

        for tbody in participants.find_all("tbody"):
            for tr in tbody.find_all("tr"):
                th = tr.find("th")
                tds = tr.find_all("td")

                # Skip any invalid rows
                if not th or len(tds) < 5:
                    continue

                country = th.get_text(strip=True)
                artist = tds[1].get_text(strip=True)
                song = tds[2].get_text(strip=True)
                rows.append({"country": country, "year": year, "artist": artist, "song_title": song})

        return rows

    except Exception as e:
        print(f"Participant retrieval failed for {year}.")
        return e


    


