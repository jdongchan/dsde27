# 함수의 실행 상황을 추적할 때 사용한다.
def trace(func):
    def wrapper():
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 끝')
    return wrapper # 함수 내에 만든 함수를 리턴값으로?? -> 클로저

@trace
def hello():
    print('hello')

@trace
def world():
    print('world')


hello()
world()

