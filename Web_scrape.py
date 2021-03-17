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

        driver_1 = webdriver.Chrome('./chromedriver')


        driver_1.get('https://blitz.gg/lol/champions/overview')
        #%%
        sleep(10)
        items = driver_1.find_elements_by_xpath("//div[contains(@class,'champion-row')]")
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
            print(name)

            driver_2 = webdriver.Chrome('./chromedriver')
            driver_2.get('https://leagueoflegends.fandom.com/wiki/{}/LoL'.format(name))
            sleep(10)
            items_2 = driver_2.find_elements_by_xpath("//*[@id='mw-content-text']/div/div[8]/aside")
            for item_2 in items_2:
                Health = item_2.find_element_by_xpath('section/section/section/div/span[2]').text
                print(Health)
                Mana = item_2.find_element_by_xpath('section/section/section/div[2]/span[2]').text
                print(Mana)
                Health_regen = item_2.find_element_by_id('HealthRegen_{}_lvl'.format(name)).text
                print(Health_regen)
                Armor = item_2.find_element_by_id('Armor_{}_lvl'.format(name)).text
                print(Armor)
                Magic_resist = item_2.find_element_by_id('MagicResist_{}_lvl'.format(name)).text
                print(Magic_resist)
                Move_speed = item_2.find_element_by_id('MoveSpeed_{}_lvl'.format(name)).text
                print(Move_speed)
                Mana_regen = item_2.find_element_by_id('ManaRegen_{}_lvl'.format(name)).text
                print(Mana_regen)
                Attack_damage = item_2.find_element_by_id('AttackDamage_{}_lvl'.format(name)).text
                print(Attack_damage)
                Crit_damage = item_2.find_element_by_id('CritDamage_{}_lvl'.format(name)).text
                print(Crit_damage)
                Attack_range = item_2.find_element_by_id('AttackRange_{}_lvl'.format(name)).text
                print(Attack_range)
                Base_AS = item_2.find_element_by_id('BaseAS_{}_lvl'.format(name)).text
                print(Base_AS)
                Bonus_AS = item_2.find_element_by_id('BonusAS_{}_lvl'.format(name)).text
                print(Bonus_AS)
                
            
                ex = {
                    'Role of champion': role,
                    'Image of champion': img,
                    'Name of champion': name,
                    'Win rate of champion': win_rate,
                    'Ban rate of champion': champion_ban_rate,
                    'Pick rate of champion': champion_pick_rate,
                    'Champion Health': Health
                }
                
                df = df.append(ex, ignore_index=True)
                # print(df)
                break
            driver_2.quit()
            break
            df.to_csv('data.csv')
            #To get lol wiki champion stats. Get the champion name and paste it into the url e.g "https://leagueoflegends.fandom.com/wiki/{Kassadin}/LoL"
#%%
        driver_1.quit()
# %%
lol_scraper = LOLScraper()
lol_scraper.get_stats()