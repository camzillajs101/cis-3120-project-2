import pandas as pd

import requests
import json
from bs4 import BeautifulSoup

# --WEB SCRAPING PART--
scraping_url = "https://en.wikipedia.org/wiki/List_of_Major_League_Baseball_players_from_Puerto_Rico"
page = requests.get(scraping_url)

web_dict = {
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

web_df = pd.DataFrame(df_dict)

# --API PART--
scraping_url = "https://www.thesportsdb.com/api/v1/json/3/"
player_search_url = scraping_url + "searchplayers.php?p="
player_details_url = scraping_url + "lookupplayer.php?id="

api_dict = {
    "Result": [],
    "Number": [],
    "Position": [],
    "Height": [],
    "Weight": []
}

for player in df_dict["Name"][:30]:
    api_call_search = requests.get(player_search_url + player.replace(" ","_"))
    player_id = api_call_search.json()['player'][0]['idPlayer']
    
    api_call_details = requests.get(player_details_url + player_id)
    player_info = api_call_details.json()['players'][0]
    
    api_dict["Result"].append(player_info['strPlayer'])
    api_dict["Number"].append(player_info['strNumber'])
    api_dict["Position"].append(player_info['strPosition'])
    api_dict["Height"].append(player_info['strHeight'])
    api_dict["Weight"].append(player_info['strWeight'])

api_df = pd.DataFrame(api_dict)

# --COMBINATION--
combined_df = pd.concat([web_df.iloc[:30],api_df],axis=1)