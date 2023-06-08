from dataclasses import dataclass

@dataclass(order=True)
class Person:
    name: str
    age: int
    phone: str

# @dataclass를 사용하니 __str__ 가 override 되어 있다.
# __str__을 자동생성하여 내가 보기 좋은 형태로 출력하고 있다.
@dataclass
class Address:
    addr: list[Person]

if __name__ == '__main__':
    hong = Person(name='홍길동', age=100, phone='010-1111-1111')
    lee = Person('이순신',50,'010-2222-2222')
    kim = Person(name='김선달', age=40, phone='010-3333-3333')

    print(hong)
    print(lee)
    print(kim)

    print(f'{hong.name}의 나이는 {hong.age}이고, 연락처는 {hong.phone} 입니다.')

    print(hong > lee) # 비교연산할 때 어떤 값을 기준으로 연산하고 있는가
    print(lee < kim)

    dsde27 = Address([hong, lee, kim])
    print(dsde27)