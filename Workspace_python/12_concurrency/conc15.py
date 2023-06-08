from concurrent.futures import ThreadPoolExecutor
from time import sleep

values = list(range(1,1001))

def power3(n):
    return n ** 3

def work():
    print('work start')
    sleep(0.5)
    print('work stop')

def callback(n):
    print(f'future.running : {n.running()}')
    print(f'future.done : {n.done()}')

def threadpool():
    with ThreadPoolExecutor(max_workers=2) as executor:
        results = executor.map(power3, values)
        print(list(results))

        future = executor.submit(power3)
        # callback 함수 - 지금 당장 실행하는 것이 아닌 필요할 때 호출하여 실행하는 함수.
        future.add_done_callback(callback)
        # 쓰레드가 모두 종료되면 callback이라는 함수를 실행시켜줘.

if __name__ == '__main__':
    threadpool()