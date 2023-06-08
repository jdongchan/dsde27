# type hint (type annotation)

# -> return 값의 type을 알려주는 것. 다른 사람이 볼 때 편안함.
def test01(a, b) -> int:
    a, b = int(a), int(b)
    return a + b

# a: int, b: str - 원하는 값이 int입니다. str입니다. 이것도 사용자가 보기 편안하기 때문.
def test02(a:int, b:str) -> str:
    result = str(a) + b
    return result

# default 지정
def test03(a: int = 0, b: int = 0) -> int:
    return a + b


if __name__ == '__main__':
    print(test01('1', 2))
    print(test02(1, '2'))
    print(test03(b=3))