class Parent:
    # python의 모든 것들이 object 의 자식들임
    # class Parent(object)
    def __new__(cls, *args, **kwargs):
        # 객체를 생성해주는 생성자 역할
        print('new Parent')

        return super().__new__(cls, *args, **kwargs)
        # 여기서는 super()가 object
    def __init__(self):
        # 객체 생성할 떄 instance 변수 초기화
        print('init Parent')
        self.name = 'parent'
        self.age = 100
    def prn01(self):
        print(f'prn01 : {self.name}')

    def prn02(self):
        print(f'prn02 : {self.name} / {self.age}')

class Child(Parent):
    # Parent를 상속받아 Child를 만듭니다.
    # 자식이 부모 클래스를 상속받았다고 하면 자식이 부모의 메서드를 쓸 수 있다.
    def __new__(cls, *args, **kwargs):
        print('new Child')
        return super().__new__(cls, *args, **kwargs)
        # super() : 부모 객체

    def __init__(self):
        print('init Child')
        self.name = 'child'
        # Child에서는 age가 선언되지 않았음.
if __name__ == '__main__':
    parent = Parent()
    parent.prn01()
    parent.prn02()
    print('-----------')
    child = Child()
    child.prn01()
    child.prn02()
    # 메모리에 자식 만들거야 하면 부모가 만들어진 후에 자식이 만들어진다.
    # child 만들기 전에 parent 먼저 만들고 child 만들어.
    # 부