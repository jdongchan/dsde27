# fibonacci numbers
# 0 1 1 2 3 5 8 13 21 34

def fibo(n):
    i = 0
    li = list()
    while i < n:
        if i <= 1:
            li.append(i)
        else:
            li.append(li[i-2]+li[i-1])
        print(li[i], end=' ')
        i += 1



if __name__ == '__main__':
    n = int(input('출력할 갯수 입력 : '))
    fibo(n)
