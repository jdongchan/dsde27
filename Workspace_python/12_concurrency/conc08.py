from threading import Thread
from datetime import datetime
import urllib.request


def mylogger(func):
    def logging():
        start = datetime.now()
        func()
        end = datetime.now()
        print(f"[time] : {end - start}")

    return logging


def crawling(name):
    with urllib.request.urlopen("http://python.org") as response:
        html = response.read().decode("utf-8").split("\n")[0]
        with open(f"{name}02.txt", "a") as f:
            f.write(html)


@mylogger
def func_way():
    for i in range(10):
        crawling("func")


@mylogger
def thread_way():
    threads = [Thread(target=crawling, args=("thread", )) for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    func_way()
    thread_way()
    # io, network 등의 작업에서는 multithreading 효과적!







