def greeting(name):

    def wrapper(func):

        def prn():
            print(f'hello, {name}')
            func()

        return prn

    return wrapper

@greeting('world') # 데코레이터에 값을 전달
def myfunc():
    print('hello, python')

if __name__ == '__main__':
    myfunc()
    # greeting('world')(myfunc)()
    # wrapper(myfunc)()
    # prn()