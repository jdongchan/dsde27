# 무언가 이 기능을 여러 번 사용할 것 같다. -> 함수로 만들자.
def bark(kind = '동물', sound = '울음소리'):
    print(f'{kind}가 {sound} 소리냅니다.')


if __name__ == '__main__':
    bark()
    bark('멍멍이', '왈왈')
    bark('고양이', '야옹')