# dictionary
# {key : value, ...} set과 마찬가지로 {}로 둘러싸여 있지만 내부 형태가 다르다.
# 순서 O, 중복 (key X, value O)
# python 3.6부터 순서 있음!
# python은 type을 알아서 추론한다. type 추론
dict01 = {'a' : 1, 'b' : 2, 'c' : 3}
print(dict01)
print(type(dict01))
print(dict01['b'])

dict01['d'] = 4
print(dict01)

dict02 = dict(a = 1, c = 2, b = 3)
print(dict02)

dict03 = dict([[1, 'a'],[2,'b']])
print(dict03)
print(type(dict03))

print(dict03.keys())
print(dict03.values())

print(list(dict03.keys()))
