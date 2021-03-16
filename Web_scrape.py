#%%
import sys 
from selenium import webdriver
from time import sleep
import pandas as pd
sys.path
driver = webdriver.Chrome('./chromedriver')

driver.get('https://blitz.gg/lol/champions/overview')
#%%
sleep(5)
items = driver.find_elements_by_xpath("//div[contains(@class,'champion-row')]")
# items = driver.find_elements_by_xpath('//*[@id="scroll-view-main"]/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div')
# //*[@id="scroll-view-main"]/div/div/div/div[1]/div/div[2]/div[2]/div/div/div[1]
print(len(items))
#%%
df = pd.DataFrame()
# <div class="champion-role"><svg viewBox="0 0 32 32" class="createSvgIcon__Svg-sc-1l8xi8d-0 loXvaP"><title>role-mid</title><path d="M5.333 26.667v-4.364l16.97-16.97h4.364v4.364l-16.97 16.97h-4.364z"></path><path fill-opacity="0.4" d="M19.394 5.333l-3.879 3.879h-6.303v6.303l-3.879 3.879v-14.061h14.061zM12.606 26.667l3.879-3.879h6.303v-6.303l3.879-3.879v14.061h-14.061z"></path></svg></div>
for item in items:
    # role = item.find_element_by_xpath('//div[@class="champion-role"]/*/title').text
    # //*[@id="scroll-view-main"]/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]
    role = item.find_element_by_xpath("div[2]/*[local-name()='svg']/*[local-name()='title']").get_attribute('innerHTML')
    name = item.find_element_by_xpath('div/span').text
    img = item.find_element_by_xpath('div/img').get_attribute('src')
    win_rate = item.find_element_by_xpath('div/p').text
    champion_ban_rate = item.find_element_by_xpath('div[5]').text
    champion_pick_rate = item.find_element_by_xpath('div[6]').text
    # print(name)
    # print(img)
    print(role)
    # print(win_rate)
    # print(champion_ban_rate)
    
    ex = {
        'Role of champion': role,
        'Image of champion': img,
        'Name of champion': name,
        'Win rate of champion': win_rate,
        'Ban rate of champion': champion_ban_rate,
        'Pick rate of champion': champion_pick_rate
    }

    df = df.append(ex, ignore_index=True)
    # print(df)
    # break

    # df.to_csv('data.csv')
    
#%%
driver.quit()
# %%
