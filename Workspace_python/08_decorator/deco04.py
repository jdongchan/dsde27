def greeting(func):

    def prn(name):
        print('hello', end=' ')
        func(name)

    return prn

# @greeting
def myfunc(name):
    print(name)

if __name__ == '__main__':
    # myfunc('world!')
    greeting(myfunc)('baby~')

# 1급 시민 (first civilization) -> 일급 함수 / 일급 객체
# -> 값으로 사용 가능