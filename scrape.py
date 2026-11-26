import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links= soup.select('.titleline')
urls = soup.select('.titleline a')
subtext = soup.select('.subtext')



def sort_stories_by_votes(hnList):
    return sorted(hnList, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, votes):
    hn =[]

    for link, text in zip(links, subtext):
        title = link.getText()
        url = link.a.get('href', None)
        vote = text.select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'href': url, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))