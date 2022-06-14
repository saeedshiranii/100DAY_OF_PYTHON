from bs4 import BeautifulSoup
import requests


def data_scraper():
    
    # get a date for scraping songs in billboard site.
    date = input("what year you would like to travel? please tell it to me in YYYY-MM-DD format : ")

    # send a request and get it as a text.
    response = requests.get("https://www.billboard.com/charts/hot-100/" + date).text

    soup = BeautifulSoup(response, 'html.parser') #Create a beatifulsoup Object


    song_names = [i.getText().strip() for i in soup.find_all(name='h3', class_='a-no-trucate')]
    band_names = [i.getText().strip() for i in soup.find_all(name='span', class_='a-no-trucate')]

    edited_bands = []
    # edit names and remove \n and \t
    for item in band_names:

        if item.strip() in ['NEW', 'RE-\nENTRY', '-'] or item.strip().isnumeric() == True:
            pass
        
        else:
            edited_bands.append(item.strip())


    return [song_names, band_names]

