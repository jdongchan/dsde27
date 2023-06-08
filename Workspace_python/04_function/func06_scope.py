# 변수 범위

# 전역 변수
x = 10

def test01():
    print(x)

test01()

def test02():
    # 지역 변수
    x = 20
    print(x)

test02()

def test03():
    # 해당 지역에서 사용하는 x는 전역변수를 사용하는 것!
    global x
    x = 30
    print(x)

# 전역변수 선언을 나중에 해주었기 때문에
test03()
print(x)
test01()

def outer01():
    y = 6

    def inner01():
        y = 9 # 만약에 얘가 없다면? -> 바깥에 있는 지역변수를 사용함. = 가까운 지역변수를 참조함.
        print(f'inner01.y : {y}')

    inner01()
    print(f'outer01.y : {y}')

outer01()

def test04():
    global y
    y = 3
    print(y)

test04()
print(f'global.y : {y}')

def outer02():
    global y
    y = 6

    def inner02():
        y = 9
        print(f'inner02.y : {y}')

    inner02()
    print(f'outer02.y : {y}')

outer02()
print(f'global.y : {y}')

def outer03():
    y = 9
    # inner03() 안의 nonlocal이 적용되는 범위
    def inner03():
        # 지금 지역 말고 바로 바깥 지역에서 사용하겠다. nonlocal을 global 느낌으로 사용할 수는 없다.
        nonlocal y
        y = 3
        print(f'inner03.y : {y}')

    inner03()

    print(f'outer03.y : {y}')

outer03()
print(f'global.y : {y}')

# pass : 지금 껍데기만 남겨놓을 거고, 쓰진 않을거야.
def test999():

    pass