import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

mens_swimming_urls = {
    "College of Staten Island": "https://csidolphins.com/sports/mens-swimming-and-diving/roster",
    "York College": "https://yorkathletics.com/sports/mens-swimming-and-diving/roster",
    "Baruch College": "https://athletics.baruch.cuny.edu/sports/mens-swimming-and-diving/roster",
    "Brooklyn College": "https://www.brooklyncollegeathletics.com/sports/mens-swimming-and-diving/roster",
    "Lindenwood University": "https://lindenwoodlions.com/sports/mens-swimming-and-diving/roster",
    "Mckendree University": "https://mckbearcats.com/sports/mens-swimming-and-diving/roster",
    "Ramapo College": "https://ramapoathletics.com/sports/mens-swimming-and-diving/roster",
    "SUNY Oneonta": "https://oneontaathletics.com/sports/mens-swimming-and-diving/roster",
    "SUNY Binghamton": "https://bubearcats.com/sports/mens-swimming-and-diving/roster/2021-22",
    "Albright College": "https://albrightathletics.com/sports/mens-swimming-and-diving/roster/2021-22",
}

womens_swimming_urls = {
    "College of Staten Island": "https://csidolphins.com/sports/womens-swimming-and-diving/roster",
    "Queens College": "https://queensknights.com/sports/womens-swimming-and-diving/roster",
    "York College": "https://yorkathletics.com/sports/womens-swimming-and-diving/roster",
    "Baruch College": "https://athletics.baruch.cuny.edu/sports/womens-swimming-and-diving/roster/2021-22?path=wswim",
    "Brooklyn College": "https://www.brooklyncollegeathletics.com/sports/womens-swimming-and-diving/roster",
    "Lindenwood University": "https://lindenwoodlions.com/sports/womens-swimming-and-diving/roster",
    "Mckendree University": "https://mckbearcats.com/sports/womens-swimming-and-diving/roster",
    "Ramapo College": "https://ramapoathletics.com/sports/womens-swimming-and-diving/roster",
    "Kean University": "https://keanathletics.com/sports/womens-swimming-and-diving/roster",
    "SUNY Oneonta": "https://oneontaathletics.com/sports/womens-swimming-and-diving/roster"
}

mens_volleyball_urls = {
    "City College of New York": "https://ccnyathletics.com/sports/mens-volleyball/roster",
    "Lehman College": "https://lehmanathletics.com/sports/mens-volleyball/roster",
    "Brooklyn College": "https://www.brooklyncollegeathletics.com/sports/mens-volleyball/roster",
    "John Jay College": "https://johnjayathletics.com/sports/mens-volleyball/roster",
    "Baruch College": "https://athletics.baruch.cuny.edu/sports/mens-volleyball/roster",
    "Medgar Evers College": "https://mecathletics.com/sports/mens-volleyball/roster",
    "Hunter College": "https://www.huntercollegeathletics.com/sports/mens-volleyball/roster",
    "York College": "https://yorkathletics.com/sports/mens-volleyball/roster",
    "Ball State": "https://ballstatesports.com/sports/mens-volleyball/roster"
}

womens_volleyball_urls = {
    "BMCC": "https://bmccathletics.com/sports/womens-volleyball/roster",
    "York College": "https://yorkathletics.com/sports/womens-volleyball/roster",
    "Hostos CC": "https://hostosathletics.com/sports/womens-volleyball/roster",
    "Bronx CC": "https://bronxbroncos.com/sports/womens-volleyball/roster/2021",
    "Queens College": "https://queensknights.com/sports/womens-volleyball/roster",
    "Augusta College": "https://augustajags.com/sports/wvball/roster",
    "Flagler College": "https://flaglerathletics.com/sports/womens-volleyball/roster",
    "USC Aiken": "https://pacersports.com/sports/womens-volleyball/roster",
    "Penn State - Lock Haven": "https://www.golhu.com/sports/womens-volleyball/roster"
}

def process_data(school_url_dict):
    '''
    Receives a dictionary: {school_name: url, ...}
    Returns a DataFrame and the average height
    '''
    #created three empty lists where we will append names, height and school names 
    #into a list. 
    names = []
    heights = []
    schools = []

    # In the for loop we are passing the values of school and url thorugh our function
    #this function is made to iterate all values from the dictionaries.

    for school, url in school_url_dict.items():
        page = requests.get(url)
        print(page.status_code) 

        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')

            #Since the html files are done by the same company, all tags are the same. and we use the .find_all method to
            #get all the values that are in 'td' <tag> and calles "side-are-table-player-name and" "heig
            
            name_tags = soup.find_all('td', class_='sidearm-table-player-name')
            height_tags = soup.find_all('td', class_='height')
            
            # Zip the name and height tags together to pair each player with their height
            for name_tag, height_tag in zip(name_tags, height_tags):
                name = name_tag.get_text(strip=True)
                raw_height = height_tag.get_text(strip=True)

                # We use try and accept to pass the function or skip if reqs are not met
                try:
                    feet, inches = raw_height.split('-')
                    height_in_inches = int(feet) * 12 + int(inches)

                    names.append(name)
                    heights.append(height_in_inches)
                    schools.append(school)
                except:
                    continue  # Skip malformed height
    #Created a DataFrame to incorporate all the data.
    data = {
        'School': schools,
        'Name': names,
        'Height (inches)': heights
    }

    df = pd.DataFrame(data)
    avg_height = df['Height (inches)'].mean()
    return df, avg_height

    #We're processing mens swimming data, saing to a csv file and printing the value.
mens_swimming_df, mens_swimming_avg = process_data(mens_swimming_urls)
mens_swimming_df.to_csv("mens_swimming.csv", index=False)
print(f"Men's Swimming Average Height: {mens_swimming_avg} inches")

#we are reusing the code above, to do the same for the womens swimming and mens women and
#volleyball team respectively.
women_swimming_df, women_swimming_avg = process_data(womens_swimming_urls)
women_swimming_df.to_csv("womens_swimming.csv", index=False)
print(f"Womens's Swimming Average Height: {women_swimming_avg} inches")

mens_volleyball_df, mens_volleyball_avg = process_data(mens_volleyball_urls)
mens_volleyball_df.to_csv("mens_volleyball.csv", index=False)
print(f"Men's Swimming Volleyball Height: {mens_volleyball_avg} inches")

women_volleyball_df, women_volleyball_avg = process_data(womens_volleyball_urls)
women_volleyball_df.to_csv("womens_volleyball.csv", index=False)
print(f"Womens's Volleyball Average Height: {women_volleyball_avg} inches")

