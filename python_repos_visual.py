import requests 

from plotly.graph_objs import Bar
from plotly import offline

# url of the API call
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# the version of the API 
headers = {'Accept': 'application/vnd.github.v3+json'} 
r = requests.get(url, headers=headers) # request to make the call to API
print(f"Status code: {r.status_code}") # print status_code, to make sure the call went through

# Variable that stores API response
response_dict = r.json()

# Prints total number of python repositories on GitHub
print(f"Total repositories: {response_dict['total_count']}")

# Receive information about the repositories & store a list of dictionaries
repo_dicts = response_dict['items']
#print(f'Repositories returned: {len(repo_dicts)}')
repo_names, stars = [],[] # two empty arrays, for the initial chart data
for repo_dict in repo_dicts: # Loop, to iterate through all the dictionaries
    repo_names.append(repo_dict['name']) # append name of project, & number of stars
    stars.append(repo_dict['stargazers_count'])
    
    # Visualization Code starts here & define the data list
data =[{
    'type': 'bar',
    'x': repo_names, # x = name of the projects
    'y': stars, # y = stars received 
}]
my_layout = {
    'title': 'Most-Starred Python Projects on GitHub', # Title of Bar graph visual
    'xaxis': {'title': 'Repository'}, # bar label
    'yaxis': {'title': 'Stars'}, # height of bars
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
    
