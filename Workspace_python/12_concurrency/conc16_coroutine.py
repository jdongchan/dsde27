def hello():
    while True:
        name = yield # 제네레이터
        print(f'hello, {name}')

if __name__ == '__main__': # 서브루틴 : 메인스레드 -> 서브스레드 -> 메인스레드
                           # 코루틴 : 메인스레드와 서브스레드가 동시에 돌아감.
    coroutine = hello()
    next(coroutine)

    coroutine.send('홍길동') # yield에 값을 전달
    coroutine.send('김선달')
    coroutine.send('이순신')