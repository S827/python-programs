import requests
from bs4 import BeautifulSoup as bs
import pprint

URL = 'https://www.geeksforgeeks.org/page/1/'

req = requests.get(URL)
soup = bs(req.text, 'html.parser')

# titles = soup.find_all(
#     'div', attrs={'class', 'ArticleCard_articleCardContainer__TrzCd'})
# print(len(titles))
# print(titles[0].text)
links = soup.select('.ArticleCard_articleCardContainer_title__2RhN5')
# print(links[0])


def create_custom(links):
    hn = []
    for idx, link in enumerate(links):
        title = link.getText()
        href = link.get('href', None)
        hn.append({'title': title, 'href': href})
    return hn


pprint.pprint(create_custom(links))
