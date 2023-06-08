from random import randint


'''
가위바위보 게임
출력 예)

가위 : 1 | 바위 : 2 | 보 : 3 | 게임종료 : 4 -> 숫자를 입력하세요 : 1
player (가위) vs computer(보) : 당신이 이겼습니다.
가위 : 1 | 바위 : 2 | 보 : 3 | 게임종료 : 4 -> 숫자를 입력하세요 : 2
player (바위) vs computer(가위) : 당신이 이겼습니다.
가위 : 1 | 바위 : 2 | 보 : 3 | 게임종료 : 4 -> 숫자를 입력하세요 : 3
player (보) vs computer(가위) : 컴퓨터가 이겼습니다.
가위 : 1 | 바위 : 2 | 보 : 3 | 게임종료 : 4 -> 숫자를 입력하세요 : 4
다음에 또 놀러오세요
'''

# 가위바위보 만들기
def game_process(player_num: int) -> None:
    computer_num = randint(1,3)
    if player_num == 1:
        if computer_num == 1:
            print('player (가위) vs computer (가위) : 비겼습니다.')
        elif computer_num == 2:
            print('player (가위) vs computer (바위) : 컴퓨터가 이겼습니다.')
        else:
            print('player (가위) vs computer (보) : 당신이 이겼습니다.')
    elif player_num == 2:
        if computer_num == 1:
            print('player (바위) vs computer (가위) : 당신이 이겼습니다.')
        elif computer_num == 2:
            print('player (바위) vs computer (바위) : 비겼습니다.')
        else:
            print('player (바위) vs computer (보) : 컴퓨터가 이겼습니다.')
    else:
        if computer_num == 1:
            print('player (보) vs computer (가위) : 컴퓨터가 이겼습니다.')
        elif computer_num ==2:
            print('player (보) vs computer (바위) : 당신이 이겼습니다.')
        else:
            print('player (보) vs computer (보) : 비겼습니다.')

def play() -> None:
    while True:
        guide = '가위 : 1 | 바위 : 2 | 보 : 3 | 게임종료 : 4 -> 숫자를 입력하세요 :'
        select = int(input(guide))
        match select:
            case 1:
                game_process(player_num=1)
            case 2:
                game_process(player_num=2)
            case 3:
                game_process(player_num=3)
            case 4:
                break
            case _:
                print('다시 입력해주세요.')
    print('다음에 또 놀러오세요')

if __name__ == '__main__':
    play()
