# (In Progress) Eurovision Data Scraper
A python script which scrapes Eurovision data from Wikipedia's REST API and inserts into a postgres supabase table.

### Current Functions
- Gathers country, artist, and song title information for each participating act in ESC for a desired year
- Inserts this data into a postgres supabase table of the format:

        id | country | artist | song_title | year
        -----------------------------------------

    (id is an auto-generated integer)

- Gathers voting, running order and placement data for each entry in a desired year of ESC for the semi's and the final
- Inserts this data into a postgres supabase table of the format:
       
        id | entry_id | jury | televote | is_final | place | running_order
        ------------------------------------------------------------------

    

### Planned Functions
- Gather and insert participant data for Serbia's national contest, Pesma Za Evroviziju (PZE)
- Gather and insert scoring and placement data for each entry in a desired year of PZE