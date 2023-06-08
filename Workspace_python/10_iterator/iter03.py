class MyIter:

    def __init__(self, end):
        self.start = 0
        self.end = end
        self.val = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start <= self.end:
            self.val = self.start ** 2
            return self.val
        else:
            raise StopIteration

    def __getitem__(self, item):
        if item < self.end:
            return list(self)[item]
        else:
            raise IndexError
        # item 은 인덱스이며, 인덱스에 해당하는 리스트의 값을 반환한다.
        # 만약, 인덱스를 넘어서는 경우 IndexError를 호출한다.
        # IndexError 설정을 하지 않으면 None을 리턴한다.


if __name__ == "__main__":
    for i in MyIter(10):
        print(i)

    print(list(MyIter(15)))
    print(MyIter(15)[15]) # list index 를 벗어난 [15]임.

