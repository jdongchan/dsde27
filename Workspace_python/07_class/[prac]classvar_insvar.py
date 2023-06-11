class Person:
    bag = list()
    def put_bag(self, stuff):
        Person.bag.append(stuff)
        # self 대신 Person을 사용하면 클래스 속성임을 더 명확하게 구분할 수 있다.

if __name__ == '__main__':
    James = Person()
    Jamie = Person()
    James.put_bag('key')
    Jamie.put_bag('wallet')
    print(f'James.bag : {James.bag}')
    print(f'Jamie.bag : {Jamie.bag}')
    # class 변수는 인스턴스끼리 공유한다.

class Person2:
    def __init__(self):
        self.bag = []
        # 속성을 인스턴스끼리 공유하지 않게 하기 위해서 인스턴스 변수로 선언.
    def put_bag(self, stuff):
        self.bag.append(stuff)

if __name__ == '__main__':
    Jack = Person2()
    Jacqueline = Person2()
    Jack.put_bag('키')
    Jacqueline.put_bag('지갑')
    print(f'Jack.bag : {Jack.bag}')
    print(f'Jacqueline.bag : {Jacqueline.bag}')