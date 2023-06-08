# 제네레이터 2
def sub_coroutine():
    character = list()
    while True:
        char = yield

        if char is None :
            return character

        character.append(list(map(lambda x : ord(x), char))) # ord: 아스키코드 변환 문자->ascii

#제네레이터 1
def coroutine():
    while True:
        character = yield from sub_coroutine() # yield from : 다른 제네레이터에게 다시 전달
        print(character)

if __name__ == '__main__':
    my_char = coroutine()
    next(my_char)

    my_char.send('Lee')
    my_char.send('Dong')
    my_char.send('Heon')
    my_char.send(None)

# 코루틴이 여러개 있을 수 있구나.