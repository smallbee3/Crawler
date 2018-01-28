import os

import re
import requests
from bs4 import BeautifulSoup

from utils.artist import Artist
from utils.song import Song



class MelonCrawler:
    def search_song(self, q):
        """
        곡 명으로 멜론에서 검색한 결과 리스트를 리턴
        :param q: 검색할 곡 명
        :return: 결과 dict리스트
        """
        """
        1. http://www.melon.com/search/song/index.htm
            에 q={q}, section=song으로 parameter를 준 URL에
            requests를 사용해 요청
        2. response.text를 사용해 BeautifulSoup인스턴스 soup생성
        3. soup에서 적절히 결과를 가공
        4. 결과 1개당 Song인스턴스 한개씩
        5. 전부 리스트에 넣어 반환
        6. 완☆성
        """
        url = 'https://www.melon.com/search/song/index.htm'
        params = {
            'q': q,
            'section': 'song',
        }
        response = requests.get(url, params)
        soup = BeautifulSoup(response.text, 'lxml')

        # select는 모든 값을 찾아 리스트로 반환, find_all과 비슷한 역할
        tr_list = soup.select('form#frm_defaultList table > tbody > tr')
        # tr = soup.find('form', id='frm_defaultList').find('table').find('tbody').find_all('tr')

        result = []
        for tr in tr_list:
            # <a href="javascript:searchLog('web_song','SONG','SO','빨간맛','30512671');melon.play.playSong('26020103',30512671);" class="fc_gray" title="빨간 맛 (Red Flavor)">빨간 맛 (Red Flavor)</a>
            # song_id = re.search(r"searchLog\(.*'(\d+)'\)", tr.select_one('td:nth-of-type(3) a.fc_gray').get('href')).group(1)
            song_id = tr.select_one('td:nth-of-type(1) input[type=checkbox]').get('value')
            title = tr.select_one('td:nth-of-type(3) a.fc_gray').get_text(strip=True)
            artist = tr.select_one('td:nth-of-type(4) span.checkEllipsisSongdefaultList').get_text(
                strip=True)
            album = tr.select_one('td:nth-of-type(5) a').get_text(strip=True)

            song = Song(song_id=song_id, title=title, artist=artist, album=album)
            result.append(song)
        return result

    def search_artist(self, q, refresh_html=False):
        url = 'https://www.melon.com/search/artist/index.htm'
        params = {
            'q': q,
        }

        response = requests.get(url, params)
        soup = BeautifulSoup(response.text, 'lxml')
        li_list = soup.select('div.section_atist div#pageList > div > ul > li')
        result = []
        for li in li_list:
            # 1) artist_id 추출
            artist_id = li.select_one('dd:nth-of-type(4) input').get('value')

            # 2) name 추출
            artist_title = li.select_one('dt > a').get('title')
            name = re.search(r'(.*?)\s-', artist_title).group(1)
            # print(name)

            # 3) nationality,gender,artis_type 동시추출
            ngt = li.select_one('dd.gubun').get_text(strip=True)
            # print(ngt)


            ### 레드벨벳 구하기 돌입###
            # 레드벨벳에서 9번째 검색결과에서 '대한민국/솔로'가 나오는 문제를 해결못함.
            # nationality = re.search(r'(.*?)/', ngt_group).group(1)
            # gender = re.search(r'/(.*?)/', ngt_group).group(1)
            # # artist_type = ngt_group[-2:]  # 이 방법은 문제점 : '사랑'검색에서 성별 안나옴.
            # artist_type = re.search(r'.*?/.*?/(.*?)$', ngt_group).group(1)

            # info_list = info_group.split('/')
            # print(info_list)

            ### 딕셔너리로 저장하기로 결정. 가수 상세페이지에도 정보가 너무 많음.
            ### 딕셔너리 포기. because 아래서 각각의 변수로 인스턴스를 생성해야하는데 딕셔너리로 하면
            ### 너무 달라진다.

            # if len(info_list) > 0:
            #     nationality = info_list[0]
            # elif len(info_list) > 1:
            #     gender = info_list[1]
            # elif len(info_list) > 2:
            #     artist_type = info_list[2]

            # num = len(info_list)
            # if num >= 1:
            #     nationality = info_list[0]
            # if num >= 2:
            #     gender = info_list[1]
            # if num == 3:
            #     artist_type = info_list[2]
            # else:
            #     # 레드벨벳 '하희수' 검색결과 항목의 경우 이전 결과의 artist_type의 값을 가져옴.
            #     artist_type = ''


            # 4) genre 추출
            genre = li.select_one('dd.gnr > div').get_text(strip=True)
            # print(genre)

            # 5) sample_music 추출
            sample_music = li.select_one('dd.btn_play > a > span:nth-of-type(2)')
            if not sample_music == None:
                sample_music = sample_music.get_text(strip=True)
            else:
                # None 을 ''로 바꿔서 type을 통일하고 이후에 발생할 문제소지를 차단
                sample_music = None
            # print(sample_music)

            # 6) url_img_cover 원본 추출
            url_img = li.select_one('div.wrap_atist12 > a > img').get('src')

            # 기본 프로필에서 이미지 주소가 html문서와 상이한 문제해결
            if url_img == 'http://cdnimg.melon.co.kr':
                url_img_cover = 'http://cdnimg.melon.co.kr/resource/image/web/default/noArtist_300_160727.jpg'
            else:
                url_img_cover = re.search(r'(.*.jpg)', url_img).group(1)
            # print(url_img_cover)


            artist = Artist(
                artist_id=artist_id,
                name=name,
                ngt = ngt,
                genre=genre,
                sample_music=sample_music,
                url_img_cover=url_img_cover,
            )
            result.append(artist)

            # Artist의 인스턴스를 return
            # -> Artist의 인스턴스를 위의 과정 없이 생성해서 바로 쓸 수있다.
            #
            # ex) artist_list = search_artist('아이유')
            #     artist_list는 '아이유' 검색결과의 각각의 "인스턴스"를 담은 리스트
            #
            #     첫번째 검색결과를 쓰려면 artist_list의 첫번째 인자를 받아야 한다.
            #     artist = artist_list[0]
            #
            #     artist도 첫번째 검색결과의 Artist class "인스턴스"이므로
            #     이제 Artist class에 접근할 수 있다.
            #     artist.artist_id



######## search_song과 같은 방식으로 인스턴스를 생성해서 return하려 했으나 ########
######## Artist Class의 __init__ 안의 속성들과 '아티스트채널 상세정보'를 ########
######## 맞추는게 우선이라 이곳에서는 원래 과제 가이드처럼 목록만 return 하 ##########
######## 려 했으나 너무 귀찮아서 다시 내 방법대로 함.  ###########################

            # result.append({
            #     'artist_id': artist_id,
            #     'name': name,
            #     'nationality': nationality,
            #     'gender': gender,
            #     'artist_type': artist_type,
            #     'genre': genre,
            #     'sample_musice': sample_music,
            # })

        return result

