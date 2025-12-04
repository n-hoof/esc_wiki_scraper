# (In Progress) Eurovision Data Scraper
A python script which scrapes Eurovision data from Wikipedia's REST API and inserts into a postgres supabase table.

### Current Functions
- Gathers country, artist, and song title information for each participating act in ESC for a desired year
- Inserts this data into a postgres supabase database of the format:

        id | country | artist | song_title | year
        -----------------------------------------

    (id is an auto-generated integer)

### Planned Functions
- Gather and insert participant data for Serbia's national contest, Pesma Za Evroviziju (PZE)
- Gather and insert scoring and placement data for each entry in a desired year of ESC
- Gather and insert scoring and placement data for each entry in a desired year of PZE