from threading import Thread
from datetime import datetime


def mylogger(func):
    def logging():
        start = datetime.now()
        func()
        end = datetime.now()
        print(f"[time] : {end - start}")

    return logging


def calc(name):
    result = 0
    for i in range(100000000):
        result += i

    with open(f"{name}01.txt", "a") as f:
        f.write(str(result) + "\n")


@mylogger
def func_way():
    for i in range(10):
        calc("func")


@mylogger
def thread_way():
    threads = [Thread(target=calc, args=("thread", )) for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    func_way()
    thread_way()
    # cpu 연산 작업에서는 thread 차이 거의 없음



