class Singleton(type):
    # 객체를 하나만 놓고 불러다 쓰는거
    # 디자인 패턴 중 하나인 싱글턴 패턴은 객체를 하나만 만들고 싶어요 !
    __instance = {}

    def __call__(self, *args, **kwargs):
        if self not in self.__instance:
            self.__instance[self] = super().__call__(*args, **kwargs)

        return self.__instance[self]

class MyClass(metaclass=Singleton):
    pass

if __name__ == '__main__':
    a = MyClass()
    b = MyClass()

    print(a)
    print(b)
    print(a == b)