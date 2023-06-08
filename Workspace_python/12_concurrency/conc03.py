from threading import Thread
from time import sleep


value = 10


def calc(name, num, sleep_time):
    global value
    for i in range(10):
        value = value + num
        print(f"{name}{i} : {value}")
        sleep(sleep_time)


if __name__ == "__main__":
    print("main thread start")

    test = Thread(target=calc, args=['test', 1, 0.5])
    daemon = Thread(target=calc, args=("daemon", -1, 1))

    # daemon thread : thread를 보조하는 thread
    daemon.daemon = True

    test.start()
    daemon.start()

    print(f"test.isDaemon : {test.daemon}")
    print(f"daemon.isDaemon : {daemon.daemon}")

    print("main thread end")





