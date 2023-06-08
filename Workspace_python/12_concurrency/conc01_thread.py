from threading import Thread


def bark(name, msg):
    for i in range(3):
        print(f"{name} : {msg} ({i}번째)")


if __name__ == "__main__":
    thread01 = Thread(target=bark, args=("멍멍이1", "멍멍!"))
    thread02 = Thread(target=bark, args=("멍멍이2", "왈왈!"))
    thread03 = Thread(target=bark, args=("야옹이1", "야옹!"))
    thread04 = Thread(target=bark, args=("야옹이2", "냐냐!"))

    thread01.start()
    thread02.start()
    thread03.start()
    thread04.start()
    # context switching
