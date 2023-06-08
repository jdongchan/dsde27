def outer():
    prefix = 'outer'

    def inner():
        print(f'{prefix}, inner')

    return inner
# closure : (함수가 값으로 사용) 내부함수가 외부함수의 값을 사용
# 내부함수가 외부함수의 변수를 기억하고 있다.
# 함수가 값 자체로 사용된다.
# return을 통해 메모리가 날라갔지만, inner 함수 바깥에 있는 prefix가 일시기억되어 사용됨.

def func_param(func):
    func()() # inner라는 함수가 값으로 사용된다.

if __name__ == '__main__':
    func_param(outer) # 함수가 값으로 사용된 경우 outer 함수를 outer로 넣었음.


# 1. func_param(func) func <- outer 라는 값을 넣음
# 2. outer() -> return inner
# 3. inner()
# 4. print(f'{prefix}, inner')
