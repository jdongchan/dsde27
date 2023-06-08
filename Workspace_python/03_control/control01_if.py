# if 조건 :
a = 2
if a == 1 :
    print(f'{a} 는 1 입니다.')

# if ~ else
b = 3
if a == b:
    print(f'{a} == {b}')
else :
    print(f'{a} != {b}')

# if ~ elif
if a > b :
    print(f'{a} > {b}')
elif a < b :
    print(f'{a} < {b}')
elif a != b :
    print(f'{a} != {b}')

# if ~ elif ~ else
c = 2
if b > c :
    print(f'{b} > {c}')
elif b < c :
    print(f'{b} < {c}')
else :
    print(f'{b} == {c}')

# 중첩
wheels = 2
engine = True

if engine :
    if wheels == 2 :
        print('바이크')
    elif wheels == 4 :
        print('자동차')
else:
    if wheels == 2 :
        print('자전거')
    if wheels == 4:
        print('네발자전거')