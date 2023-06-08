class HelloClassDeco:
    cnt = 0

    def __init__(self):
        self.name = "hello class decorator"
        HelloClassDeco.cnt += 1

    @classmethod
    def class_method(cls):
        print(cls.cnt)
        # staticmethod vs classmethod : 상속

    def __del__(self):
        HelloClassDeco.cnt -= 1


if __name__ == "__main__":
    class08_1 = HelloClassDeco()
    class08_2 = HelloClassDeco()
    print(class08_1.cnt)
    class08_3 = HelloClassDeco()
    print(class08_2.cnt)
    class08_3.class_method()

    del class08_3
    class08_2.class_method()
