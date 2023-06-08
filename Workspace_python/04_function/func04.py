def param01(param):
    print(f'param이라는 변수 안에 저장되어 있는 값 : {param}')

# default 값 설정
def param02(a='100', b='dongchan'):
    print(a)
    print(b)
    print('----')


# arguments
# * : 여러 개의 값을 한 번에 받을 수 있음! (packing)
def param03(*args):
    print(args)
    print('~~')
    for i, arg in enumerate(args):
        print(f'{i}번 파라미터의 값 : {arg}')

# kwargs = keyword arguments
# **kwargs : {key : value} 형식으로 parameter를 받음.
def param04(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(f'key : {k}    value : {v}')

# *args 와 **kwargs 섞어 쓰는 경우
def param05(*args,**kwargs):
    print(f'args : {args}')
    print(f'kwargs : {kwargs}')

if __name__ == '__main__':
    # 프로그램의 주 진입점
    param01('arguments')

    # param01() # parameter에 arg를 삽입하지 않았을 때 error가 발생한다.
    param02(29,'정동찬')
    # default 값을 정해주었기 때문에 error가 발생하지 않는다.
    param02(50)
    param02()
    param02(b='wow!')

    param03('a','b','c','d')
    param03([1,2,3,4])
    # list에 있는 여러 값을 전달하는 경우에 *을 붙여주어야 한다.
    param03(*[5,6,7,8])

    param04(a=1, b=2, c=3)
    # param04({'a':1,'b':2,'c':3})
    # param04(*{'a':1,'b':2,'c':3})
    param04(**{'a':1, 'b':2, 'c':3})

    param05('a','b','c', d=1, e=2, f=3, g=4)

    # print(*object, sep=' ', end='\n', file=None, flush=False)