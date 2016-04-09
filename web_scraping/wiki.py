from urllib.request import urlopen
from bs4 import BeautifulSoup

import re
import random
import datetime


def get_links(article_url):
    result = []
    html = urlopen('http://en.wikipedia.org/' + article_url)
    bsObj = BeautifulSoup(html, 'html.parser')
    return bsObj.find('div', {'id': 'bodyContent'}).findAll('a',
                      href=re.compile('^(/wiki/)((?!:).)*$'))

if __name__ == "__main__":
    user_input = input('Enter an article url, say "/wiki/Kevin_Bacon)": ')
    user_input = '/wiki/Kevin_Bacon'
    links = get_links(user_input)
    while len(links) > 0:
        new_article = links[random.randint(0, len(links) - 1)].attrs['href']
        print(new_article)
        links = get_links(new_article)
