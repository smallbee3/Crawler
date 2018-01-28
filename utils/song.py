import os

import requests
from bs4 import BeautifulSoup, NavigableString



# utils가 있는
PATH_MODULE = os.path.abspath(__file__)

# 프로젝트 컨테이너 폴더 경로
ROOT_DIR = os.path.dirname(os.path.dirname(PATH_MODULE))

# data/ 폴더 경로
DATA_DIR = os.path.join(ROOT_DIR, 'data')

# 만약에 path_data_dir에 해당하는 폴더가 없을 경우 생성해준다
os.makedirs(DATA_DIR, exist_ok=True)

# print(PATH_MODULE)
# print(ROOT_DIR)
# print(DATA_DIR)


class Song:
    def __init__(self, song_id, title, artist, album):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.album = album

        self._release_date = None
        self._genre = None
        self._lyrics = None
        self._producers = None

    def __str__(self):
        return f'{self.title} (아티스트: {self.artist}, 앨범: {self.album})'

    def get_detail(self, refresh_html=False):
        """
        자신의 _release_date, _lyrics, _genre, _producers를 채운다
        :return:
        """
        # 파일위치는 data/song_detail_{song_id}.html
        file_path = os.path.join(DATA_DIR, f'song_detail_{self.song_id}.html')
        try:
            file_mode = 'wt' if refresh_html else 'xt'
            with open(file_path, file_mode) as f:
                # url과 parameter구분해서 requests사용
                url = f'https://www.melon.com/song/detail.htm'
                params = {
                    'songId': self.song_id,
                }
                response = requests.get(url, params)
                source = response.text
                # 만약 받은 파일의 길이가 지나치게 짧을 경우 예외를 일으키고
                # 예외 블럭에서 기록한 파일을 삭제하도록 함
                file_length = f.write(source)
                if file_length < 10:
                    raise ValueError('파일이 너무 짧습니다')
        except FileExistsError:
            print(f'"{file_path}" file is already exists!')
        except ValueError:
            # 파일이 너무 짧은 경우
            os.remove(file_path)
            return

        source = open(file_path, 'rt').read()
        soup = BeautifulSoup(source, 'lxml')
        # div.song_name의 자식 strong요소의 바로 다음 형제요소의 값을 양쪽 여백을 모두 잘라낸다
        # 아래의 HTML과 같은 구조
        # <div class="song_name">
        #   <strong>곡명</strong>
        #
        #              Heart Shaker
        # </div>
        div_entry = soup.find('div', class_='entry')
        title = div_entry.find('div', class_='song_name').strong.next_sibling.strip()
        artist = div_entry.find('div', class_='artist').get_text(strip=True)
        # 앨범, 발매일, 장르...에 대한 Description list
        dl = div_entry.find('div', class_='meta').find('dl')
        # isinstance(인스턴스, 클래스(타입))
        # items = ['앨범', '앨범명', '발매일', '발매일값', '장르', '장르값']
        items = [item.get_text(strip=True) for item in dl.contents if not isinstance(item, str)]
        it = iter(items)
        description_dict = dict(zip(it, it))

        # value가 없을 수도 있으므로 get()으로 넣어준다.
        album = description_dict.get('앨범')
        release_date = description_dict.get('발매일')
        genre = description_dict.get('장르')

        # 가사 부분에서 첫번째 주석처리와 띄어쓰기 문제해결
        div_lyrics = soup.find('div', id='d_video_summary')

        lyrics_list = []
        for item in div_lyrics:
            if item.name == 'br':
                lyrics_list.append('\n')
            elif type(item) is NavigableString:
                lyrics_list.append(item.strip())
        lyrics = ''.join(lyrics_list)

        # 작사 / 작곡
        li_list = soup.select('ul.list_person > li')

        producers = {}
        ### producers[person_type] = list() 한줄로 아래 세줄 박살
        # word_list = list()
        # lyrics_list = list()
        # arrange_list = list()
        for i in li_list:
            person = i.select_one('div.ellipsis > a').text
            person_type = i.select_one('div.meta > span').text

        ### 이 한 줄 한 시간 걸림.. ###
        ### 없는 키를 호출 했을 때 None을 받는 방법을 생각하면 a.get(key) 밖에 없다.
        ### a.keys()에서 반환되는 리스트에서 person_type을 일일이 대조하는 방법도 있지만 너무 코드가 길어진다.
            if producers.get(person_type) == None:
                producers[person_type] = []
            producers[person_type].append(person)
            # print(producers, '\n')

        # 리턴하지말고 데이터들을 자신의 속성으로 할당
        self.title = title
        self.artist = artist
        self.album = album
        self._release_date = release_date
        self._genre = genre
        self._lyrics = lyrics
        self._producers = producers

        #################################################################
        #
        # # 작사/작곡은 주말 숙제 포함
        # 'producers': {
        #     '작사': ['별들의 전쟁'],
        #     '작곡': ['David Amber', 'Sean Alexander'],
        #     '편곡': ['Avenue52'],
        # },
        #
        # # 리스트로 받을 수 있고 또 키 value로 받을 수 있게 해 놨잖아요.
        # 이 키는 없어도 되잖아요. 이 키가 있을 경우에만 해당 키를 추가하고
        # 해당 키가 있으면 append를 시키고, 리스트가 없으면 새로 만들고.
        # 이런과정을 코드로 만들어야겠죠.
        #
        #################################################################

    @property
    def release_date(self):
        # 만약 가지고 있는 발매일 정보가 없다면
        if not self._lyrics:
            # 받아와서 할당
            self.get_detail()
        # 그리고 발매일 정보 출력(리턴)
        return self._lyrics

    @property
    def genre(self):
        if not self._genre:
            self.get_detail()
        return self._genre

    @property
    def lyrics(self):
        if not self._lyrics:
            self.get_detail()
        return self._lyrics

    @property
    def producers(self):
        if not self._producers:
            self.get_detail()
        return self._producers

