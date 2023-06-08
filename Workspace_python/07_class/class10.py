class Parent:
    def __init__(self):
        print('init parent')
        self.name = 'parent'
        self.age = 100

    def prn01(self):
        print(f'prn01 : {self.name}')

    def prn02(self):
        print(f'prn02 : {self.name} / {self.age}')

class Child(Parent):
    def __init__(self):
        print('init child')
        super().__init__() # 부모의 init 실행해서 값 쓸래요. 명시적으로.
        self.name = 'child'


if __name__ == '__main__':
    child = Child()
    child.prn01()
    child.prn02()