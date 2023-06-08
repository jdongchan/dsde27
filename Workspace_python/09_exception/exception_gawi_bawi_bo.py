from random import randint
'''
1. GawiBawiBoException 이라는 class를 만들자. (Exception 상속받기!)
2. 만일, 사용자 입력 값이 [1, 2, 3, 4]가 아니라면 GawiBawiBoException을 발생시키자.
3. 예외 처리를 할 건데
3-1. 만일 숫자가 아닌 값을 입력하면
'숫자만 입력할 수 있습니다.'
'다시 입력해 주세요.'라고 출력 후 게임 진행
3-2. GawiBawiBoException이 발생했다면
'1, 2, 3, 4 중 하나만 입력할 수 있습니다.'
'다시 입력해 주세요'
3-3. 그 외의 예외가 발생하면
'문제가 생겼습니다. 관리자에게 연락해 주세요.'
4. 예외가 발생하지 않는다면
game_process 함수를 호출!
'''

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
