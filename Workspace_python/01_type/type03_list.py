# 여러 개의 값을 효과적으로 관리하기 위한 객체들 : list, tuple, set, dict
# Sequence : 순서가 있는 값들을 가진 객체
# list : 순서 O, 중복 O

# [값]
a = [5, 4, 3, 2, 3, 1]
print(a)
print(type(a))
a.append(6)
print(a)
print('---------')
# list() 생성자
b = list()
b.append(7)
b.append(9)
b.append(8)
print(b)
print(b.pop())
print(b)
print('---------')
# a라는 list에서 처음 나오는 숫자 3을 출력하고 싶다.
# list[index]
print(a[2])
# b에서 9출력
print(b[1])
print(type(b))
print('---------')
# dir() : 객체의 속성, 메서드 확인
print(dir(list))
# __??__ : special method (magic method)
# __iter__ : iterable(반복가능) -> iterator
# __len__, __getitem__ : sequenceable(연속적인)
print('---------')
# 거꾸로
b.reverse()
print(b)
print('---------')
# 정렬
b.sort()
print(b)
print('---------')
# 크기 확인
print(len(b))
print(len(a))
print('---------')
# list + list
c = a + b
print(c)
print('---------')
# * : 반복
print(b * 2)
print('---------')
# c list의 index 5의 위치에 숫자 6을 삽입
print(c)
c.insert(5,6)
print(c)
print('---------')
# 중첩
d = ['a', 'b', 'c', 'd', 'e', ['f', 'g', 'h'], 'i']
print(d)
print(len(d))
print('---------')
# 문자열 "d" 출력
print(d[3])
# d 안에 있는 list 출력
print(d[5])

# f 출력
print(d[5][0])





