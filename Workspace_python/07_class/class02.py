class HelloSelf:
    # 클래스 변수 class variable
    suffix = '님, 반갑습니다~'
    # __??__ : special method, magic method
    # 어떤 함수한테 종속되어있는 경우 메서드, 독립적인 경우 함수라고 한다.
    # __init__ : 객체 생성 시, 인스턴스(메모리에 구현된 객체) 변수 초기화
    # 인스턴스 : 객체 안에서 해당 객체가 사용하는 변수
    def __init__(self):
        # self.변수 -> 인스턴스 변수 instance variable
        # 객체마다 따로 가질 수 있는 값
        self.prefix = '안녕하세요,'
    def greetings(self, name):
        return f'{self.prefix} {name} {HelloSelf.suffix}'

if __name__ == '__main__':
    class02 = HelloSelf() # () : HelloSelf가 가진 생성자를 호출해주세요.
    class02.greetings('이동헌')
    class02.greetings('홍길동')

    class03 = HelloSelf()
    class03.greetings('김선달')

    HelloSelf.suffix = '하이하이~'
    class02.greetings('홍길동')
    class03.greetings('김선달')

    class02.prefix = '헬로헬로,'
    class02.greetings('홍길동')
    class03.greetings('김선달')

    HelloSelf.suffix = '니하오'
    class02.greetings('홍길동')
    class03.greetings('김선달')

