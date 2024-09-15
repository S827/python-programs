import requests
from bs4 import BeautifulSoup as bs
import pprint


def custom_scrap(links, subtext):
    hn = []
    for idx, link in enumerate(links):
        title = link.getText()
        a_tag = link.find('a')
        href = a_tag.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                hn.append({'title': title, 'href': href, 'votes': points})
    return sorted(hn, key=lambda k: k['votes'], reverse=True)


for i in range(1, 3):
    URL = f"https://news.ycombinator.com/news?p={i}"
    req = requests.get(URL)
    soup = bs(req.text, 'html.parser')
    links = soup.select('.titleline')
    subtext = soup.select('.subtext')
    pprint.pprint(custom_scrap(links, subtext))
