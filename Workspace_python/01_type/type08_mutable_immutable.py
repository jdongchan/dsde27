# mutable(값의 변화가 가능한) : list, set, dictionary
a = [1,2,3,4,5]
print(a)
print(id(a))
a.append(6) # a[0] = 2 와 같이 값을 변경해도 주소가 바뀌지 않는다.
print(a)
print(id(a))
print(id(a+[7]))

# immutable : numbers, tuple, str, frozenset
b = 10
print(b)
print(id(b))
b = 20
print(b)
print(id(b))

c = (1,2,3,4,5)
print(c)
print(id(c))
print(c + tuple(a))
print(c)
print(id(c))
c = c + tuple(a)
print(c)
print(id(c))

# mutable 객체는 값의 변화가 가능하여 add, append, pop과 같은 메서드가 가능하다.
# immutable 객체는 값의 변화가 불가능하여 위와 같은 메서드가 불가능하다.