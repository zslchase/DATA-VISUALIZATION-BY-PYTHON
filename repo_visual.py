import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict=r.json()

repo_dicts=response_dict['items']
print(repo_dicts[0])
repo_links,stars,labels=[],[],[]
for repo_dict in repo_dicts:
    repo_name=repo_dict['name']
    repo_url=repo_dict['html_url']
    repo_link=f"<a href='{repo_url}'>{repo_name}</a>"
    star=repo_dict['stargazers_count']
    repo_links.append(repo_link)
    stars.append(star)
    owner=repo_dict['owner']['login']
    description=repo_dict['description']
    label=f"{owner}<br /> {description}"
    labels.append(label)

data=[{'type': 'bar',
        'x':repo_links,
        'y':stars,
        'hovertext':labels,
        'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6,
    }]

my_layout={
    'title':'Github上最受欢迎的Python项目',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}
fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='repo.html')


