def greeting(func):

    def prn(*args, **kwargs):
        print('hello,', end = ' ')
        func(*args, **kwargs) # 함정

    return prn

@greeting
def myfunc01(name):
    print(name)

@greeting
def myfunc02():
    print('python!', 'hello, deco!') # 이게 함정이었네.

if __name__ == '__main__':
    myfunc01('world!')
    myfunc02()
