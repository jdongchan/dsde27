# 산술 연산
a = 17
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# power (거듭제곱)
print(a ** b)
# floor division (몫)
print(a // b)
# modulo (나머지)
print(a % b)
a, b = 5, 3
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print('------')
print(a is b)
print(a is not b)

# 여러 개 한 번에 비교 가능!
print(1 < a < b)

# and : 둘 다 True일 때만 True
print(True and True)
print((a > 1) and (b > 1))

# or : 둘 중 하나만 True이면 True
print(True or False)

# and
print(True & True)
# or
print(False | True)

# not : 반전
print(not True)

# 멤버 연산
list01 = [1, 2, 3, 4, 5]
print(3 in list01)
print(6 in list01)
print(6 not in list01)

# range : 해당 범위의 숫자 생성
print(range(10))

# range(stop) : 0 ~ stop - 1
list02 = list(range(10))
print(list02)


# range(start, stop) : start ~ stop - 1
list03 = list(range(10,20))
print(list03)

# range(start, stop, step) : start, start + step, start + step + step, ..., stop - 1
list04 = list(range(1, 10, 2))
print(list04)

# 10부터 1까지 거꾸로
# print(list(range(0, 10, -1))) -> 무한대의 값이므로 연산을 하지 않음.
list05 = list(range(10,0,-1))
print(list05)

# slice
original = list(range(100))
print(original)

# [n] : index n
print(original[33])

# [start:stop] : start ~ stop - 1
slice01 = original[1:10]
print(slice01)
print(slice01[2])

# [start:stop:step]
slice02 = original[10:20:2]
print(slice02)

# [:stop] : 처음 ~ stop - 1
print(original[:10])

# [start:] : start ~ 끝
print(original[50:])

# [::step] : 처음, 처음 + 10, 처음 + 10 + 10 , ... , 끝
print(original[::10])

# 20부터 11까지 거꾸로 slice
slice03 = original[20:10:-1]
print(slice03)


# !를 빼고 출력
hello = "hello, world!"
print(hello[0:12])
print(hello[:12])
print(hello[:-1])

# world 만 출력
print(hello[7:12])
# world 만 두번 출력
print(hello[7:12] * 2)

# -1
print(hello[-1])
print(hello[:-1])
print(hello[::-1])

# 증감 연산자
c = 10
# c = c + 1
c += 1
print(c)

# c = c - 1
c -= 1
print(c)

# c = c * 2
c *= 2
print(c)

# c = c / 3
c /= 3
print(c)
# print(c++) 지원 안해줌!
