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
        # chrome_options = Options()
        # chrome_options.add_argument("C:\Users\j_theocharides\AppData\Local\Google\Chrome\User Data")
        # driver_1 = webdriver.Chrome(chrome_options= chrome_options,executable_path='./chromedriver')
        driver_ranks = webdriver.Chrome('./chromedriver')

        driver_ranks.get('https://euw.op.gg/ranking/ladder/')
        #%%
        sleep(10)

        items = driver_ranks.find_elements_by_xpath("/html/body/div[3]/div[3]/div[3]/div/div/div/table/tbody/tr/td[2]/a/span")
        # /html/body/div[2]/div[3]/div[3]/div/div/div/table/tbody/tr[95]/td[2]/a
        # /html/body/div[2]/div[3]/div[3]/div/div/div/table/tbody/tr[1]/td[2]/a
        # /html/body/div[2]/div[3]/div[3]/div/div/div/table/tbody/tr[2]/td[2]/a
        # //*[@id="summoner-37802452"]/td[2]/a
        # //*[@id="summoner-27341898"]/td[2]/a
        print(len(items))
        

#%%
lol_scraper = LOLScraper()
lol_scraper.get_stats()

#%%