from urllib.request import urlopen, Request 
from bs4 import BeautifulSoup as bs

url = "https://leagueoflegends.fandom.com/wiki/Akali/LoL"
r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})    
html_page  = urlopen(r)
soup = bs(html_page, "html.parser")
attributes = soup.findAll("li")
print(attributes)
