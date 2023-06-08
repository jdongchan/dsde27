# Python 3.10 ~ 버전부터 사용 가능.

a = input('1 ~ 3 사이의 값을 입력해주세요 : ')
match a :
    case "1" :
        print('one')
    case "2" :
        print('two')
    case "3" :
        print('three')

season = int(input('월 입력:'))
match season :
    case 12 | 1 | 2 :
        # or, and 지원 안해줌. | & 을 사용한다.
        print('겨울')
    case 3 | 4 | 5 :
        print('봄')
    case 6 | 7 | 8 :
        print('여름')
    case 9 | 10 | 11 :
        print('가을')
    case _:
        print('1 ~ 12 사이의 값을 입력해 주세요!')
        # _ : 값을 사용하고 싶지 않을 때, 다른 게 전부 해당되지 않을 때