class Greeting:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('hello', end=' ')
        self.func(*args, **kwargs)

@Greeting
def myfunc():
    print('world!')

if __name__ == '__main__':
    myfunc()