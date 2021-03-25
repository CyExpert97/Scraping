from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
import tqdm
from tqdm import tqdm
champions = open(r"C:\Users\j_theocharides\PycharmProjects\Scraping\champions.txt", encoding='utf-8').read().splitlines()
C_name = []
C_title = []
C_values = []
for c in tqdm(champions):
    c = c.replace(" ","_").replace("'","%27")
    url = "https://leagueoflegends.fandom.com/wiki/"+str(c)+"/LoL"
    r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html_page = urlopen(r)
    soup = bs(html_page, "html.parser")
    sections = soup.findAll('section')
    Char_title = []
    Char_values = []
    Char_name = []
    for s in sections:
        attribs = s.findAll('div')

        for i,a in enumerate(attribs):
            titles = a.findAll('a')
            spans = a.findAll('span')

            texts = [x.text for x in spans]
            title = [x.text for x in titles]

            if len(title)>0:
                tle = str(''.join(title))
                if len(texts)>0:
                    values = str(''.join(texts))
                else:
                    values = str(a.text).replace(tle,"")
                if "+" in values:
                    values =''.join([x for x in values if x.isdigit()== True or x =="+"])
                    vs = values.split("+")
                    base = vs[0]
                    if base != "":
                        range = (float(vs[1])*17) + float(base)
                        values = str(base) + " - " + str(range)
                    else:
                        values = values

                if "N/A" in values or tle in values or "Champion" in tle or values ==" " or len(values)==0:
                    continue
                elif tle not in Char_title and values not in Char_values:
                    Char_title.append(tle)
                    Char_values.append(values)
                    Char_name.append(c)
    C_title.extend(Char_title)
    C_values.extend(Char_values)
    C_name.extend(Char_name)

import pandas as pd
DF = pd.DataFrame(list(zip(C_name, C_title, C_values)), columns = ["Character", "Attribute", "Values"])
# savefile = "D:\\Users\\Caleb\\Documents\\forjonny.csv"
DF.to_csv(savefile, encoding='utf-8')
