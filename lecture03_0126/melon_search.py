import requests

from bs4 import BeautifulSoup
import re

def rch_song(title):


    url = f'https://www.melon.com/search/song/index.htm?q={title}&section=song'
    response = requests.get(url)
    source = response.text

    num = 1
    soup = BeautifulSoup(source, 'lxml')
    for tr in soup.find_all('tr'):
        if num == 1:
            print(num)
            num += 1
            continue
        # title = tr.find('div', class_='ellipsis').find('a')
        # title = tr.select_one('div a:nth-of-type(2)').get('title')
        # print(title)
        print(num)
        num += 1

        artist = tr.find('div', class_='ellipsis')
        print(artist)


    return
