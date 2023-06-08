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

'''
<player - computer>

player              가위1     바위2      보3
computer    가위1     0       1(승)     2(패)
            바위2     -1(패)   0        1(승)
            보3      -2(승)   -1(패)    0  


'''

# 가위바위보 만들기
def game_process(player_num: int) -> None:
    prn = {1: '가위', 2: '바위', 3: '보'}
    computer_num = randint(1,3)

    if (player_num - computer_num) in [1, -2]:
        print('당신이 이겼습니다.')
    elif player_num == computer_num:
        print('비겼습니다.')
    else:
        print('컴퓨터가 이겼습니다.')

def play() -> None:
    while True:
        player_num = int(input('가위 : 1 | 바위 : 2 | 보 : 3 | 게임종료 : 4 -> 숫자를 입력하세요 : '))
        if player_num ==4:
            break
        elif player_num not in [1,2,3]:
            print('다시 입력해 주세요!')
            continue
        else:
            game_process(player_num)

    print('다음에 또 놀러오세요~')


if __name__ == '__main__':
    play()
