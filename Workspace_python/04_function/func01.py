def hello01():
    print('hello, world!')

hello01()

# 문자열 return
def hello02():
    return 'hello, return!'

print(hello02())

# dict 형식으로 return
def hello03():
    return {'name' : 'dongchan', 'age' : '29'}

print(hello03())

def hello04():
    print('hello04, return')
    return

# return을 사용하지 않거나 return 값이 없어 None이 뜸.
print(hello04())
print(hello01())

# return을 여러 번 사용하는 경우 하나만 뜬다. 애초에 들여쓰기 인식을 안함.
def hello05():
    return 1
    return 2
    return 3

print(hello05())