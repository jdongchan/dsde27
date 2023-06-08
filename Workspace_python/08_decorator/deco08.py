from datetime import datetime
from time import sleep

def mylogger(name):
    def wrapper(func):
        def logging():
            print(f'[{name}] {datetime.now()}')
            func()
            print(f'[{name}] {datetime.now()}')

        return logging
    return wrapper

@mylogger('dongchan') # 사용자한테 전달받을 수 없다.
def greeting():
    sleep(2)
    print('hello, world!')
    sleep(2)

if __name__ == '__main__':
    greeting()