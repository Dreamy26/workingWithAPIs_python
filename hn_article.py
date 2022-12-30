import requests 
import json

# API call, response stored
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# structure of the data
response_dict = r.json()
readable_file ='data/readable_hn_data.json'
with open(readable_file, 'w') as file:
    json.dump(response_dict, file, indent=4)
    