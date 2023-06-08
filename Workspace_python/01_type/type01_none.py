# 한 줄 주석 : 사람을 위한 설명
'''
여러 줄 주석
여러 줄로 설명
'''

a = 1  # a라는 변수에 값 1을 대입
print(a)  # a라는 변수를 콘솔에 출력해주세요.
print(type(a))
print('---------')

# None : 다른 언어에서는 Null이라고 부른다. = 값이 없음. undefined는 정의되지 않음.(변수 자체가 없음.)
b = None
print(b)
print(type(b))
print('---------')
# print(c) # 변수가 정의되지 않음. 실행하기도 전에 빨간 줄이 그어져있다.
c = None
print(c)
print('---------')
# singleton : (객체가 하나만 만들어짐) 자주 쓰는 수를 미리 메모리에 할당해놓기 떄문임.
print(id(b))
print(id(c))