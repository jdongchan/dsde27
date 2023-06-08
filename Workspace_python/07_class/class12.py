class Parent:
    class_val = 'class variable'

    @classmethod
    def class_method(cls):
        print(cls.class_val)

    @staticmethod
    def static_method():
        print('static')

    # class와 static의 공통점 : 클래스 안에서 기능을 수행하고 싶어서 객체 하나하나 x
    # 차이점 : class(cls) 파라미터가 있다
    # parent의 상속 받아 출력하는 class method에 cls에 전달되는 값이 달라진다.
class Child(Parent):
    class_val = "child's class variable"

if __name__ == '__main__':
    parent = Parent()
    parent.class_method()
    # cls 가 Parent
    parent.static_method()
    print('----------')
    child = Child()
    child.class_method()
    # cls 가 Child
    child.static_method()