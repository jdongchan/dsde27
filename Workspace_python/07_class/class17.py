class A:
    pass

class CreateMeta(type):
    def __new__(cls, *args, **kwargs):
        print('new metaclass')
        return(super().__new__(cls, *args, **kwargs))

    def __init__(self, *args, **kwargs):
        print('init metaclass')

    def __call__(self, *args, **kwargs):
        print('call metaclass')
        return super().__call__(*args, **kwargs)

if __name__ == '__main__':
    num = 10
    print(type(num))

    # class의 type은 type이다. = 객체다.
    print(type(A))

    print('-------')

    # class 생성
    metaclass = CreateMeta('class', (), {})
    # metaclass는 memory에 적재되지는 아니다. namespace에 올라간다.
    print(metaclass)

    # instance 생성
    my_instance = metaclass()
    print(my_instance)

    print('---------')

    hello_meta = type('hello_meta', (), {}) # () : *args {} : **kwargs
    print(hello_meta)
    hello_instance = hello_meta()
    print(hello_instance)
