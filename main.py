
import re
from bs4 import BeautifulSoup
from utils import get_top100_list

# source = open('melon.html', 'rt').read()
# soup = BeautifulSoup(source, 'lxml')

# result = []
# for tr in soup.find_all('tr', class_='lst50'):
#     rank = tr.find('span', class_='rank').text
#     title = tr.find('div', class_='rank01').find('a').text
#     artist = tr.find('div', class_='rank02').find('a').text
#     album = tr.find('div', class_='rank03').find('a').text
#     url_img_cover = tr.find('a', class_='image_typeAll').find('img').get('src')
#     # http://cdnimg.melon.co.kr/cm/album/images/101/28/855/10128855_500.jpg/melon/resize/120/quality/80/optimize
#     # .* -> 임의 문자의 최대 반복
#     # \. -> '.' 문자
#     # .*?/ -> '/'이 나오기 전까지의 최소 반복
#     p = re.compile(r'(.*\..*?)/')
#     url_img_cover = re.search(p, url_img_cover).group(1)
#
#     result.append({
#         'rank': rank,
#         'title': title,
#         'url_img_cover': url_img_cover,
#         'artist': artist,
#         'album': album,
#     })


if __name__ == '__main__':
    result = get_top100_list()
    for item in result:
        print(item)