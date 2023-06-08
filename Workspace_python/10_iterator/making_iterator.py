import random
class Counter:
    def __init__(self, stop):

        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration

    def __getitem__(self, item):
        if item < self.stop:
            return item
        else:
            raise IndexError

if __name__ == '__main__':
    it = Counter(10)
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())


    # unpacking이 가능하다.
    it2 = Counter(5)
    a,b,c,d,e = it2
    print(a,b,c,d,e)

    # 인덱스로 접근가능한 이터레이터
    it3 = Counter(4)
    print(it3[3])

    # iter와 next 함수 활용하기 iter(호출가능한 객체, 반복을 끝낼 값: sentinel(감시병))
    it4 = iter(lambda : random.randint(0,5),2)
    print(next(it4))
    print(next(it4))