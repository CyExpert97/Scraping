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

        driver_ranks = webdriver.Chrome('./chromedriver')
        
        driver_ranks.get('https://euw.op.gg/ranking/ladder/')
        #%%
        sleep(10)
        df = pd.DataFrame()

        rank_1 = driver_ranks.find_element_by_xpath('/html/body/div[3]/div[3]/div[3]/div/div/div/div[1]/ul/li[1]/a').get_attribute('href')
        ex = {'Url 0f player': rank_1}
        df = df.append(ex, ignore_index=True)
        rank_2 = driver_ranks.find_element_by_xpath('/html/body/div[3]/div[3]/div[3]/div/div/div/div[1]/ul/li[2]/a').get_attribute('href')
        ex = {'Url 0f player': rank_2}
        df = df.append(ex, ignore_index=True)
        rank_3 = driver_ranks.find_element_by_xpath('/html/body/div[3]/div[3]/div[3]/div/div/div/div[1]/ul/li[3]/a').get_attribute('href')
        ex = {'Url 0f player': rank_3}
        df = df.append(ex, ignore_index=True)
        rank_4 = driver_ranks.find_element_by_xpath('/html/body/div[3]/div[3]/div[3]/div/div/div/div[1]/ul/li[4]/a').get_attribute('href')
        ex = {'Url 0f player': rank_4}
        df = df.append(ex, ignore_index=True)

        items = driver_ranks.find_elements_by_xpath("/html/body/div[3]/div[3]/div[3]/div/div/div/table/tbody/tr/td[2]/a")
        for item in items:
        
           ex = {'Url 0f player': item.get_attribute('href')}
           df = df.append(ex, ignore_index=True)

        df.to_csv('top_100.csv')
        
        driver_ranks.quit()
#%%
lol_scraper = LOLScraper()
lol_scraper.get_stats()

#%%