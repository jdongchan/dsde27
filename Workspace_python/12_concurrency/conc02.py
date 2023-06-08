from threading import Thread


class Animal(Thread):

    def __init__(self, name, msg):
        Thread.__init__(self)
        self.name = name
        self.msg = msg

    def run(self):
        for i in range(3):
            print(f"{self.name} : {self.msg} ({i}번째)")


if __name__ == "__main__":
    thread01 = Animal("멍멍이1", "멍멍1!")
    thread02 = Animal("멍멍이2", "왈왈!")
    thread03 = Animal("야옹이1", "야옹!")
    thread04 = Animal("야옹이2", "냐냐!")

    # start -> run 호출
    thread01.start()
    thread02.start()
    thread03.start()
    thread04.start()
    # thread01.run()
    # thread04.run()
