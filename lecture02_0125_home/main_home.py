
from lecture02_0125_home.utils_home import *
from lecture02_0125_home.song_id import *
import random

if __name__ == '__main__':
    result = get_top100_list()
    for item in result:
        print(item)


# 너무 많으니까 보기쉽게 랭크와 제목만 출력.—
if __name__ == '__main__':

    num = 0
    while True:
        if num == 0:
            print('\n\n= 멜론에 오신 것을 환영합니다. =')
            num += 1
        data = input('\n 원하시는 번호를 선택하세요.\n\n  1. TOP100 리스트보기 (실시간)\n  2. 곡 상세정보 보기\n  3. 인기곡의 ID 보기 (무작위 30곡)\n  4. 나가기\n\n')

        if data == '1':
            result = get_top100_list(True)
            print('')
            for i in range(len(result)):
                print(result[i])


        elif data == '2':
            print('')
            song_id = input('원하는 곡의 ID를 입력하세요 ')
            result = get_song_detail(song_id)

            print('')
            print(result)

        # elif data == '3':
        #     result = get_top100_list()
        #     for item in result:
        #         print(f'{ item["title"]:3} : {item["song_id"]}')
        #                             # {} 안에서 공백 넣을 때 :3 이렇게 쓴다.

        elif data == '3':
            result = get_top100_list()
            print('')
            for i in range(30):
                choice = random.choice(result)
                print(f'{choice["song_id"]} : {choice["title"]:7}')

        else:
            print('')
            print('= 감사합니다. =\n\n')
            break


