import os
import requests
from bs4 import BeautifulSoup


def get_song_detail(song_id, refresh_html=False):

    """
    song_id에 해당하는 곡 정보 dict를 반환
    위의 get_top100_list의 각 곡 정보에도 song_id가 들어가도록 추가
    http://www.melon.com/song/detail.htm?songId=30755375
    위 링크를 참조
    파일명
        song_detail_{song_id}.html
    :param song_id: 곡 정보 dict
    :return:
    """

    # utils가 있는
    path_module = os.path.abspath(__name__)
    # print(f'path_module: \n{path_module}')

    # 프로젝트 컨테이너 폴더 경로
    root_dir = os.path.dirname(path_module)
    # print(f'root_dir: \n{root_dir}')

    # data/ 폴더 경로
    path_data_dir = os.path.join(root_dir, 'song_detail')
    # print(f'path_data_dir: \n{path_data_dir}')

    # 만약에 path_data_dir에 해당하는 폴더가 없을 경우 생성해준다
    os.makedirs(path_data_dir, exist_ok=True)

    # 실시간 1~100위 웹페이지 주소
    url_song_detail = 'https://www.melon.com/song/detail.htm?songId=' + song_id
    # print(f'url_song_detail: \n{url_song_detail}')

    # file_path = os.path.join(path_data_dir, f'song_detail_{song_id}.html') # 이것도 됨.
    file_path = os.path.join(path_data_dir, 'song_detail_{}.html'.format(song_id))


    try:
        # refresh_html매개변수가 True일 경우, wt모드로 파일을 열어 새로 파일을 다운받도록 함
        file_mode = 'wt' if refresh_html else 'xt'
        with open(file_path, file_mode, encoding='utf8') as f:
            response = requests.get(url_song_detail)
            f.write(response.text)
    # xt모드에서 있는 파일을 열려고 한 경우 발생하는 예외
    except FileExistsError:
        pass
        # print(f'"{file_path}" file is already exists!')

    source = open(file_path, 'rt').read()

    soup = BeautifulSoup(source, 'lxml')

    div = soup.find('div', class_='entry')

    title = soup.find('meta', property='og:title').get('content')
    artist = div.find('div', class_='artist').find('a').get('title')
    album = div.find('dd').find('a').text

    # https://stackoverflow.com/questions/38233838 'selecting second child in beautiful soup'
    date = div.select_one('dl dd:nth-of-type(2)').text
    genre = div.select_one('dl dd:nth-of-type(3)').text
    flac = div.select_one('dl dd:nth-of-type(4)').text

    # print('-'*5)
    # print(title)
    # print(artist)
    # print(album)
    # print(date)
    # print(genre)
    # print(flac)
    # print('-'*5)

    song_id_dict = dict()

    song_id_dict["{song_id}"] = {
        '제목' : title,
        '가수' : artist,
        '앨범' : album,
        '발매일' : date,
        '장르': genre,
        'FLAC': flac,
    }

    return song_id_dict['{song_id}']