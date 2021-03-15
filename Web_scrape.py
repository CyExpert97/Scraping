#%%
import sys 
from selenium import webdriver
from time import sleep
import pandas as pd
sys.path
driver = webdriver.Chrome('./chromedriver')

driver.get('https://blitz.gg/lol/champions/overview')
#%%
sleep(1)
items = driver.find_elements_by_xpath('//*[@id="scroll-view-main"]/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div')
print(len(items))

df = pd.DataFrame()

for item in items:
    role = item.find_element_by_xpath("div/svg/title").text
    name = item.find_element_by_xpath('div/span').text
    img = item.find_element_by_xpath('div/img').get_attribute('src')
    win_rate = item.find_element_by_xpath('div/p').text
    champion_ban_rate = item.find_element_by_xpath('div[5]').text
    champion_pick_rate = item.find_element_by_xpath('div[6]').text
    print(name)
    print(img)
    print(role)
    print(win_rate)
    print(champion_ban_rate)
    
    ex = {
        # 'Role of champion': role,
        'Image of champion': img,
        'Name of champion': name,
        'Win rate of champion': win_rate,
        'Ban rate of champion': champion_ban_rate,
        'Pick rate of champion': champion_pick_rate
    }

    df = df.append(ex, ignore_index=True)
    print(df)
    break

    df.to_csv('data.csv')
    
#%%
driver.quit()
# %%
