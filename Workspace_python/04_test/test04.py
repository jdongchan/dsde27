# fibonacci numbers
# 0 1 1 2 3 5 8 13 21 34
def fibo(n):
    a, b = 0, 1
    i = 0
    while i < n:
        print(a, end=' ')
        a, b = b, a + b # 파이썬이 변수의 값 바꾸는 것이 용이해서 나온 문제

        i += 1


if __name__ == '__main__':
    n = int(input('출력할 갯수 입력 : '))
    fibo(n)
