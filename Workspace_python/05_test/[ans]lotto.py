from random import randint


# 1 ~ 45 까지의 중복되지 않는 랜덤한 숫자 6개를 정렬하여 리턴하자
def make() -> list:
    li = []
    while len(li) < 6:
        num = randint(1, 45)
        if num not in li:
            li.append(num)
        else:
            continue
    return sorted(li)

# lotto = set()
# while len(lotto) < 6:
#     lotto.add(randint(1, 45))
#     return sorted(lotto)

if __name__ == '__main__':
    print(make())
