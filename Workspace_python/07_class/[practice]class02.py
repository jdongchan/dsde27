class HelloSelf:
    suffix = '님, 반갑습니다!' # 클래스 변수

    def __init__(self, name = '홍길동', age = 80 ): # special method init (초기화)
                                                 # name, age parameter 설정, default 설정
        self.name = name # 인스턴스 변수
        self.age = age

    def members_info(self): # 메서드
        return f'이름 : {self.name} 나이 : {self.age}'

if __name__ == '__main__':

    class01 = HelloSelf()
    print(class01.members_info()) # default를 넣어 반환한다.

    class02 = HelloSelf(name = '정동찬', age = 29)
    print(class02.members_info())
    class02.name, class02.age = '김명석', 42
    print(class02.members_info())
    print(dir(class02))
