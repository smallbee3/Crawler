from utils import get_top100_list
from utils.melon_crawler import MelonCrawler



if __name__ == '__main__':
    crawler = MelonCrawler()
    # q = input('검색할 곡 명을 입력해주세요: ')
    # search_song_list = crawler.search_song(q)



################ top100 list ################

    # result = get_top100_list()
    # for i in result:
    #     print(i)



################ song 검색 ################

    # song_list = crawler.search_song('기대해')
    # song = song_list[0]

    # print(song)
    # print(song.title)
    # print(song.album)

    # print(song._lyrics, ': song._lyrics는 None' )
    # # print(song.lyrics)
    #
    # print(song._producers, ': song._producers는 None' )
    # print(song.producers)



################ artist 검색 ################

    # 시도 1
    # # search_artist() # -> Artist를 호출하는 부분이 존재.
    # search_artist를 호출할 경우에 그 안에 다른 부분의 인스턴스를
    # 생성하는 부분 'artist = Artist(~)' 이 있을경우 Artist undefined 에러가 발생

    # 시도 2
    # Artist.get_detail()           # 인자를 전달해 줘야하는데 방법이 없다.

    # 시도 3
    # artist_list = Artist('아이유')   # Artist는 인자를 엄청많이 받음, '아이유'만 받는것 검색임.
    # Artist.get_detail(artist_list) # 그리고 이짓안하려고 위에서 Artist인자를 return하는 것

    # 시도 4 (성공)
    artist_list = crawler.search_artist('아이유')
    # artist_list = crawler.search_artist('아이유악대')
    # artist_list = crawler.search_artist('걸스데이')
    # artist_list = crawler.search_artist('레드벨벳')


#### 1) 아티스트 검색 ####

    for i in artist_list:
        print(i)




#### 2) 아티스트의 곡 ####

    # artist = artist_list[0]
    # result = artist.get_song()
    # for i in result:
    #     print(i)



#### 3) 아티스트 상세정보 ####

    # artist = artist_list[0]
    # artist.get_detail()





#### 과제 가이드처럼 그냥 리스트목록을 받는 것으로 했다가
#### 너무 귀찮아서 그냥 내 방식대로 함.
#### 1) 아티스트 검색 ####
# for i in artist_list:
#     print(i)
# 딕셔너리 형태로 너무 보기 싫어서 아래로 바꿈

# for i in artist_list:
#     for j in i.keys():
#         print(f'{j}: {i.get(j)}')
#     print('')
