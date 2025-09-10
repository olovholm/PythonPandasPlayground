import requests
import os
import json
from common import DATA_RAW


BASE_URL = "https://valgresultat.no/api"
DATA_DIR = os.path.join(DATA_RAW,"norwegian_elections")
os.makedirs(DATA_DIR, exist_ok=True)


def get_election_urls():
    metadata_resp = requests.get(f"{BASE_URL}")
    metadata = metadata_resp.json()

    sublinks = metadata["_sublinks"]
    years = list(sublinks.keys())

    election_urls = []
    for year in years:
        st_items = list(filter(lambda x: x["navn"] == "st", sublinks[year]))
        if st_items:
            stortings_urls = st_items[0]["href"]
            election_urls.append(f"{BASE_URL}{stortings_urls}")
    return election_urls


def get_related_links(payload):
    urls = []
    for element in payload['_links']['related']:
        path = element['href'].lstrip('/')
        urls.append(f"{BASE_URL}/{path}")

    return urls

def save_election_data(year, data):
    filename = os.path.join(DATA_DIR, f"election_results_{year}.json")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Saved election data for year {year} to {filename}")

def save_countydata(year, county_url, data):
    year_dir = os.path.join(DATA_DIR, str(year))
    os.makedirs(year_dir, exist_ok=True)
    county_path = county_url.replace(f"{BASE_URL}/", "")
    out_path = os.path.join(year_dir, f"{county_path.replace('/', '_')}.json")
    with open(out_path, 'w', encoding="utf-8") as out_f:
        json.dump(data, out_f, ensure_ascii=False, indent=4)
    print(f"Saved county data for year {year} to {out_path}")

def save_municipality_data(year, county_nr, muni_nr, data):
    year_dir = os.path.join(DATA_DIR, str(year), str(county_nr))
    os.makedirs(year_dir, exist_ok=True)
    out_path = os.path.join(year_dir, f"{muni_nr}.json")
    with open(out_path, 'w', encoding="utf-8") as out_f:
        json.dump(data, out_f, ensure_ascii=False, indent=4)
    print(f"Saved municipality data for year {year}, county {county_nr}, municipality {muni_nr} to {out_path}")




election_urls = get_election_urls()
county_links = list()

election_metadata = []

for election_url in election_urls:
    print("Fetching election data from:", election_url)
    year_data_resp = requests.get(election_url)
    year_data = year_data_resp.json()

    year = year_data["id"]["valgaar"]
    save_election_data(year, year_data)
    county_links.append({"year": year, "links": get_related_links(year_data)})



 # Replace with the actual base URL
municipality_links = list()

for element in county_links:
    print(f"Fetching county data from: {element["year"]}")
    for link in element["links"]:
        county_resp = requests.get(link)
        if county_resp.status_code == 200:
            county_data = county_resp.json()
            year = county_data["id"]["valgaar"]
            county_nr = county_data["id"]["nr"]
            year_dir = os.path.join(DATA_DIR, str(year))
            save_countydata(year, link, county_data)
            municipality_links.append({"year": year, "county_id": county_nr, "links" : get_related_links(county_data)})
        else:
            print(f"Failed to download {link}")


for element in municipality_links:
    print(f"Fetching municipality data from: {element['year']} for county {element['county_id']}")
    for link in element["links"]:
        muni_resp = requests.get(link)
        if muni_resp.status_code == 200:
            muni_data = muni_resp.json()
            year = muni_data["id"]["valgaar"]
            muni_nr = muni_data["id"]["nr"]
            save_municipality_data(year, element['county_id'], muni_nr, muni_data)
        else:
            print(f"Failed to download {link}")
