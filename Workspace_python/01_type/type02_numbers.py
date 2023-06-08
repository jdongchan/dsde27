# Number

# int : 정수
a = 100
print(a)
print(type(a))
print('---------')
# int 생성자
b = int(101)
print(b)
print(type(b))
print('---------')
# float : 실수
c = 200.2
print(c)
print(type(c))
print('---------')
# float 생성자
d = float(200.2)
print(d)
print(type(d))
print('---------')
# 정수 + 실수, a + d : 값 자체 literal
print(a + d)
print(type(a + d))
print('---------')
# complex : 복소수
# real + imaginary (실수부 + 허수부 j)
e = 1 + 2j
print(e)
print(type(e))
print('---------')
# complex 생성자
f = complex(3, 4)
print(f)
print(type(f))
print('---------')
# bool : 논리형
g = True
h = False

print(g)
print(h)
print(type(g))
print(type(h))

print(1 == g)  # = 은 대입연산자 == 은 비교연산자
print(0 == h)
print(0 != h)
print('---------')
# 진법
# 2진수
binary = 0b1111
print(binary)
# 8진수
octal = 0o77
print(octal)
# 16진수
hexadecimal = 0xff
print(hexadecimal)
print('---------')
