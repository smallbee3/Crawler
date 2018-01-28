import requests
import re


# # response = requests.get('https://www.melon.com/chart/index.htm')
# # html = response.text
# # print(html)
#
#
# source = '''<td><div class="wrap">
# <div class="wrap_song_info">
#     <div class="ellipsis rank01"><span>
#         <a href="javascript:melon.play.playSong('19030101',30851703);" title="다른사람을 사랑하고 있어 재생">다른사람을 사랑하고 있어</a>
#     </span></div><br>
#     <div class="ellipsis rank02">
#         <a href="javascript:melon.link.goArtistDetail('514741');" title="수지 (SUZY) - 페이지 이동">수지 (SUZY)</a><span class="checkEllipsis" style="display: none;"><a href="javascript:melon.link.goArtistDetail('514741');" title="수지 (SUZY) - 페이지 이동">수지 (SUZY)</a></span>
#     </div>
# </div>
# </div></td>'''



# result = re.findall(r'title="\w*', source)

# result = re.findall(r'>\w+|\s+</a>', source)   # 엉망코드

# print(result)



# p1 = re.compile(r'<div class="ellipsis rank01">.*title=".*?</div>', re.DOTALL)
# p1.findall(source)
# print(p1)

# # 위에서 p1을 한번 더 해야되는 이유
# p = re.compile(r'<a.*?')
# result = re.findall(p, source)
# for index, item in enumerate(result):
#     print(index, item)



# 위에서 div class에서 한번 짜르고 그걸 가지고 한번 더 짜르고.
#
#
# pattern_div_rank01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)
# # result = re.findall(pattern_div_rank01, source)
# # for index, item in enumerate(result):
# #     print(index, item)
#
# div_rank01 = re.search(pattern_div_rank01, source).group()
# print(div_rank01)
#
# pattern_a_content = re.compile(r'<a.*?>(.*?)</a>')
#
#
#
# title = re.search(pattern_a_content, div_rank01).group(1)
# print(title)
#
#


# 1단계 : 전체 html 가져오기
f = open('melon.txt', 'rt')
source = f.read()
# print(source)


# 한줄로 닫아줄 필요 없게.

# source = open('melon.html', 'rt').read()

# 참조한 객체는 없어서 자동으로 닫힘.


# 2단계 : tbody 짜르기

pattern_tbody = re.compile(r'<tbody>.*?</tbody>', re.DOTALL)
content_tbody = re.search(pattern_tbody, source)
tbody = content_tbody.group()
# print(result.group())



# 3단계 : <tr class="lst50" 까지 짜르기 > finditer로 반복가능한 iterator 저장.

pattern_lst50 = re.compile(r'<tr class="lst50.*?</tr>', re.DOTALL)
result_iter = re.finditer(pattern_lst50, tbody)
num = 1
for i in result_iter:
    print(f'{num}순위 곡의 tr class 출력')
    print(i.group())
    print(' ')
    print(' ')
    num += 1

# print(result_iter)

