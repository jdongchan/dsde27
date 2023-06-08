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
        super().__init__()
        self.name = 'child'

    # override : 부모의 메서드를 가져다가 재정의
    def prn01(self):
        print(f'override : {self.name} + {self.age}')

if __name__ == '__main__':
    child = Child()
    child.prn01()
    child.prn02()