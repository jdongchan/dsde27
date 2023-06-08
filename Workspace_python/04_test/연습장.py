class Person:
    name = '홍길동'
    _age = 15
    __address = '강남'
    def printInfo1(self):
        print('이름 : ',self.name)
        print('나이 : ',self._age)
        print('주소 : ',self.__address)

class01 = Person()
print(class01.__address)