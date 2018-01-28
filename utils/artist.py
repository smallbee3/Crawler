import os

import re
import requests
from bs4 import BeautifulSoup, NavigableString, Tag

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


class Artist:
    def __init__(self, artist_id, name, ngt, genre, sample_music, url_img_cover):
        self.artist_id = artist_id
        self.name = name
        self.ngt = ngt              # 내 방식
        self.genre = genre          # 내 방식
        self.sample_music = sample_music    # 내 방식
        self.url_img_cover = url_img_cover


        self._real_name = None
        self._team_member = []    # 내 방식

        self._info = {}
        self._award_history = []
        self._introduction = str()
        self._activity_information = {}
        self._personal_information = {}
        self._related_information = {}




    def __str__(self):
        return f'''
        아이디: {self.artist_id}
        이름: {self.name}
        국적,성별,타입: {self.ngt}
        장르: {self.genre}
        샘플음악: {self.sample_music}
        프로필이미지 : {self.url_img_cover}
        '''


    def get_detail(self, refresh_html=False):

        # 파일위치는 data/song_detail_{song_id}.html
        file_path = os.path.join(DATA_DIR, f'artist_detail_{self.artist_id}.html')

        try:
            file_mode = 'wt' if refresh_html else 'xt'
            with open(file_path, file_mode) as f:

                # url과 parameter구분해서 requests사용
                url = f'https://www.melon.com/artist/detail.htm'
                params = {
                    'artistId': self.artist_id,
                }
                response = requests.get(url, params)
                source = response.text

                # 만약 받은 파일의 길이가 지나치게 짧을 경우 예외를 일으키고
                # 예외 블럭에서 기록한 파일을 삭제하도록 함
                # f.write()는 작성한 문자열의 길이를 반환함.
                file_length = f.write(source)
                if file_length < 10:
                    return ValueError('파일이 너무 짧습니다')
        # except FileNotFoundError:
        #     print(f'"{file_path}" file does not exists! ')
        #     return
        except FileExistsError:
            print(f'"{file_path}" file already exists!')
        except ValueError:
            # 파일이 너무 짧은 경우
            os.remove(file_path)
            return

        source = open(file_path, 'rt').read()
        soup = BeautifulSoup(source, 'lxml')


    ### 1) name (이미 self.name으로 존재)
        self.name = soup.select_one('p.title_atist').strong.next_sibling
        # print(f'이름: {name}')

    ### 2) real_name
        if soup.select_one('p.title_atist > span.realname'):
            self._real_name = soup.select_one('p.title_atist > span.realname').get_text(strip=True)
        else:
            self._real_name = ''
        # print(f'실명: {real_name}')

    ### 3) team_memer "list"
        # team_member = list()
        if not soup.select_one('a.atistname > span:nth-of-type(1)') == None:
            a = soup.select('a.atistname > span:nth-of-type(1)')
            for i in a:
                i = i.get_text(strip=True)
                self._team_member.append(i)
        else:
            self._team_member = ''
        # print(f'멤버: {self.team_member}')

    ### 4) _info "dictionary"

        dl = soup.select_one('dl.atist_info')
        # print(dl)

        # 4-1) 데뷔일
        if re.search(r'.*데뷔', str(dl), re.DOTALL):
            debut = re.search(r'.*데뷔.*?gubun">(.*?)</span>', str(dl), re.DOTALL).group(1)
        else:
            debut = ''
        # print(f'데뷔일: {debut}')

        # 4-2) 생일
        if re.search(r'.*생일', str(dl), re.DOTALL):
            birthday = re.search(r'.*생일.*?(\d*?.\d*?.\d*?)</dd>', str(dl), re.DOTALL).group(1)
        else:
            birthday = ''
        # print(f'생일: {birthday}')

        # 4-3) 활동유형
        if re.search(r'.*활동유형', str(dl), re.DOTALL):
            artist_type = re.search(r'.*활동유형.*?<dd>(.*?)</dd>', str(dl), re.DOTALL).group(1)
        else:
            artist_type = ''
        # print(f'활동유형: {artist_type}')

        # 4-4) 소속사
        if re.search(r'.*소속사', str(dl), re.DOTALL):
            company = re.search(r'.*소속사.*?<dd>(.*?)</dd>', str(dl), re.DOTALL).group(1)
        else:
            company = ''
        # print(f'소속사: {company}')

        # 4-5) 수상이력
        if re.search(r'.*수상이력', str(dl), re.DOTALL):
            # 1. 정규표현식으로 한번 자르고
            awards_tag = re.search(r'.*수상이력.*?ellipsis">(.*?)href', str(dl), re.DOTALL).group(1)
            # 2. BeautifulSoup으로 텍스트 걸러내고
            soup = BeautifulSoup(awards_tag, 'lxml')
            awards_string = soup.get_text(strip=True)
            # 3. split 함수로 잘라서 리스트로 만들기
            awards = awards_string.split('|')
        else:
            awards = ''
        # print(f'수상이력: {awards}')


        self._info = {
            '데뷔' : debut,
            '생일' : birthday,
            '활동유형' : artist_type,
            '소속사' : company,
            '수상이력' : awards,
        }
        # print(self._list)


        ##### 위에서 텍스트 걸러낼때 한번 사용했기 때문에 다시 선언해야하는데
        ##### 그걸 놓쳐서 30분 날라감.
        soup = BeautifulSoup(source, 'lxml')

    ### 5) _award_history "list"

        if re.search(r'수상이력</h3>', source, re.DOTALL):
            dd_list = soup.select('div.wrap_insdc dl.list_define > dd')
            for dd in dd_list:
                award_string = dd.get_text(strip=True)
                award_list = award_string.split('|')
                award = f'{award_list[0]} ({award_list[1]})'

                self._award_history.append(award)

        else:
            self._award_history = ''

        # print(self._award_history)


    ### 6) _introduction "dictionary"

        if re.search(r'아티스트 소개</h3>', source, re.DOTALL):
            intro_tag = soup.select_one('div#d_artist_intro')
            # print(intro_tag)
            for i in intro_tag:
                # print(type(i))
                if type(i) is NavigableString:  ## == 비교도 가능.
                    self._introduction += i.strip()
                elif type(i) == Tag:
                    self._introduction += '\n'
        else:
            pass

        # print(self._introduction)


    ### 7) _activity_information "dictionary"

        # _activity_information =
        # print(_activity_information)

        if re.search(r'활동정보</h3>', source, re.DOTALL):
            ################################################
            ## find_next_sibling으로 겨우 해결..
            # dl_list = soup.select_one('div.debutsong').find_next_sibling('dl', class_='list_define')
            ## 아이유 악대가 find_next_sibling이 안되서 다시 보니 section_atistinfo03로 한번에 뽑을 수 있었다.
            ## 그냥 soup + .find_next_sibling 공부했다 치자...
            ################################################
            dl_list = soup.select_one('div.section_atistinfo03 > dl')
            dt = dl_list.select('dt')
            dd = dl_list.select('dd')

            dd_dt = list(zip(dt, dd))
            # print(dd_dt)

            for i, j in dd_dt:
                i = i.get_text(strip=True)
                j = j.get_text(strip=True)
                self._activity_information[i] = j

            # print(self._activity_information)
        else:
            self._activity_information = ''

    ### 8) _personal_information "dictionary"

        if re.search(r'신상정보</h3>', source, re.DOTALL):
            dl_list = re.search(r'신상정보</h3>.*?-->(.*?)</dl>', source, re.DOTALL)
            # dt = re.findall('<dt>.*?</dt>', dl_list.group(1))
            # dd = re.findall('<dd>.*?</dd>', dl_list.group(1))
            soup = BeautifulSoup(dl_list.group(), 'lxml')
            dt = soup.select('dt')
            dd = soup.select('dd')

            dd_dt = list(zip(dt, dd))
            # print(dd_dt)

            for i, j in dd_dt:
                i = i.get_text(strip=True)
                j = j.get_text(strip=True)
                self._personal_information[i] = j
            # print(self._personal_information)
        else:
            self._personal_information = ''


    ### 9) _related_information "dictionary"

        if re.search(r'연관정보</h3>', source, re.DOTALL):
            soup = BeautifulSoup(source, 'lxml')

            # 1. SNS
            sns_list = soup.select('dl.list_define_sns > dd > button')
            # print(sns_list)

            sns_dict = {}
            for i in sns_list:
                sns_title = i.get_text(strip=True)
                sns_url = re.search('open\(\'(.*?)\'', str(i)).group(1)
                sns_dict[sns_title] = sns_url

            self._related_information['SNS'] = sns_dict

            # 2. YouTube, 팬클럽
            dl_list = soup.select_one('div.section_atistinfo05 > dl.list_define')
            dt = dl_list.select('dt')
            dd = dl_list.select('dd')

            dd_dt = list(zip(dt, dd))
            # print(dd_dt)

            for i, j in dd_dt:
                i = i.get_text(strip=True)
                j = j.get_text(strip=True)
                self._related_information[i] = j
            # print(self._related_information)
        else:
            self._related_information = ''


        # 자신의 속성 채우기

        # 위에서 다 함. 별도로 변수를 만들어주는게 오히려 더 복잡해서.


        # 모두 출력
        print(f'이름: {self.name}')
        print(f'실명: {self._real_name}')
        print(f'멤버: {self._team_member}')

        print(f'기본정보: {self._info}')
        print(f'수상이력: {self._award_history}')
        print(f'아티스트소개: {self._introduction}')
        print(f'활동정보: {self._activity_information}')
        print(f'신상정보: {self._personal_information}')
        print(f'연관정보: {self._related_information}')



    def get_song(self):
        url = 'https://www.melon.com/artist/song.htm'
        params = {
            'artistId': self.artist_id,
        }
        response = requests.get(url, params)
        soup = BeautifulSoup(response.text, 'lxml')

        tr_list = soup.select('tbody > tr')

        result = []
        for tr in tr_list:

            rank = tr.select_one('td.no > div').text
            song_id = tr.select_one('td > div > input').get('value')
            title = tr.select_one('div.pd_none > div.ellipsis > a > span').text
            artist = tr.select_one('div.wrapArtistName > div.ellipsis > span').text

            ### BeautifulSoup CSS selector로 사용할 때 style 태그 검색방법
            ### tag[style*=" "]
            album = tr.select_one('div[style*="max-width:90%"] > a').text

            result.append({
                'rank': rank,
                'title': title,
                # 'url_img_cover': url_img_cover,
                'artist': artist,
                'album': album,
                'song_id': song_id,
            })

            # Song class에도 이 4개 변수가 존재해서 아래처럼 Song의 인스턴스를 생성해서 보내려고 했으나
            # get_song에서 인스턴스를 통해 접근하는게 의미가 없어보임..
            ###########################################################
            # song = Song(song_id=song_id, title=title, artist=artist, album=album)
            # result.append(song)


        return result
