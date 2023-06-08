from threading import Thread, Lock
from time import sleep


resource = 0


def increase_resources():
    global resource
    resource += 1


class LockTest(Thread):

    def __init__(self, name, lock):
        Thread.__init__(self)
        self.name = name
        self.lock = lock

    def run(self):
        global resource
        resource = 0

        for i in range(10):
            self.lock.acquire()
            increase_resources()
            sleep(0.5)
            self.lock.release()

            print(f"{self.name} ({i}) : {resource}")


if __name__ == "__main__":
    lock = Lock()
    thread_list = [LockTest("t01", lock),
                   LockTest("t02", lock),
                   LockTest("t03", lock),
                   LockTest("t04", lock),
                   LockTest("t05", lock)]

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print(resource)


