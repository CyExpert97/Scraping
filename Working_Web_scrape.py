#%%
import sys 
from selenium import webdriver
from time import sleep
import pandas as pd
# import urllib.request
import requests
sys.path

class LOLLeaderboardScraper:
    def __init__(self):
        self.driver_stats = webdriver.Chrome('./chromedriver')
        self.driver_stats.get('https://blitz.gg/lol/champions/overview')
        self.champions = []

    def get_stats(self):    
        sleep(10)
        # Scrappin from blitz.gg website to get champion info
        items = self.driver_stats.find_elements_by_xpath("//div[contains(@class,'champion-row')]")
        # Creating pandas dataframe to save code later
        
        # From bliz.gg search the table specifically for the info we want and save it to a dictionary
        for item in items:
            role = item.find_element_by_xpath("div[2]/*[local-name()='svg']/*[local-name()='title']").get_attribute('innerHTML')
            name = item.find_element_by_xpath('div/span').text
            img = item.find_element_by_xpath('div/img').get_attribute('src')
            win_rate = item.find_element_by_xpath('div/p').text
            champion_ban_rate = item.find_element_by_xpath('div[5]').text
            champion_pick_rate = item.find_element_by_xpath('div[6]').text
            # Below is used to save images locally
            img_data = requests.get(img).content
            with open(f'image_{name}.jpg', 'wb') as handler:
                handler.write(img_data)

            ex = {
                    'Role of champion': role,
                    'Image of champion': img,
                    'Name of champion': name,
                    'Win rate of champion': win_rate,
                    'Ban rate of champion': champion_ban_rate,
                    'Pick rate of champion': champion_pick_rate
            }
            self.champions.append(ex)
        self.driver_stats.quit()
          

    def get_champion_wiki(self, name):
            # Open new driver to LOL wiki page to get individual champion stats
            driver_wiki = webdriver.Chrome('./chromedriver')
            driver_wiki.get('https://leagueoflegends.fandom.com/wiki/{}/LoL'.format(name))
            #Appends to dictionaries with the same champion name
            champs = list(filter(lambda x: x['Name of champion']==name, self.champions))
            while True:
                try:
                    driver_wiki.find_element_by_class_name('NN0_TB_DIsNmMHgJWgT7U.XHcr6qf5Sub2F2zBJ53S_').click()
                    break
                except:
                    sleep(0.1)
            # Class name for every row of the table (has 4 columns)
            items_2 = driver_wiki.find_elements_by_class_name('pi-smart-group-body')                                             
            print(len(items_2))
            # Only giterating through relevant information to increase efficiency 
            for item in items_2[:7]:
                # Splits items by line (is equal to columns)
                it = item.text.split("\n")
                # Only wanting columns of length > 4 since that has info we want
                if len(it) > 3:
                    # Columns 0 and 2 are category names and 1 and 3 are values
                    for champ in champs:
                        champ[it[0]] = it[1]
                        champ[it[2]] = it[3]
            
            driver_wiki.quit()    
            
            

    def scrape(self):
        self.get_stats()
        for champ in self.champions:
            self.get_champion_wiki(champ['Name of champion'])
        df = pd.DataFrame(self.champions)
        df.to_csv('data_test_2.csv') 

lol_scraper = LOLLeaderboardScraper()
lol_scraper.scrape()

# %%
