    # class는 객체를 만든다.
    # greeting()
    # object : class를 가지고 memory에 구현한 구현체
    # C언어는 절차 지향
    # 파이썬은 Object Oriented Programming (OOP)
    # 기능별로 객체를 나누어서 만들자!
    # ex 게임 프로그래밍 맵, 캐릭터, 무기, 몬스터 설계도
    # 객체 지향 프로그래밍의 장점 : 기능 별로 설계도로 만들고 다른 프로그램에 적용하기 좋다.
    # 객체 지향 프로그래밍의 단점 : 설계도가 무조건 있어야 한다.
    # 객체 지향의 특징 :
    # 추상화, 상속, 다형성 : ex 멍멍이, 고양이, 코끼리 case
    # 공통 내용을 가지고 하나로 묶어 주는 것을 추상화라고 한다.
    # 하나로 묶은 것을 통해 뭔가를 만들어내는 경우 상속이라 한다.
    # 하나로 묶은 것으로 여러 가지를 만들 수 있는 것을 다형성이라 한다.
    # 캡슐화 : 함수 내부의 코드를 알 수 없다. 하지만 사용은 할 수 있다.
    # 함수는 기능을 수행하는 데 그 안에 들어가는 값이 달라지는 것
class HelloClass:
    def greetings(self):
            print('Hello, World!')

if __name__ == '__main__':
    class01 = HelloClass()
    class01.greetings()

    print(class01)
    print(type(class01))