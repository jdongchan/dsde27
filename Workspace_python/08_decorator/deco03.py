def greeting(func):

    def prn():
        print('hello', end=' ')
        func()

    return prn

# greeting 함수를 decorator로 사용하는 경우 greeting(myfunc)()와 같아진다.
          # syntax sugar라고 말한다.
@greeting
def myfunc():
    print('world')

if __name__ == '__main__':
    # greeting(myfunc)()
    myfunc()

