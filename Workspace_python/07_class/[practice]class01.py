class HelloClass:
    ex = 'Hi' # 클래스 변수 생성

    def greetings(self, name): # 메서드 (method) 생성, name이라는 parameter를 설정
        print(self.ex, f'Hello, World! {name}!') # 함수 안에서 클래스 변수를 사용할 때 self.## 라고 사용
        
if __name__ == '__main__':
    class01 = HelloClass()  # class instance (객체) 생성
    class02 = HelloClass()

    class01.greetings(name='정동찬')
    class02.greetings(name='정혁수')

    print(class01)  # HelloClass가 메모리(0x10c347d90와 같은 주소)에 객체로 저장되었고, 이를 class01 변수에 할당.
    print(type(class01))  # HelloClass 라는 class임을 알려준다.
    print(class01.ex)
