

import re



source = '''<tr class="lst50" id="lst50" data-song-no="30851703">
    <td><div class="wrap t_right"><input type="checkbox" title="다른사람을 사랑하고 있어 곡 선택" class="input_check " name="input_check" value="30851703"></div></td>
    <td><div class="wrap t_center"><span class="rank ">1</span><span class="none">위</span></div></td>
        <!-- 차트순위 추가 -->
        <td><div class="wrap">
                <span title="순위 동일" class="rank_wrap">
                    <span class="bullet_icons rank_static"><span class="none">순위 동일</span></span>
                    <span class="none">0</span>
                </span>
        </div></td>
    <td><div class="wrap">
        <a href="javascript:melon.link.goAlbumDetail('10131396');" title="Faces of Love" class="image_typeAll">
            <img onerror="WEBPOCIMG.defaultAlbumImg(this);" width="60" height="60" src="http://cdnimg.melon.co.kr/cm/album/images/101/31/396/10131396_500.jpg/melon/resize/120/quality/80/optimize" alt="Faces of Love - 페이지 이동">
            <span class="bg_album_frame"></span>
        </a>
    </div></td>
    <td><div class="wrap">
        <a href="javascript:melon.link.goSongDetail('30851703');" title="다른사람을 사랑하고 있어 곡정보" class="btn button_icons type03 song_info"><span class="none">곡정보</span></a>
    </div></td>
    <td><div class="wrap">
        <div class="wrap_song_info">
            <div class="ellipsis rank01"><span>
                <a href="javascript:melon.play.playSong('19030101',30851703);" title="다른사람을 사랑하고 있어 재생">다른사람을 사랑하고 있어</a>
            </span></div><br>
            <div class="ellipsis rank02">
                <a href="javascript:melon.link.goArtistDetail('514741');" title="수지 (SUZY) - 페이지 이동">수지 (SUZY)</a><span class="checkEllipsis" style="display: none;"><a href="javascript:melon.link.goArtistDetail('514741');" title="수지 (SUZY) - 페이지 이동">수지 (SUZY)</a></span>
            </div>
        </div>
    </div></td>
    <td><div class="wrap">
        <div class="wrap_song_info">
            <div class="ellipsis rank03">
                <a href="javascript:melon.link.goAlbumDetail('10131396');" title="Faces of Love - 페이지 이동">Faces of Love</a>
            </div>
        </div>
    </div></td>
    <td><div class="wrap">
        <button type="button" class="button_etc like" title="다른사람을 사랑하고 있어 좋아요" data-song-no="30851703" data-song-menuid="19030101"><span class="odd_span">좋아요</span>
<span class="cnt">
<span class="none">총건수</span>
20,627</span></button>
    </div></td>
    <td><div class="wrap t_center">
        <button type="button" title="듣기" class="button_icons play " onclick="melon.play.playSong('19030101',30851703);"><span class="none">듣기</span></button>
    </div></td>
    <td><div class="wrap t_center">
        <button type="button" title="담기" class="button_icons scrap " onclick="melon.play.addPlayList('30851703');"><span class="none">담기</span></button>
    </div></td>
    <td><div class="wrap t_center">
        <button type="button" title="다운로드" class="button_icons download " onclick="melon.buy.goBuyProduct('frm', '30851703', '3C0001', '','0', '19030101');"><span class="none">다운로드</span></button>
    </div></td>
    <td><div class="wrap t_center">
        <button type="button" title="뮤직비디오" class="button_icons video " onclick="melon.link.goMvDetail('19030101', '30851703','song');"><span class="none">뮤직비디오</span></button>
    </div></td>
    <td><div class="wrap t_center">
        <button type="button" title="링/벨" class="button_icons bell disabled" disabled="disabled" onclick="melon.buy.popPhoneDecorate('0010000000000000','30851703')"><span class="none">링/벨</span></button>
    </div></td>
</tr>'''
#
#
# import re
#
# # 로컬 HTML문서 불러오기
# source = open('melon.txt', 'rt').read()
#
#
#
# # Patterns - title
# # <div class="ellipsis rank01> ~ </div>부분의 텍스트
# PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)
# # <a href=....>(내용)</a>
# PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')
#
#
# # 전체 문서에서 PATTERN_DIV_RANK01에 해당하는 match object목록을 순회
# match_list = re.finditer(PATTERN_DIV_RANK01, source)
# num = 1
# for match_div_rank01 in match_list:
#     # 각 순회에서 매치된 전체 문자열 (<div clas... ~ </div>)부분을 가져옴
#     div_rank01_content = match_div_rank01.group()
#
#     # 부분 문자열에서 a태그의 내용을 title변수에 할당
#     match_title = re.search(PATTERN_A_CONTENT, div_rank01_content)
#     title = match_title.group(1)
#     # print(title)
#     print(f'{num}순위 이미지 출력 {title}')
#     num += 1
#
#
#
#
# # Patterns - images
# PATTERN_IMG_RANK01 = re.compile(r'<img onerror.*?이동">', re.DOTALL)
# PATTERN_IMG_CONTENT = re.compile(r'src="(.*?)" alt')
#
#
# match_img_list = re.finditer(PATTERN_IMG_RANK01 , source)
# num = 1
# for match_img_rank01 in match_img_list:
#
#     img_rank01_content = match_img_rank01.group()
#
#     match_img = re.search(PATTERN_IMG_CONTENT, img_rank01_content)
#     img = match_img.group(1)
#     print(f'{num}순위 이미지 출력 {img}')
#     num += 1



## 텍스트 + 이미지 한줄 씩 가져오려다 실패 becase 튜플 언패킹을 잘못 이해함.

#
# match_img_list = re.finditer(PATTERN_IMG_RANK01 , source)
# num = 1
#
# # 전체 문서에서 PATTERN_DIV_RANK01에 해당하는 match object목록을 순회
# match_list = re.finditer(PATTERN_DIV_RANK01, source)
# num = 1
#
#
# tuple1 = (match_img_list, match_list)
# a, b = tuple1
#
# # 이렇게 될지는 몰라도 for문 우측에 오는 튜플은 그 안에 요소들이 반복되어야한다.
# ex) t =  tuple((x, y) for x in range(5) for y in range(5))
#  >>> t
# ((0, 0),
#  (0, 1),
#  (0, 2),
#  (0, 3),
#  (0, 4),
#  (1, 0),
#  (1, 1),
#  (1, 2),
#
# # 내가 만든 튜플로 for 문에 넣으려는 것은
# t = tuple(range(10))
# >>> t
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#
# for item in t:  # 원래 이렇게 해야되는 곳에
#     print(item)
#
# for x, y in t:  # 이런 연산을 시도하는 것과 다를 바 없음.
#     print(x, y)



#
# for match_div_rank01, match_img_rank01 in match_img_list, match_list:
#     # 각 순회에서 매치된 전체 문자열 (<div clas... ~ </div>)부분을 가져옴
#     div_rank01_content = match_div_rank01.group()
#
#     # 부분 문자열에서 a태그의 내용을 title변수에 할당
#     match_title = re.search(PATTERN_A_CONTENT, div_rank01_content)
#     title = match_title.group(1)
#     # print(title)
#     print(f'{num}순위 타이틀 출력 {title}')
#
#
#
#     # 각 순회에서 매치된 전체 문자열 (<div clas... ~ </div>)부분을 가져옴
#     img_rank01_content = match_img_rank01.group()
#
#     # 부분 문자열에서 a태그의 내용을 title변수에 할당
#     match_img = re.search(PATTERN_IMG_CONTENT, img_rank01_content)
#     img = match_img.group(1)
#     print(f'{num}순위 이미지 출력 {img}')
#     num += 1






######################################### 수업시간 #########################################


# <td>...</td> 요소를 찾기 위한 정규표현식
PATTERN_TD = re.compile(r'<td.*?>.*?</td>', re.DOTALL)
# 찾은 결과 리스트                                                     # <td></td>로 반복되는 부분을 findall로 찾아서
td_list = re.findall(PATTERN_TD, source)                           # td_list[index]처럼 바로 갖다쓰는 것이 포인트

# 리스트를 순회 (한줄로 깔끔하게 출력해서 알아보기 위한 코드로 아래 과정과는 무관)
for index, td in enumerate(td_list):
    td_strip = re.sub(r'[\n\t]+|\s{2,}', '', td)
    # print(f'{index:02}: {td_strip}')


# 인덱스3번에 해당하는 <td>...</td>가 커버이미지의 img태그를 가지고 있음
td_img_cover = td_list[3]
# img태그의 'src'내용을 가져오는 정규표현식
PATTERN_IMG = re.compile(r'<img.*?src="(.*?)".*?>', re.DOTALL)
# 정규표현식을 인덱스3번 td에 적용해 커버이미지 url을 가져옴
url_img_cover = re.search(PATTERN_IMG, td_img_cover).group(1)
print(url_img_cover)


# 인덱스5번에 해당하는 td가 곡 제목, 가수명을 가지고 있음
td_title_author = td_list[5]
# div.rank01에 곡 제목이 있음
PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)
# div.rank01부분을 가져옴
div_rank01 = re.search(PATTERN_DIV_RANK01, td_title_author).group()
# 'div.rank01 a'의 내용에 곡 제목 텍스트가 있음
PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')

# div.rank01에서 a태그의 내용을 가져와 title에 할당
title = re.search(PATTERN_A_CONTENT, div_rank01).group(1)
print(title)