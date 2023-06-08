class MyException(Exception): # Exception 클래스 상속받아 재정의
    def __init__(self):
        super().__init__('내가 만든 예외입니다!!')

def user_defined_exception():
    try:
        a = 1
        b = 2
        if a + b == 3:
            raise MyException() # 예외를 강제로 발생

    except MyException as e:
        print(e)

if __name__ == '__main__':
    user_defined_exception()