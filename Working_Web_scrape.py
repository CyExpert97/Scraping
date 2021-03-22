#%%
import sys 
from selenium import webdriver
from time import sleep
import pandas as pd
sys.path

class LOLScraper:
    def __init__(self):
        pass

    def get_stats(self):
        pass
        driver_stats = webdriver.Chrome('./chromedriver')

        driver_stats.get('https://blitz.gg/lol/champions/overview')
        #%%
        sleep(10)
        items = driver_stats.find_elements_by_xpath("//div[contains(@class,'champion-row')]")
        print(len(items))
        #%%
        df = pd.DataFrame()
        for item in items:
            role = item.find_element_by_xpath("div[2]/*[local-name()='svg']/*[local-name()='title']").get_attribute('innerHTML')
            name = item.find_element_by_xpath('div/span').text
            img = item.find_element_by_xpath('div/img').get_attribute('src')
            win_rate = item.find_element_by_xpath('div/p').text
            champion_ban_rate = item.find_element_by_xpath('div[5]').text
            champion_pick_rate = item.find_element_by_xpath('div[6]').text
            ex = {
                    'Role of champion': role,
                    'Image of champion': img,
                    'Name of champion': name,
                    'Win rate of champion': win_rate,
                    'Ban rate of champion': champion_ban_rate,
                    'Pick rate of champion': champion_pick_rate,
                    # "Health":"",
                    # "Health regen.":"",
                    # "Armor":"",
                    # "Attack damage":"",
                    # "Magic resist.":"",
                    # "Crit. damage":"",
                    # "Move. speed":"",
                    # "Attack range":"",
                    # "Base AS":"",
                    # "Bonus AS":"",
                    # "Mana":"",
                    # "Mana regen.":"",
                    # "MagicTrue":"",
                    # "Energy":"",
                    # "Energy regen.":"",
                    # "Missile speed":"",
                    # "Magic damage":"",
                    # "Attack speed":"",
                    # "Range":"",
                    # "Magic res.":"",
                    # "Mov. speed":"",
            }
            print(name)

            driver_wiki = webdriver.Chrome('./chromedriver')
            driver_wiki.get('https://leagueoflegends.fandom.com/wiki/{}/LoL'.format(name))
            while True:
                try:
                    driver_wiki.find_element_by_class_name('NN0_TB_DIsNmMHgJWgT7U.XHcr6qf5Sub2F2zBJ53S_').click()
                    break
                except:
                    sleep(0.1)
            #Class name for every row of the table (has 4 columns)
            items_2 = driver_wiki.find_elements_by_class_name('pi-smart-group-body')                                             
            print(len(items_2))
            #Only giterating through relevant information to increase efficiency 
            for item in items_2[:7]:
                #Splits items by line (is equal to columns)
                it = item.text.split("\n")
                #Only wanting columns of length > 4 since that has info we want
                if len(it) > 3:
                    #Columns 0 and 2 are category names and 1 and 3 are values
                    ex[it[0]] = it[1]
                    ex[it[2]] = it[3]
            df = df.append(ex, ignore_index=True)
            driver_wiki.quit()    
            print(ex)
        driver_stats.quit()
        df.to_csv('data_test_2.csv')    

# %%
lol_scraper = LOLScraper()
lol_scraper.get_stats()
#%%