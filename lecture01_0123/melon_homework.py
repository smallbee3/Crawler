import requests, re

source = open('melon.html', 'rt', encoding='utf8').read()


# 1) rank
rank_pattern = re.compile(r'rank ">(\d{1,})</span>')
rank_content = re.findall(rank_pattern, source)
# print(rank_content)

# 2) title
title_pattern = re.compile(r';" title="(.*?)\s재생">')
title_content = re.findall(title_pattern, source)
# print(title_content)

# 3) artist
artist_pattern = re.compile(r'checkEllipsis.*?goArtistDetail.*?- 페이지 이동" >(.*?)</a>', re.DOTALL)
artist_content = re.findall(artist_pattern, source)
# print(artist_content)                                     # 왜 findall로 해서 두번 나오는 것을 또 걸러줬는지 의문
                                                            # 더 의문은 아래서는 또 search로 했다는것.. ;; ???
# 4) album                                                  # 스트링으로 뽑으려고 search로 바꿈 ㅡ_ㅡ;;
album_pattern = re.compile(r'ellipsis rank03".*?- 페이지 이동">(.*?)</a>', re.DOTALL)
album_content = re.findall(album_pattern, source)
# print(album_content)

# 이유는 모르겠지만 코드 상에서 찾을 수 없음.
# # 5) like
# like_pattern = re.compile(r'총건수</span>\n(.*?|,?)</span>', re.DOTALL)
# result5 = re.findall(like_pattern, source)
# print(result5)



# <tr> finditer로 match객체 찾기
tr_pattern = re.compile(r'<(tr class="lst50".*?)</tr>', re.DOTALL)
tr_iter = re.finditer(tr_pattern, source)

# 출력으로 tr코드 확인
# num = 1
# for i in tr_iter:
#     print(i.group())
#     print(f'{num}순위 tr 코드 가져오기')
#     num += 1



# 1) 수업시간에 못해본 1줄 리스트 출력해보기 by re.findall
# for i in tr_iter:
#     print( re.findall(rank_pattern, i.group()), end = '')
#     print( re.findall(title_pattern, i.group()), end = '' )
#     print( re.findall(artist_pattern, i.group()), end = '' )
#     print( re.findall(album_pattern, i.group()), end = '\n' )


# 2) 수업시간에 못해본 1줄 리스트 출력해보기 by re.search
# for i in tr_iter:
#     print( re.search(rank_pattern, i.group()).group(1), end = ' ')
#     print( re.search(title_pattern, i.group()).group(1), end = ' ' )
#     print( re.search(artist_pattern, i.group()).group(1), end = ' ' )
#     print( re.search(album_pattern, i.group()).group(1), end = '\n' )


# 3) 딕셔너리에 넣기

# melon_chart = list()
# melon_dict = dict()
#
#
# for i in tr_iter:
#     melon_dict['rank'] = re.search(rank_pattern, i.group()).group(1)
#     melon_dict['title'] = re.search(title_pattern, i.group()).group(1)
#     melon_dict['artist'] = re.search(artist_pattern, i.group()).group(1)
#     melon_dict['album'] = re.search(album_pattern, i.group()).group(1)
#     melon_chart.append(melon_dict)
#     # print(melon_chart)
#
# # print(melon_dict2) # 마지막 melon_dict 확인


# 4) 문제 굉장히 지저분하게 해결.
#
# melon_chart = list()
# melon_dict = dict()
# melon_dict2 = dict()
#
#
# for i in tr_iter:
#     melon_dict['rank'] = re.search(rank_pattern, i.group()).group(1)
#     melon_dict['title'] = re.search(title_pattern, i.group()).group(1)
#     melon_dict['artist'] = re.search(artist_pattern, i.group()).group(1)
#     melon_dict['album'] = re.search(album_pattern, i.group()).group(1)
#     # 딕셔너리에 잘 들어갔는지 확인
#     melon_dict2 = melon_dict.copy()
#     melon_chart.append(melon_dict2)
#     melon_dict.clear()                     # 1) 딕셔너리에 같은게 계속 들어가서 덮어씌워지고 있었음?
#     # 리스트에 딕셔너리가 잘 들어갔는지 확인         # 2) 그런데 .clear() 함수를 쓰면 리스트에 들어간 놈들까지 다 없어짐 ;;;
#     # print(melon_chart)                   # 3) 아마 리스트안의 것들의 참조값이 같았던 모양..
#                                            # 4) deep copy를 하는 .copy() 함수로 겨우 해결.
#
# # print(melon_dict2) # 마지막 melon_dict 확인



## 딕셔너리 50개의 객체가 아니라 들어갈때 같은 딕셔너리에 내용이 덮어서 들어갈때 그렇게 된것.



# 1) rank
rank_pattern = re.compile(r'rank ">(\d{1,})</span>')
rank_content = re.findall(rank_pattern, source)
# print(rank_content)

# 2) title
title_pattern = re.compile(r';" title="(.*?)\s재생">')
title_content = re.findall(title_pattern, source)
# print(title_content)

# 3) artist
artist_pattern = re.compile(r'checkEllipsis.*?goArtistDetail.*?- 페이지 이동" >(.*?)</a>', re.DOTALL)
artist_content = re.findall(artist_pattern, source)
# print(artist_content)                                     # 왜 findall로 해서 두번 나오는 것을 또 걸러줬는지 의문
                                                            # 더 의문은 아래서는 또 search로 했다는것.. ;; ???
# 4) album                                                  # 스트링으로 뽑으려고 search로 바꿈 ㅡ_ㅡ;;
album_pattern = re.compile(r'ellipsis rank03".*?- 페이지 이동">(.*?)</a>', re.DOTALL)
album_content = re.findall(album_pattern, source)
# print(album_content)




# 5) 딕셔너리 생성하는 위치 바꾸기 - 위치 하나로 위의 모든 불필요한 과정 생략.


melon_chart = list()


for i in tr_iter:
    melon_dict = dict()

    melon_dict['rank'] = re.search(rank_pattern, i.group()).group(1)
    melon_dict['title'] = re.search(title_pattern, i.group()).group(1)
    melon_dict['artist'] = re.search(artist_pattern, i.group()).group(1)
    melon_dict['album'] = re.search(album_pattern, i.group()).group(1)
    # 딕셔너리에 잘 들어갔는지 확인
    melon_chart.append(melon_dict)
    # 리스트에 딕셔너리가 잘 들어갔는지 확인
    print(melon_chart)

# print(melon_dict) # 마지막 melon_dict 확인




# 최종결과 확인
# 1줄씩 출력
for i in range(0, len(melon_chart)):
    print( melon_chart[i] )

# 리스트 통째로 출력
# print(melon_chart)