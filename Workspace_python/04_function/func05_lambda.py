# lambda : 익명 함수 표현식
# lambda param : expression
def sum10(x, y):
    return x + y + 10

print(sum10(3, 4))

# 이 정도는 굳이 lambda를 쓸 필요가 없다.
sum20 = lambda x, y: x + y + 20
print(sum20(3, 4))
# def sum20(x, y):
#   return x + y + 20 와 같다.

result = (lambda x, y, z : x * y / z)(10, 20, 30)
print(result)

tuple_list = [(1, 'one', 9), (3, 'three', 7), (4, 'four', 6), (2, 'two', 8)]

print(tuple_list)
tuple_list.sort()
print(tuple_list)

# 어떤 key를 기준으로 정렬할 것인가 , self는 class 얘기할 때 나온다.
tuple_list.sort(key=lambda x: x[1])
print(tuple_list)

# lambda 중첩
result = (lambda x: lambda y: x * y)(10)(20)
print(result)

# list comprehension
hundred = [i for i in range(1, 101)]
print(hundred)
# 1 ~ 100 사이의 값 중, 5의 배수만 list, 5로 나눴을 때 0이 나오는 경우는 5의 배수임 -> 0 = False
# False 의 False는 True이기 때문에 5의 배수만 나오게 되는 것
five01 = [i for i in range(1, 101) if not (lambda x: bool(x % 5))(i)]
print(five01)
# x를 5로 나눈 나머지가 0이 아니라면, x를 그대로 가져가세요. 조건이 거짓이라면, None을 가져가세요.
five02 = [i for i in range(1, 101) if not (lambda x: x if (x % 5) != 0 else None)(i)]
print(five02)

num = [1,2,3]
char = ['a','b','c']

# zip을 사용할 때 두 인자의 길이가 같아야 한다. len(num) == len(char)
zip_test = zip(num, char)
print(zip_test) # zip object at 0x7fe6f00b0c80 값을 출력해주지 않고 객체로 저장만 한다.
print(list(zip_test))
# dict로 변환할 때는 중간에 변수를 사용하면 안된다 dict(zip_test) 불가능 - 파이썬이 그렇게 만듦
print(dict(zip(num, char)))

# map - 데이터 엔지니어링에서 많이 사용된다.
map_test = list(map(lambda x: x * 10, num))
print(map_test)

# filter
print(list(filter(lambda x: x > 1, num)))

# test_list 에서 숫자만 list로 생성하여 출력하자
test_list = ['3', '6', None, '9', '', 'a']
# 나의 답
print(list(filter(lambda x: x.isdigit(), list(map(lambda x: str(x), test_list)))))
# 강사님 답 : 이게 맞는듯
print(list(filter(lambda x: x.isdigit() if x else False, test_list)))
# is____()은 90% T/F, has____()도 90% T/F