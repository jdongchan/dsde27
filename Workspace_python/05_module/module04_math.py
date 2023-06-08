# import math
# from math import pi
import math as m

def circle(r):
    # return math.pi * r * r
    return m.pi * r * r

if __name__ == '__main__':
    r = int(input('반지름 입력 : '))
    print(f'반지름이 {r}인 원의 넓이는 {circle(r):.2f} 입니다.')