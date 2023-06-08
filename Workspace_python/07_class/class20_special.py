# special method ( magic method )

# __ge__() : >=
# __gt__() : >
# __le__() : <=
# __lt__() : <
# __eq__() : ==
# __ne__() : !=

# __add__() : +
# __sub__() : -
# __div__() : /

# __new__(), __init__() : 생성자
# __str__() : 객체 표현
# __repr__() : 객체 표현

class Line:
    def __init__(self, length = 0):
        self.length = length
        print(f'길이 {self.length}의 선이 생성되었습니다.')

    def __add__(self, other):
        return self.length + other.length

    def __sub__(self, other):
        return self.length - other.length

    def __gt__(self, other):
        return self.length > other.length

    def __ge__(self, other):
        return self.length >= other.length

    def __lt__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length

    def __eq__(self, other):
        return self.length == other.length

    def __ne__(self,other):
        return self.length != other.length

    def __str__(self):
        return f'{self.length}'

    def __repr__(self):
        return f'{self.length}의 길이를 가진 선'


if __name__ == '__main__':
    line1 = Line(10)
    line2 = Line(3)

    print(f'line1 : {line1.length}')
    print(f'line2 : {line2.length}')

    print(f'line1 + line2 : {line1 + line2}')
    print(f'line1 >= line2 : {line1 >= line2}')
    print(f'line1 > line2 : {line1 > line2}')
    print(f'line1 <= line2 : {line1 <= line2}')
    print(f'line1 < line2 : {line1 < line2}')
    print(f'line1 == line2 : {line1 == line2}')
    print(f'line1 != line2 : {line1 != line2}')

    print(line1)

    # eval : 명령 실행 - 보안에 취약하다. 사용하는 것을 지양한다.
    eval('Line(5)')
    eval('Line(5) + Line(5)')
    eval('print(3+4)')