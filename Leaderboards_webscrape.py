import sys 
from selenium import webdriver
from time import sleep
import pandas as pd
sys.path

class LOLChampionStatsScraper:
    def __init__(self):
        pass

    def get_stats(self):

        driver_ranks = webdriver.Chrome('./chromedriver')
        
        driver_ranks.get('https://euw.op.gg/ranking/ladder/')
        #Scraping from op.gg to get url for pro player webpages
        sleep(10)
        df = pd.DataFrame()
        # Since top 5 players are not in the table we need to get there elements individualy
        rank_1 = driver_ranks.find_element_by_xpath('/html/body/div[3]/div[3]/div[3]/div/div/div/div[1]/ul/li[1]/a').get_attribute('href')
        ex = {'Url of player': rank_1}
        df = df.append(ex, ignore_index=True)
        rank_2 = driver_ranks.find_element_by_xpath('/html/body/div[3]/div[3]/div[3]/div/div/div/div[1]/ul/li[2]/a').get_attribute('href')
        ex = {'Url of player': rank_2}
        df = df.append(ex, ignore_index=True)
        rank_3 = driver_ranks.find_element_by_xpath('/html/body/div[3]/div[3]/div[3]/div/div/div/div[1]/ul/li[3]/a').get_attribute('href')
        ex = {'Url of player': rank_3}
        df = df.append(ex, ignore_index=True)
        rank_4 = driver_ranks.find_element_by_xpath('/html/body/div[3]/div[3]/div[3]/div/div/div/div[1]/ul/li[4]/a').get_attribute('href')
        ex = {'Url of player': rank_4}
        df = df.append(ex, ignore_index=True)
        rank_5 = driver_ranks.find_element_by_xpath('/html/body/div[3]/div[3]/div[3]/div/div/div/div[1]/ul/li[5]/a').get_attribute('href')
        ex = {'Url of player': rank_5}
        df = df.append(ex, ignore_index=True)
        # Main loop of getting rest of top 95 players from table
        items = driver_ranks.find_elements_by_xpath("/html/body/div[3]/div[3]/div[3]/div/div/div/table/tbody/tr/td[2]/a")
        for item in items:
        
           ex = {'Url of player': item.get_attribute('href')}
           df = df.append(ex, ignore_index=True)

        df.to_csv('top_100.csv')
        
        driver_ranks.quit()

lol_scraper = LOLChampionStatsScraper()
lol_scraper.get_stats()

