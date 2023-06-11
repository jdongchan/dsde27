# private 변수와 메서드는 class 내부에서만 사용이 가능하다.
class HelloPrivate:
    def __init__(self):
        self.public = 'public variable'
        self.__private = 'private variable'

    def __private_method(self):
        print(f'private : {self.__private}')

    def public_method(self):
        print(f'public : {self.public}')
        self.__private_method()  # class 내부에서는 사용이 가능하다.

if __name__ == '__main__':
    class06 = HelloPrivate()
    print(class06.public)
    # print(class06.private)  # 위에서 __붙여놓았음.
    class06.public_method()
    # class06.private_method() # 위에서 __붙여놓았음.
