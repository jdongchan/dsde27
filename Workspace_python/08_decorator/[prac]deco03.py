def greeting(func):
    def hello(name):
        print('hello')
        func(name)
        print('this is your world')
    return hello
@greeting
def myname(name):
    print(name)

if __name__ == '__main__':
    myname('dongchan')

