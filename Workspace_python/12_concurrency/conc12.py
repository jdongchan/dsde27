from threading import Thread
from datetime import datetime
from multiprocessing import Process


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


@mylogger
def process_way():
    process_list = [Process(target=calc, args=("process", )) for _ in range(10)]
    for prc in process_list:
        prc.start()
    for prc in process_list:
        prc.join()


if __name__ == "__main__":
    func_way()
    thread_way()
    process_way()



