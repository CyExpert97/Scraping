import requests
url = 'https://api.stackexchange.com/2.2/posts?sort=creation&order=desc&pagesize=100&site=stackoverflow'
r = requests.get(url)
print(len(r.json()['items']))
# print(len(r.json()))