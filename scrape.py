import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links= soup.select('.titleline')
subtext = soup.select('.subtext')

def create_custom_hn(links, votes):
    hn =[]

    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
        hn.append({'title': title, 'href': href, 'votes': points})

    return hn

print(create_custom_hn(links, subtext))