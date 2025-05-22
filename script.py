import pandas as pd

import requests
import json
from bs4 import BeautifulSoup

scraping_url = "https://en.wikipedia.org/wiki/List_of_Major_League_Baseball_players_from_Puerto_Rico"
page = requests.get(scraping_url)

df_dict = {
    "Name": [],
    "Team": [],
    "Years": []
}

if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')
    table_tag = soup.find('table',class_="wikitable").find('tbody')
    for tr in table_tag.find_all('tr'):
        cols = tr.find_all('td')
        if len(cols) > 0: # exclude header row (has no td tags)
            df_dict["Name"].append(cols[0].text[:-1])
            df_dict["Team"].append(cols[1].text[:-1])
            df_dict["Years"].append(cols[2].text[:-1])
else:
    print("API error")
