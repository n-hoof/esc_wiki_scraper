import requests
from bs4 import BeautifulSoup
from collections import defaultdict

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

# 2026-?
# semis = jury + televote
# final = jury + televote
def get_esc_scores_by_year_2026(year: int, user_header: dict) -> list:
    pass

# 2023-2025
# semis = televote
# final = jury + televote
def get_esc_scores_by_year_2023_2025(year: int, user_header: dict) -> dict:
    url = f"https://en.wikipedia.org/api/rest_v1/page/html/Eurovision_Song_Contest_{year}"
    try:
        response = requests.get(url, headers=user_header)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        semi_1 = None
        semi_2 = None
        final_ro_place = None
        final_score = None

        for table in soup.find_all("table"):
            caption = table.find("caption")

            if caption:
                if "First semi-final of the Eurovision Song Contest" in caption.get_text(strip=True):
                    semi_1 = table
                elif "Second semi-final of the Eurovision Song Contest" in caption.get_text(strip=True):
                    semi_2 = table
                elif "Final of the Eurovision Song Contest" in caption.get_text(strip=True):
                    final_ro_place = table
                elif "Detailed jury voting results of the final of the Eurovision Song Contest" in caption.get_text(strip=True):
                    final_score = table

            if semi_1 and semi_2 and final_ro_place and final_score:
                break

        if not semi_1:
            raise ValueError("First semi-final table not found")
        
        if not semi_2:
            raise ValueError("Second semi-final table not found")
        
        if not final_ro_place:
            raise ValueError("Final table not found")
        
        if not final_score:
            raise ValueError("Detailed final voting table not found")
        
        scoring_data = defaultdict(list)

        for tr in semi_1.find_all("tr")[1:]:
            th = tr.find("th")
            tds = tr.find_all("td")

            run_order = th.get_text(strip=True)
            run_order = int(run_order) if run_order.isnumeric() else None

            country = tds[0].get_text(strip=True)

            tele = tds[3].get_text(strip=True)
            tele = int(tele) if tele.isnumeric() else None

            place = tds[4].get_text(strip=True)
            place = int(place) if place.isnumeric() else None

            scoring_data[country].append({"is_final": False, "televote": tele, "place": place, "running_order": run_order})

        for tr in semi_2.find_all("tr")[1:]:
            th = tr.find("th")
            tds = tr.find_all("td")

            run_order = th.get_text(strip=True)
            run_order = int(run_order) if run_order.isnumeric() else None

            country = tds[0].get_text(strip=True)

            tele = tds[3].get_text(strip=True)
            tele = int(tele) if tele.isnumeric() else None

            place = tds[4].get_text(strip=True)
            place = int(place) if place.isnumeric() else None

            scoring_data[country].append({"is_final": False, "televote": tele, "place": place, "running_order": run_order})

        for tr in final_ro_place.find_all("tr")[1:]:
            th = tr.find("th")
            tds = tr.find_all("td")

            country = tds[0].get_text(strip=True)

            run_order = th.get_text(strip=True)
            run_order = int(run_order) if run_order.isnumeric() else None

            place = tds[4].get_text(strip=True)
            place = int(place) if place.isnumeric() else None

            scoring_data[country].append({"is_final": True, "running_order": run_order, "place": place})

        for tr in final_score.find_all("tr")[3:]:
            th = tr.find_all("th")
            if len(th) > 1:
                th = th[1]
            else:
                th = th[0]
            tds = tr.find_all("td")

            country = th.get_text(strip=True)
            
            jury = tds[1].get_text(strip=True)
            jury = int(jury) if jury.isnumeric() else None

            tele = tds[2].get_text(strip=True)
            tele = int(tele) if tele.isnumeric() else None

            scoring_data[country][-1]["jury"] = jury
            scoring_data[country][-1]["televote"] = tele

        return scoring_data

    
    except Exception as e:
        print(f"Scoring data retrieval failed for {year}.")
        return e

# 2009-2022
# semis = televote + jury
# final = televote + jury
def get_esc_scores_by_year_2009_2022(year: int, user_header: dict) -> list:
    pass  


