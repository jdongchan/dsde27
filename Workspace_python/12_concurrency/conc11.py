from threading import Thread
from multiprocessing import Process
from datetime import datetime


def work():
    pass


if __name__ == "__main__":
    workers = 10

    thread_start = datetime.now()
    threads = [Thread(target=work) for _ in range(workers)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    thread_end = datetime.now()
    print(f"thread time : {thread_end - thread_start}")

    process_start = datetime.now()
    process_list = [Process(target=work) for _ in range(workers)]
    for prc in process_list:
        prc.start()
    for prc in process_list:
        prc.join()
    process_end = datetime.now()
    print(f"process time : {process_end - process_start}")








