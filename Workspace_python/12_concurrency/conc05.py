from threading import Thread
from datetime import datetime


value = 100000000
result = 0


def calc(name, start, end):
    cnt = 0
    for i in range(start, end):
        cnt += i

    print(f"{name} : {cnt}")

    global result
    result += cnt


def single_threading():
    start_time = datetime.now()

    global value
    global result

    result = 0

    t01 = Thread(target=calc, args=['thread', 1, value+1])
    t01.start()
    t01.join()

    print(f"result : {result}")
    end_time = datetime.now()
    print(f"single : {end_time - start_time}")


def multi_threading():
    start_time = datetime.now()

    global value
    global result

    result = 0

    t01 = Thread(target=calc, args=['thread1', 1, value // 2])
    t02 = Thread(target=calc, args=['thread2', value // 2 , value + 1])

    t01.start()
    t02.start()

    t01.join()
    t02.join()

    print(f"result : {result}")
    end_time = datetime.now()
    print(f"multi : {end_time - start_time}")


if __name__ == "__main__":
    single_threading()
    print("-----")
    multi_threading()
    # 철학자들의 저녁식사

    # 거의 차이가 없음!
    # GIL (Global Interpreter Lock)
