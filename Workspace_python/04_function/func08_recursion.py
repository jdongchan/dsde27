# 3! = 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2 * 1

def factorial_loop(n):
    value = 1
    for i in range(n, 0, -1):
        value *= i
    return print(f'{n}! = {value}')

def factorial_loop2(n):
    value = 1
    while n == 0 :
        value *= n
        n -= 1
    return (print(f'{n}! = {value}'))
    pass

# 재귀함수 : 나를 다시 호출하는 함수
def factorial_recursion(n):
    # 종료 조건 필수!
    if n == 1:
        return 1

    return n * factorial_recursion(n-1)
'''
    5 * factorial_recursion(4)
    5 * (4 * factorial_recursion(3))
    5 * (4 * (3 * factorial_recursion(2)))
    5 * (4 * (3 * (2 * factorial_recursion(1))))
    5 * (4 * (3 * (2 * 1)))
    5 * (4 * (3 * 2))
    5 * (4 * 6)
    5 * 24
    120
    # 엔지니어링을 위해 알고리즘 공부하다보면 재귀함수 내용이 나오기도 한다.
'''

if __name__ == '__main__':
    num = int(input('input num : '))
    print(factorial_loop(num))
    print(factorial_loop(num))