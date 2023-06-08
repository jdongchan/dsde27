def input_num():
    # 숫자를 입력 받음
    # 만일, 숫자가 아닌 다른 것을 입력받을 경우, '다시 입력해 주세요!'라고 하고
    # 다시 입력 받음
    # 만일, 숫자가 입력되면 int() 를 사용해서 숫자로 변환한 후 리턴
    # 숫자가 아닌 다른 것들이 계속 입력되는 경우, 숫자가 입력될 때 까지 반복
    while True:
        try:
            num = int(input('숫자를 입력해 주세요 : '))
        except ValueError:
            print('다시 입력해 주세요!')
        else:
            break
    return num

if __name__ == '__main__':
    a = input_num()
    b = input_num()
    print(f'{a} + {b} = {a + b}')