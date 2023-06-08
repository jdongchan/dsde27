
# parameter : 함수 외부에서 전달되는 값을 받아서, 함수 내부에서 사용하기 위한 '변수'
def sum2(x):
    return x + 2

# argument : 함수 외부에서 전달되는 '값' args
# print(sum2(22))

# parameter 2개 사용
def sum_x_y(x, y):
    result = x + y
    return result
# print(sum_x_y(2, 3))

def my_x_y(x, y):
    return x + y, x - y
# tuple 형태로 반환
# print(my_x_y(2, 3))
# print(type(my_x_y(2, 3)))

# print(__name__) # 내가 나를 실행시키면 __main__, 다른 애가 나를 실행시키면 __내파일__
# print(__name__)을 주석처리 뺀 후에 func03에서 실행하면 func02 가 나온다.
if __name__ == '__main__' :
    print(sum2(3))
    print(sum_x_y(4, 5))
    print(my_x_y(6, 7))
    print('내가 스스로 실행되었을 때!')