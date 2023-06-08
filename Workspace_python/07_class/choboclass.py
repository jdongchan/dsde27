# 251 클래스, 객체, 인스턴스
print('클래스는 객체를 만들어내는 틀')
print('객체는 클래스에 의해 메모리에 구현된 구현체')
print('인스턴스는 객체와 동일하다.')

#252 클래스 정의
class Human:
    pass

#253 인스턴스 생성
class Human:
    pass
areum = Human()

#254 클래스 생성자-1
class Human:
    def __init__(self):
        print('응애응애')
areum = Human()
areum

#255 클래스 생성자-2
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
areum = Human('아름', 25, '여자')

#256 인스턴스 속성에 접근
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
areum = Human('조아름', 25, '여자')
print(f'이름: {areum.name} 나이: {areum.age} 성별: {areum.sex}')

#257 클래스 메소드-1
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def who(self):
        print(f'이름: {self.name}, 나이: {self.age}, 성별: {self.sex}')

areum = Human('조아름', 25, '여자')
areum.who()

#258 클래스 메소드-2
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def who(self):
        print(f'이름: {self.name}, 나이: {self.age}, 성별: {self.sex}')

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human('뭐야', 0, '모름')
areum.who()
areum.setInfo('아름', 25, '여자')
areum.who()

#259 클래스 소멸자?

#260 에러의 원인
class OMG :
    def print(self):
        print('Oh my god')
mystock = OMG()
mystock.print()