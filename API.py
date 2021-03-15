import requests
url = 'https://api.stackexchange.com/2.2/posts?sort=creation&order=desc$site=stackoverflow'
r = requests.get(url)
