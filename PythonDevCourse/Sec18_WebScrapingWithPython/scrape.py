import requests
from bs4 import BeautifulSoup
import pprint
# beautifulsoup allows to access html and grab the data
# requests allows to download the required html

res = requests.get('https://news.ycombinator.com/')
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body)
# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.title)
# print(soup.a)
# print(soup.find('a'))
# print(soup.find(id='score_41540362'))
# print(soup.select('#score_41540362'))  # list is returned

links = soup.select('.titleline')
subtext = soup.select('.subtext')
# print(votes[0])
# # get id
# print(votes[0].get('id'))
# print(links[0].get('href'))


def create_custom_hn(links, subtext):
    hn = []
    for idx, link in enumerate(links):
        title = link.getText()
        a_tag = link.find('a')
        href = a_tag.get('href', None)
        vote = subtext[idx].select('.score')
        # print(vote[0].getText())
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            # print(points)
            if points >= 100:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sorted(hn, key=lambda k: k['votes'], reverse=True)


pprint.pprint(create_custom_hn(links, subtext))
