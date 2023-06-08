class HelloGetterSetter:
    def __init__(self, name='홍길동'):
        self.name = name
        self.__age = 100
        # 변수 앞에 __ 가 붙으면 외부에서 건드리지 못하게 하겠다는 의미. private 변수

    @property  # getter - 외부에서 값을 가져오게 할 수 있다.
    def age(self):
        return self.__age

    @age.setter # setter - 외부에서 값을 넣는 것을 가능하게 한다.
    def age(self, age):
        if age <= 0:
            self.__age = 0
        else:
            self.__age = age

    def __str__(self):
        return f'{self.name}, {self.__age}'

if __name__ == '__main__':
    class05 = HelloGetterSetter('김선달')
    print(class05)

    print(class05.age)
    class05.age = 50
    print(class05)

# 굳이 @getter, @setter 사용하는 이유 # @: decorator
# 자동차를 만든다고 하였을 때
# 자동차의 속도를 속성(클래스변수, 인스턴스변수)으로 넣었다고 하였을 때,
# 밖에서 이를 건들 수 있게 만든다면, 누군가가 -100을 설정할 수 있게 된다.
# 이를 setter 내에 설정하여서 이를 미연에 방지하도록 만들 수 있다.