import requests 
 # Make an API call and store the response
 
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' # url of the API call
headers = {'Accept': 'application/vnd.github.v3+json'} # the version of the API
r = requests.get(url, headers=headers) # request to make the call to API
print(f"Status code: {r.status_code}") # print status_code, to make sure the call went through

# Store API response in a variable.
response_dict = r.json()

# Process results.
print(response_dict.keys())