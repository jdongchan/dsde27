from multiprocessing import Process
import os


def child():
    print(f"child : {os.getpid()}")


if __name__ == "__main__":
    print(f"parent : {os.getpid()}")
    children = [Process(target=child) for _ in range(5)]

    for prc in children:
        prc.start()
