import requests
from bs4 import BeautifulSoup as bs
import pprint
# URL = 'https://www.geeksforgeeks.org/page/1/'

# req = requests.get(URL)
# soup = bs(req.text, 'html.parser')


def create_custom(links):
    hn = []
    for link in links:
        title = link.getText()
        href = link.get('href', None)
        hn.append({'title': title, 'href': href})
    return hn


for i in range(1, 10):
    URL = f"https://www.geeksforgeeks.org/page/{i}/"
    req = requests.get(URL)
    soup = bs(req.text, 'html.parser')
    links = soup.select('.ArticleCard_articleCardContainer_title__2RhN5')
    # print(URL)
    print(f'*************Page {i}*******')
    pprint.pprint(create_custom(links))
