def greetings(name):
    prefix = '안녕하세요, '

    # lexical scope : suffix라는 함수가 선언될 때, 변수의 범위(scope)가 정해진다.
    # 내부함수에서 외부함수에 있는 파라미터를 사용할 수 있는 상황 = closure
    def suffix():
        return prefix + name + '님! 반갑습니다^^'
        # 함수가 값으로 사용되고 있다. parameter나 변수로 사용됨.
        # 1급 함수, 1급 객체
    # return되는 suffix 함수가, greetings라는 함수가 종료되어도 greetings의 환경 (name, prefix 같은 변수 값)을 기억한다.
    return suffix # suffix와 suffix()의 차이?


if __name__ == '__main__':
    print(greetings('정동찬')())
