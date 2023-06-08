def exception01():
    print(10 / 0)

def exception02():
    try:
        print(10/0)
    except:
        print('예외 발생!')

def exception03():
    try:
        print(10/0)
    except ZeroDivisionError: # except 뒤에 발생할 에러를 알려주면 그 타입에 대해 맞춤형 출력이 됨 if error ~ 라고 보면 좋을듯
        print('0으로 나눌 수 없습니다...')
    except:
        print('예외 발생!')

def exception04():
    try:
        a = [1, 2, 3, 4, 5]
        a[5]
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다...')

def exception05():
    try:
        a = [1, 2, 3, 4, 5]
        a[5]
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다...')
    except IndexError:
        print('리스트의 인덱스 범위를 벗어났습니다...')

def exception06():
    try:
        a = [1,2,3,4,5]
        a[5]

    except Exception as e:
        print(e)

def exception07():
    try:
        a = [1, 2, 3, 4, 5]
        a[0]
    except:
        print('예외 발생!')
    else: # 예외가 발생하지 않았기 때문에
        print(a)

def exception08():
    try:
        a = [1, 2, 3, 4, 5]
        a[0]

    except:
        print('예외 발생')

    else:
        print(a)

    finally:        # 예외가 발생하든 발생하지 않든 무조건 !
        print('끝!')

if __name__ == '__main__':
    # exception01()
    # exception02() # 정상적으로 종료
    # exception03()
    # exception04()
    # exception05()
    # exception06()
    # exception07()
    exception08()

