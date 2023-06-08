# for 변수 in collections :
# collections : list, tuple, set, dict, ...
# iterable 한 객체들 (__iter__, __next__)

subjects = ['python', 'science', 'engineer']

for sub in subjects :
    print(sub)

for i in range(1, 101):
    print(i, end = ' ')
print()

# 100부터 1까지 거꾸로 출력하자.

for i in range(100, 0, -1):
    print(i, end = ' ')
print()

# 중첩
for i in range(10):
    for j in range(10):
        print(f'({i},{j})', end = ' ')
print()

# 구구단 출력하자.
print('<구구단>')
for i in range (2,10):
    print(f'<{i}단>')
    for j in range (1,10):
        print(f'{i} * {j} = {i * j}')

for _ in range(3):
    print('hello, world!')

# enumerate : (index, value)

for idx, val in enumerate(subjects) :
    print(f'index : {idx}, value : {val}')