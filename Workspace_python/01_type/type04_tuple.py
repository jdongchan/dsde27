# tuple : ()
a = (1,2,3)
print(a)
print(type(a))
print(dir(a))
# a.append(4)
print('---------')
# tuple(값)
b = tuple([5, 6, 6, 7])
print(b)
print(type(b))

print(dir(b))
print(b.count(6))
print('---------')
c = a + b
print(c)
print('---------')
d = list(c)
print(d)
print(type(d))
print('---------')
# packing - tuple 형태로 묶어진다.
f = 1,2,3
print(f)
print(type(f))
print('---------')
# unpacking
g, h, i = f
print(g)
print(h)
print(i)
print('---------')
# ----
a, b = 2, 3
print(a)
print(b)
print('-------')
a, b = b, a
print(a)
print(b)